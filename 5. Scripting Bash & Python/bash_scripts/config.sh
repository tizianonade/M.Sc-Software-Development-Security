#!/bin/bash

# Script bash that sets up a configuration of a machine
# Tasks:
#   1. Change hostname
#   2. Check the presence of a network interface
#   3. Deactivate a network card
#   4. Modify the address of a network card
#   5. Activate a network interface and the network service (if necessary)
#   6. Modify the DNS address
#   7. Test network configuration

# Check tests at every steps & error messages will be printed out if problems accour

# Arguments received:
#   $1: Hostname
#   $2: Id of the network card to configure
#   $3: Address of the network card 
#   $4: Address of the gateway
#   $5: Address of DNS

#Function task 1
change_hostname(){
    hostnamectl set-hostname $1
}

#Function task 2
check_interface_presence(){

    #Initialization
    interface_presence=0
    i=0

    # Get the total number of interfaces (lo included)
    ipLink=$(ip link show | awk '{print $2}')

    # Get interfaces names
    for elmt in $ipLink
    do
        # 6 lignes in total & all interfaces names are located on a pair ligne
        if [ $[$[($i)%2]] -eq 0 ]
        then    
            #Print out interfaces name without the last character ":" 
            interface=${elmt:0:-1}

            #Check presence of the interface
            if [ "$1" = "$interface" ]
            then
                interface_presence=1
            fi
        fi
        let i++
    done  

    if [ $interface_presence -eq 1 ]
    then
        echo "$1 is present"
    else
        echo "$1 is not present"
    fi
}

deactivate_card(){
    deactivate=$(ip link set $1 down)
    $deactivate
    echo "Interface $1 is deactivated"
}

# Main
if [ $# -eq 2 ]
then
    #Task 1:
    change_hostname $1
    
    #Task 2:
    check_interface_presence $2

    #Task 3:
    deactivate_card $2
    
else
    echo "5 arguments required"
    exit 1
fi

exit 0