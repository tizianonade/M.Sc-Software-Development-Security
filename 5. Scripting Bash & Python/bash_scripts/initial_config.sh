#!/bin/bash

# Task to redefine basic configuration of the machine

hostnamectl set-hostname urca

sudo ip link set enp0s3 up

sed -i "s/nameserver .*/nameserver 127.0.0.0:53/" /etc/resolv.conf

exit 0