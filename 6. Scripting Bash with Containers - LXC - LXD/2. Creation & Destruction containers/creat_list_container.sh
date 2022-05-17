#!/bin/bash

# Bash script that create a list of LXC containers

sudo bash creat_container.sh \
    ubuntu \
    192.168.10.11 \
    128 \
    1 \
    pass \
    c1

sudo bash creat_container.sh \
    debian \
    192.168.10.12 \
    128 \
    1 \
    pass \
    c2

sudo bash creat_container.sh \
    ubuntu \
    192.168.10.13 \
    128 \
    1 \
    pass \
    c3
