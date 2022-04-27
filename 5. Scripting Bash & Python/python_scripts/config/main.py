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
from functions import *
arguments = sys.argv

if (len(arguments) - 1) <= 5:
    #Task 1:
    change_hostname(arguments[1])

    #Task 2:

    #Task 3:

    #Task 4:

    #Task 5:

    #Task 6:

    #Task 7:

else:
    print("5 max arguments required")
    exit(1)
        
exit(0)