#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2019 Bitergia
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

import json
import requests

OAUTH2_TOKEN = 'https://secure.meetup.com/oauth2/access'

def get_token(client_id, client_secret, redirect_uri, code):
    access_uri = "{}?client_id={}&client_secret={}&redirect_uri={}&code={}&grant_type=authorization_code".format(OAUTH2_TOKEN,
        client_id,
        client_secret,
        redirect_uri.strip("\""),
        code
    )
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    r = requests.post(access_uri, headers=headers)
    r_json = r.json()
    print(json.dumps(r_json, sort_keys=True, indent=4))

def main():
    print("Access https://secure.meetup.com/meetup_api/oauth_consumers and create a consumer (if you don't have it)")
    print("Replace YOUR_CONSUMER_KEY and YOUR_CONSUMER_REDIRECT_URI with the correct info in the link below")
    print("https://secure.meetup.com/oauth2/authorize?client_id=YOUR_CONSUMER_KEY&response_type=code&redirect_uri=YOUR_CONSUMER_REDIRECT_URI")
    print("If everything goes OK, you will get a code as param of YOUR_CONSUMER_REDIRECT_URI, for instance: https://example.com/test?code=683f3ebe84bf867d2b8d591faa389ed5")
    print("Use this code, together with your client key, secret, redirect URI to get an access token")
    client_id = input('Enter your client key: ')
    client_secret = input('Enter your client secret: ')
    redirect_uri = input('Redirect URI: ')
    code = input('Code: ')
    print("***** ***** ***** *****")
    get_token(client_id, client_secret, redirect_uri, code)
if __name__ == "__main__":
    main()
