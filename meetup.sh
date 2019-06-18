#!/bin/bash
# TODO: tokens
if [ ! -f "/etc/meetup/token" ]
then
  echo 'TODO: add token handling!'
  perceval meetup --sleep-for-rate hyperledger
  echo 'TODO: add token handling!'
else
  perceval meetup --sleep-for-rate -t `cat /etc/meetup/token` hyperledger
fi
