#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'

import googleapiclient
import pydrive
import sys
import os
import argparse
import oauth2client
from oauth2client import file
from oauth2client import tools
from oauth2client import client
from googleapiclient.discovery import build

#sys.path.append(os.path.dirname(os.path.realpath(__file__))[:-6:])
#global tools
#import tools
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

'''
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

home_dir = os.path.abspath('google-cli-tools')
print home_dir
print os.path.join(home_dir, 'etc')
gauth = GoogleAuth(settings_file='etc/drive_setting.yaml')
gauth.LocalWebserverAuth()

drive = GoogleDrive()

file_list = drive.ListFile({'q': "'root' in parents"}).GetList()
for file1 in file_list:
    print 'title: %s, id: %s' % (file1['title'], file1['id'])
'''
import httplib2
FILENAME = os.path.abspath('google-cli-tools/drive/document.txt')

# Metadata about the file.
MIMETYPE = 'text/plain'
TITLE = 'My New Text Document'
DESCRIPTION = 'A shiny new text document about hello world.'


#http = authentication()
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
import pprint
# Perform the request and print the result.
new_file = drive_service.files().insert(body=body, media_body=media_body).execute()
pprint.pprint(new_file)
