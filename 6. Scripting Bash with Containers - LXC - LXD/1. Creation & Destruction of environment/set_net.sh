#!/bin/bash

# Bash script that create a network bridge for containers

# Tasks:
#   1. create bridge

lxc network create br0 \
    ipv6.nat=false \
    ipv4.nat=false \
    ipv6.address=none \
    ipv4.address=192.168.10.1/24

