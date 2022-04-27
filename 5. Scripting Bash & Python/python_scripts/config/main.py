#!/bin/python3.8

""" Script Python that sets up a configuration of a machine
# Tasks:
    1. Change hostname
    2. Check the presence of a network interface
    3. Deactivate a network card
    4. Modify the address of a network card
    5. Activate a network interface and the network service (if necessary)
    6. Modify the DNS address
    7. Test network configuration 
"""

"""Check tests at every steps & error messages will be printed out if problems accour

    Arguments received:
        $1: Hostname
        $2: Id of the network card to configure
        $3: Address of the network card with netmask
        $4: Address of the gateway
        $5: Address of DNS
"""

import sys
import re
from functions import *

arguments = sys.argv
NB_ARGUMENTS = 2

if (len(arguments) - 1) == NB_ARGUMENTS:

    #Task 1:
    if arguments[1] and re.match("\w{1,10}",arguments[1]):
        change_hostname(arguments[1])
    else:
        print("Error: first argument - string required (a-zA-Z0-9_) from 1 to 10 characters")
        exit(1)

    #Task 2:
    if arguments[2] and re.match("[a-z]{1,10}", arguments[2]):
        check_interface(arguments[2])
    else:
        print("Error: second argument - string required (a-z) from 1 to 10 characters")
        exit(1)

    #Task 3:

    #Task 4:

    #Task 5:

    #Task 6:

    #Task 7:

else:
    print("{} max arguments required".format(NB_ARGUMENTS))
    exit(1)
        
exit(0)