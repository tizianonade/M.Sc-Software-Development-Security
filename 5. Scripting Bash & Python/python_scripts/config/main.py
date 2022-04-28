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
from task1 import change_hostname
from task2 import check_interface
from task3 import deactivate_interface
from task4 import change_network_information
from task5 import activate_interface


arguments = sys.argv
NB_ARGUMENTS = 4

if (len(arguments) - 1) == NB_ARGUMENTS:
    
    interfaceExist = False

    #Task 1:
    if arguments[1] and re.match("\w{1,10}",arguments[1]):
        change_hostname(arguments[1])
    else:
        print("Error: first argument - string required (a-zA-Z0-9_) from 1 to 10 characters")
        exit(1)

    # #Task 2:
    if arguments[2] and re.match("[a-z]{1,10}", arguments[2]):
        interfaceExist = check_interface(arguments[2])
    else:
        print("Error: second argument - string required (a-z) from 1 to 10 characters")
        exit(1)

    #Task 3:
    # if arguments[2] and re.match("[a-z]{1,10}", arguments[2]):
    #     deactivate_interface(interfaceExist, arguments[2])
    # else:
    #     print("Error: second argument - string required (a-z) from 1 to 10 characters")
    #     exit(1)

    #Task 4:
    # if interfaceExist:
    #     if arguments[3] and re.match("^[0-9]{2,3}(.[0-9]{1,3}){3}\/[0-9]{2}$", arguments[3]): #IPv4 address + net mask (10.0.2.17/24)
    #         change_network_information(arguments[2], arguments[3])
    #     else:
    #         print("Error: third argument - IPv4 address + netmask excepted (x.x.x.x/net)")
    #         exit(1)
    # else:
    #     print("Error: Interface doesn't exist")
    #     exit(1)

    #Task 5:
    if arguments[2] and re.match("[a-z]{1,10}", arguments[2]):
        activate_interface(arguments[2])
    else:
        print("Error: first argument - string required (a-zA-Z0-9_) from 1 to 10 characters")
        exit(1)

    #Task 6:

    #Task 7:

else:
    print("{} max arguments required".format(NB_ARGUMENTS))
    exit(1)
        
exit(0)