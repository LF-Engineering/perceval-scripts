#!/bin/bash
# TODO: tokens
if [ ! -f "/etc/discourse/token" ]
then
  echo 'TODO: add token handling!'
  perceval discourse https://edgex.discourse.group
  echo 'TODO: add token handling!'
else
  perceval discourse -t `cat /etc/discourse/token` https://edgex.discourse.group
fi
