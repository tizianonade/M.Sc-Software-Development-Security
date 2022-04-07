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

if [ $# -eq 1 ]
then
    #Task 1:
    hostnamectl set-hostname $1

    #Task 2:

    #Initialization
    nb_interfaces=0
    i=0

    # Get the total number of interfaces (lo included)
    ipLink=$(ip link show | awk '{print $2}')

    # Get interfaces names
    for elmt in $ipLink
    do
        # 6 lignes in total & all interfaces names are located on a pair ligne
        if [ $[$[($i)%2]] -eq 0 ]
        then    
            #Print out interfaces name without the ":" at the end
            echo ${elmt:0:$[len-1]}
        fi
        let i++
    done 

    #echo $nb_interfaces
    


    #touch hello.txt
    #update=$(ls)

    #for elmt in $update
    #do
    #    echo $elmt >> hello.txt
    #done

else
    echo "5 arguments required"
    exit 1
fi

exit 0