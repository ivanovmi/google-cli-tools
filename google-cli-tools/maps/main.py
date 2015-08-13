#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'

import gmaps
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))[:-5:])
global tools
import tools


def check_address(address, lang):
    """
    This module allow simple search by organization naming
    :param address: string, can be: 'NAME_ORG', 'COUNTRY', 'TOWN_NAME'
    :param lang: allow display result in available language
    :return: print result to CLI
    """
    full = ''
    try:
        data = gmaps.Geocoding().geocode(address=address,
                                         language=lang, sensor=True)
    except gmaps.errors.NoResults:
        print 'No places found'
        raise SystemExit
    for i in data:
        print i['formatted_address']

    while full.lower() not in ['y', 'yes', 'n', 'no']:
        full = raw_input('You wanna see f'
                         'ull result (Contain many debug info)[y/n]: ')

    if full.lower() in ['y', 'yes']:
        tools.MyPrettyPrinter().pprint(data)
    else:
        raise SystemExit


def reverse_check_address(lng, lat, lang):
    """
    This module allow simple search by coordinates
    :param address: num, can be: 1.1, 1.5
    :param lang: allow display result in available language
    :return: print result to CLI
    """
    full = ''
    try:
        data = gmaps.Geocoding().reverse(lat=lat, lon=lng, language=lang)
    except gmaps.errors.NoResults:
        print 'No places found'
        raise SystemExit
    for i in data:
        print i['formatted_address']

    while full.lower() not in ['y', 'yes', 'n', 'no']:
        full = raw_input('You wanna see full '
                         'result (Contain many debug info)[y/n]: ')

    if full.lower() in ['y', 'yes']:
        tools.MyPrettyPrinter().pprint(data)
    else:
        raise SystemExit
