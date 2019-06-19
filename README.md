# perceval-scripts
Scripts to get data for various datasources.


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

- register in meetup, for example go [here](https://www.meetup.com/pro/hyperledger) and sing up.
- Create an OAuth token [TODO](https://www.meetup.com/meetup_api/auth/#oauth2).
- For now we can try accessing without token but this will hit raate limits, I've requested more informatiuons [here](https://github.com/chaoss/grimoirelab-perceval/issues/541).


# Other

Other historical scripts are in `perceval` and `elk` folders, more perceval documentation is [here](https://buildmedia.readthedocs.org/media/pdf/perceval/latest/perceval.pdf).


# Devstats

New DevStats Hyperledger page is [here](http://a2bbd9e20925911e99f1b066ec8f6d81-384019263.us-west-2.elb.amazonaws.com), please not that this is a bare Grafana without SSL, meant to be embedded in some LFDA panel in the future.
