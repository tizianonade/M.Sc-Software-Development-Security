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
#   $3: Address of the network card with netmask
#   $4: Address of the gateway
#   $5: Address of DNS

#Function task 1
change_hostname(){
    #$1 new hostname
    hostnamectl set-hostname $1
}

#Function task 2
check_interface_presence(){
    #$1 name of interface

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
    #$1 name of interface

    deactivate=$(ip link set $1 down)
    $deactivate
    echo "Interface $1 is deactivated"
}

modify_address(){
    # Replace string within a file 
    # Source : https://linuxhint.com/replace_string_in_file_bash/
    # sed -e "<line number>s/<search pattern>/<replacement string>/"
    
    #$1 name of interface
    #$2 new address of the interface

    #Initialization
    #i=0
    #yamlFile="/etc/netplan/00-installer-config.yaml"

    # Get netmask
    echo "Interface: $1"
    echo "New address: $2"
    printf "Type the netmask: "
    read netmask

    # *** Part 1: Locate the line of the interface within the yaml file ***
    #catYamlFile=$(cat /etc/netplan/00-installer-config.yaml | awk '{print $1}')
    
    #for elmt in $catYamlFile
    #do
    #    #Print out interfaces name without the last character ":" 
    #    interface=${elmt:0:-1}

    #    if [ "$1" = "$interface" ]
    #    then
    #        line_interface=$i
    #    fi

    #   let i++
    #done

    # *** Part 2: Change dhcp from true to false ***
    #line_dhcp=$line_interface+1
    
    #sed -i "s/      dhcp4: false/      dhcp4: true/" net.yaml

    #echo "      addresses: [10.0.2.17/24]" >> $yamlFile
    #cat $yamlFile
   # sed -n '2{h; d}; 4{p; x;}; p' $yamlFile


    # IP METHOD
    setUpNewIp=$(ip addr add $2/$netmask dev $1)
    #delOldIp=$(ip addr del $OldIp/netmask dev $1)

    $setUpNewIp

}

activate_interface(){
    #$1 name of the interface
    sudo ip link set $1 up
}

modify_dns(){
    #$1 new DNS address

    # OLD : nameserver 127.0.0.0:53
    sed -i "s/nameserver .*/nameserver $1/" /etc/resolv.conf
}

test_net_config(){
    ip a 
    ping -c 4 8.8.8.8
}

# Main function
if [ $# -le 5 ]
then
    #Task 1:
    change_hostname $1
    
    #Task 2:
    check_interface_presence $2

    #Task 3:
    #deactivate_card $2

    #Task 4:
    #modify_address $2 $3 $4

    #Task 5:
    activate_interface $2

    #Task 6: 
    modify_dns $5

    #Task7:
    test_net_config 
    
else
    echo "5 arguments required"
    exit 1
fi

exit 0