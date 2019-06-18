#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2018 Bitergia
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, 51 Franklin Street, Fifth Floor, Boston, MA 02110-1335, USA.
#
# Authors:
#     Valerio Cosentino <valcos@bitergia.com>
#
import requests
from requests.auth import HTTPBasicAuth
GROUPSIO_API_URL = 'https://api.groups.io/v1/'
GET_SUBSCRIPTIONS = 'getsubs'
PER_PAGE = 100
def urijoin(*args):
    """Joins given arguments into a URI.
    :returns: a URI string
    """
    return '/'.join(map(lambda x: str(x).strip('/'), args))
def fetch(url, payload, auth):
    """Fetch requests from groupsio API"""
    r = requests.get(url, params=payload, auth=auth)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise e
    return r
def get_subscriptions(api_token):
    auth = HTTPBasicAuth(api_token, '')
    url = urijoin(GROUPSIO_API_URL, GET_SUBSCRIPTIONS)
    keep_fetching = True
    payload = {
        "limit": PER_PAGE
    }
    while keep_fetching:
        r = fetch(url, payload, auth)
        response_raw = r.json()
        subscriptions = response_raw['data']
        for sub in subscriptions:
            print(sub['group_name'])
        payload['page_token'] = response_raw['next_page_token']
        keep_fetching = response_raw['has_more']
def main():
    groups_io_token = input('Enter your token: ')
    print("***** ***** ***** *****")
    get_subscriptions(groups_io_token)
if __name__ == "__main__":
    main()
