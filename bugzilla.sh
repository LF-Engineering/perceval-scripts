#!/bin/bash
if [ ! -f "/etc/bugzilla/login" ]
then
  echo "$0: please provide Bugzilla login in '/etc/bugzilla/login' file"
  exit 1
fi
if [ ! -f "/etc/bugzilla/pwd" ]
then
  echo "$0: please provide Bugzilla password in '/etc/bugzilla/pwd' file"
  exit 2
fi
#perceval bugzilla --from-date 2019-06-01 -u `cat /etc/bugzilla/login` -p `cat /etc/bugzilla/pwd` https://bugzilla.yoctoproject.org
perceval bugzilla -u `cat /etc/bugzilla/login` -p `cat /etc/bugzilla/pwd` https://bugzilla.yoctoproject.org
