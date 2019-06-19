# perceval-scripts

Scripts to get data for various datasources.


# IRC

To be able toget data from any IRC channel we need to:

- Install supybot on that channel, which requires:
  - Dockerizing supybot to be able to run it on Kubernetes.
  - Run `supybot-wizard` somehow to generate bot config file, that will be used by the doc ker image.
  - Configure non-root user to run the bot (docker image must run as non-root, supybot forbids root).
  - Store supybot logs into some PV to make it available for the Perceval IRC backend pod
- Create Perceval IRC datasource pod that will have access to bot logs to analyze them
- List all IRC channels we need and subscribe supybot to all of them (as a part of creating config files)
- Finally figure out how to analyze logs using `perceval supybod` command.


# groups.io

You neeed to:

- Go to [Hyperledger groups.io](https://lists.hyperledger.org/g/main) or [Zephyr groups.io](https://lists.zephyrproject.org/g/main) or any other groups.io page.
- Create account, remember `<email>` and `<password>`.
- Log in to that account, subscribe to `hyperledger` or `zephyrproject` or any other groups.io page.
- Created token directory: `mkdir /etc/groupsio`.
- Run attached `groupsio.sh` script to get groups.io data for the project: `./groupsio.sh projectname`. `projectname` can be `hyperledger` or `zephyrproject` or any other groups.io page.
- Go to all given groups.io pages and subscribe you `<email>` account to all of them.
- It will ask for email and password, use `<email>` and `<password>` you have used to register to groups.io. It will generate `/etc/groupsio/token` file.
- Subsequent runs will use that file and will not ask for `email/password` pair, it will use saved token.
- You can always run `./groupsio_subscriptions.py < /etc/groupsio/token` to get a list of subscriptions for your groups.io account.

Caveats:

- The final approach should have all this data stored in GrimoireLab config (whatever it is) - probably in Kubernetes secrets.


# Docker

To get `dockerhub` data for the Hyperledger project run: `./hyperledger_dockerhub.sh`.


# Jenkins

To get data for Hyperledger jenkins do [TODO].

To get Jenkins data run: `./jenkins.sh`.


# Meetups

To get data from meetups:

- Register in meetup, for example go [here](https://www.meetup.com/pro/hyperledger) and sing up.
- Create an OAuth token [TODO](https://www.meetup.com/meetup_api/auth/#oauth2).
- For now we can try accessing without token but this will hit raate limits, I've requested more informatiuons [here](https://github.com/chaoss/grimoirelab-perceval/issues/541).

Caveats:
- New meetup users cannot generate API tokens anymore, they're deprecated.
- If you have an old meetup account you can still use old API key, just put it in `/etc/meetup/token` file.


# Bugzilla

Yocto project uses bugzilla 4.4.X. there are two perceval backends for Bugzilla: `bugzilla` (old one) and `bugzillarest` using a lot faster RES API, but it requires Bugzilla 5+. So we can only use `bugzilla` for the Yocto project.

You need to provide `/etc/bugzilla/login` and `/etc/bugzilla/pwd` files (user and password) for bugzilla backed. Go to [Youct Bugzilla](https://bugzilla.yoctoproject.org) and create an account there.

Run: `./bugzilla.sh` to get data.


# Git

Run `./git.sh` script to get git data, note that this script doesn't have all possible repos listed - this is just an example.


# Rocket.Chat

There is no Rocket.Chat support in Perceval, if we need this, we have to implement this and upstream, see [here](https://github.com/chaoss/grimoirelab-perceval/issues/543).


# Other

Other historical scripts are in `perceval` and `elk` folders, more perceval documentation is [here](https://buildmedia.readthedocs.org/media/pdf/perceval/latest/perceval.pdf).


# Devstats

New DevStats Hyperledger page is [here](http://a2bbd9e20925911e99f1b066ec8f6d81-384019263.us-west-2.elb.amazonaws.com:3000), please not that this is a bare Grafana without SSL, meant to be embedded in some LFDA panel in the future.
