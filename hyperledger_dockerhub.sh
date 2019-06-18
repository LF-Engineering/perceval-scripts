#!/bin/bash
perceval dockerhub hyperledger burrow || exit 1
perceval dockerhub hyperledger cello-baseimage || exit 2
perceval dockerhub hyperledger cello-engine || exit 3
perceval dockerhub hyperledger cello-mongo || exit 4
perceval dockerhub hyperledger cello-operator-dashboard || exit 5
perceval dockerhub hyperledger composer-cli || exit 6
perceval dockerhub hyperledger composer-playground || exit 7
perceval dockerhub hyperledger composer-rest-server || exit 8
perceval dockerhub hyperledger explorer || exit 9
perceval dockerhub hyperledger fabric-ca || exit 10
perceval dockerhub hyperledger fabric-ccenv || exit 11
perceval dockerhub hyperledger fabric-couchdb || exit 12
perceval dockerhub hyperledger fabric-kafka || exit 13
perceval dockerhub hyperledger fabric-orderer || exit 14
perceval dockerhub hyperledger fabric-peer || exit 15
perceval dockerhub hyperledger fabric-tools || exit 16
perceval dockerhub hyperledger fabric-zookeeper || exit 17
perceval dockerhub hyperledger indy-core-baseci || exit 18
perceval dockerhub hyperledger iroha || exit 19
perceval dockerhub hyperledger sawtooth-rest-api || exit 20
perceval dockerhub hyperledger sawtooth-settings-tp || exit 21
perceval dockerhub hyperledger sawtooth-shell || exit 22
perceval dockerhub hyperledger sawtooth-validator || exit 23
echo 'OK'
