#!/bin/bash
perceval git git://git.openembedded.org/meta-openembedded --category commit --git-path .meta-openembedded > .yocto.meta-openembedded.log || exit 1
