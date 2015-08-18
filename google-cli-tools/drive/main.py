#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'

import mimetypes
import googleapiclient
from googleapiclient.discovery import build
from oauth2client import tools
from oauth2client import client
from oauth2client import file
import sys
import os
import argparse
import oauth2client
import httplib2
import readline
import glob

sys.path.append(os.path.dirname(os.path.realpath(__file__))[:-6:])
global tool
import tools as tool

APPLICATION_NAME = 'google-cli-tools'
CLIENT_SECRET_FILE = 'etc/client_secrets.json'
CREDENTIALS_PATH = 'etc/drive-api.json'
SCOPES = 'https://www.googleapis.com/auth/drive'


def authentication():
    flags = argparse.ArgumentParser(
        parents=[oauth2client.tools.argparser]).parse_args()
    home_dir = os.path.abspath('../google-cli-tools')
    print home_dir
    credential_dir = os.path.join(home_dir, 'etc/.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)

    store = oauth2client.file.Storage(CREDENTIALS_PATH)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = oauth2client.client.flow_from_clientsecrets(
            CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = oauth2client.tools.run_flow(flow, store, flags)
        else:
            credentials = oauth2client.tools.run(flow, store)
        print 'Storing credentials to %s' % CREDENTIALS_PATH
    return credentials


def complete(text, state):
    return (glob.glob(text+'*')+[None])[state]


readline.set_completer_delims(' \t\n;')
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)


filename = raw_input('Enter the path to file: ')
FILENAME = os.path.abspath(filename)
print os.path.basename(FILENAME)

mimetypes.init()
# Metadata about the file.
MIMETYPE = mimetypes.MimeTypes().guess_type(FILENAME)[0]
if MIMETYPE is None:
    MIMETYPE = 'text/plain'
TITLE = os.path.basename(FILENAME)
DESCRIPTION = 'A shiny new text document about hello world.'


credentials = authentication()
http = httplib2.Http()
credentials.authorize(http)
drive_service = googleapiclient.discovery.build('drive', 'v2', http=http)

# Insert a file. Files are comprised of contents and metadata.
# MediaFileUpload abstracts uploading file contents from a file on disk.
media_body = googleapiclient.http.MediaFileUpload(
    FILENAME,
    mimetype=MIMETYPE,
    resumable=True
)
# The body contains the metadata for the file.
body = {
    'title': TITLE,
    'description': DESCRIPTION,
}

# Perform the request and print the result.
new_file = drive_service.files().insert(
    body=body, media_body=media_body).execute()

tool.MyPrettyPrinter().pprint(new_file['alternateLink'])
