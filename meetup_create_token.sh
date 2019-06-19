#!/bin/bash
cat /etc/meetup/key /etc/meetup/secret /etc/meetup/redirect_uri /etc/meetup/code | ./meetup_create_token.py
