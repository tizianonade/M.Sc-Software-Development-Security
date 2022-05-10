#!/bin/bash

# Bash script that sets up execution environment of LXC containers
# It installs all packages required to use LXC containers & bridges

# Previous taks:
#   1. update
#   -- LXC -- NOT USEFUL 
#   2. install lxc & lxctl lxc templates
#   3. install additional packages and first container
#   4. remove first container
#   -- LXD -- 
#   5. install lxd 
#   6. configure lxd with default options
#   7. download template ubuntu & create first container
#   8. remove first container
#   -- Bridge utils --
#   9. install bridge utils 

# Check tests at every steps & error messages will be printed out if problems accour

#Task 1:
apt update

#Task 2:
# apt-get -y install lxc lxctl lxc-templates

# #Task 3:
# lxc-create -n ctn01 -t ubuntu

# #Task 4:
# lxc-destroy -n ctn01

#Task 5: 
apt-get -y install lxd

#Task 6:
lxd init --minimal

# #Task 7:
# lxc init ubuntu:20.04 ctn01

# #Task 8:
# lxc delete ctn01

#Task 9: 
apt-get -y install bridge-utils