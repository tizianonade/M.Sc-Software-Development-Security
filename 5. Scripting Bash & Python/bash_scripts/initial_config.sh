#!/bin/bash

# Task to redefine basic configuration of the machine

hostnamectl set-hostname urca

sudo ip link set enp0s3 up

exit 0