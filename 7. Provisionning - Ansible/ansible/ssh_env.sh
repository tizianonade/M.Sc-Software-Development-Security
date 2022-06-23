#!/bin/bash

#$1 = name of container

lxc exec $1 -- apt-get update
lxc exec $1 -- apt-get -y install openssh-server
lxc exec $1 -- systemctl status ssh