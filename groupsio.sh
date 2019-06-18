#!/bin/bash
if [ -z "$1" ]
then
  echo "$0: you need to provide group name, for example: zephyrproject, hyperledger. You must be sugscribed to that group"
  exit 1
fi
if [ ! -f "/etc/groupsio/token" ]
then
  echo "No saved groups.io token"
  echo -n "groups.io email/login: "
  read email
  echo -n "groups.io password: "
  read -s pass
  echo ""
  response=`curl -s "https://api.groups.io/v1/login" -u 123456: -d "email=${email}&password=${pass}"`
  token=`echo $response | jq -r '.token'`
else
  token=`cat /etc/groupsio/token`
fi
if ( [ -z "$token" ] || [ "$token" = "null" ] )
then
  echo "Cannot get token value, exiting"
  exit 1
fi
if [ ! -f "/etc/groupsio/token" ]
then
  echo $token > /etc/groupsio/token
fi
echo "Token: $token"
perceval groupsio -t "$token" "$1"
