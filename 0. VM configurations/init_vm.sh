#/bin/bash

netplan_file_exists(){
	
	existing_file=$(ls /etc/netplan) 
	
	if [ ! -n $existing_file ]
	then 
		echo "Existing Netplan file not found"
		exit 1
	fi
}

make_backup(){
	
	existing_file=$(ls /etc/netplan) 
	cp "/etc/netplan/$existing_file" "/etc/netplan/$existing_file.bak"
}

update_netplan_file(){	
	searched_file=$(ls /etc/netplan | grep -v ".yaml.bak") 
	existing_file=$(echo "$searched_file" | tr -d '\n')
	echo -e "# This is the network config written by 'subiquity'" > "/etc/netplan/$existing_file"
	echo -e "network:" >> "/etc/netplan/$existing_file"
	echo -e "  ethernets:" >> "/etc/netplan/$existing_file"
        echo -e "    enp0s3:" >> "/etc/netplan/$existing_file"
	echo -e "      dhcp4: true" >> "/etc/netplan/$existing_file"
	echo -e "    enp0s8:" >> "/etc/netplan/$existing_file"
	echo -e "      dhcp4: false" >> "/etc/netplan/$existing_file"
	echo -e "      addresses: [$1]" >> "/etc/netplan/$existing_file"
	echo -e "  version: 2" >> "/etc/netplan/$existing_file"	
}

if [ $# -eq 1 ]
then
	echo "Apply the address $1 to the second nic"
	sleep 3
	echo "Update..."
	sleep 3
	apt update
	echo "Upgrade..."
	sleep 3
	apt upgrade -y
	echo "SSH server installing..."
	sleep 3
	apt install openssh-server -y	
else
	echo "1 argument required: xxx.xxx.xxx.xxx/xx"
	exit 1
fi

if [ $? -eq 0 ]
then 
	echo "Packages required installed successfully"
	echo "Searching for netplan configuration file..."
	sleep 3
	netplan_file_exists
else
	echo "An occured while installing packages required"
	exit 1
fi

if [ $? -eq 0 ]
then
	echo "Yaml file found"
	echo "Creating a backup..."
	sleep 3
	make_backup
else
	echo "An error occured while searching for the network yaml configuration file"
	exit 1
fi

if [ $? -eq 0 ]
then 
	echo "Yaml backup create successfully"
	echo "Updating netplan file..."
	sleep 3
	update_netplan_file $1
else
	echo "An error occured while creating the backup file"
	exit 1
fi

if [ $? -eq 0 ]
then
	netplan apply
else
	echo "An error occured while updating the network yaml configuration file"
	exit 1
fi

if [ $? -eq 0 ]
then 
	echo "Network configuration successfull"
	sleep 3	
	ip a 
	sleep 5
	systemctl status sshd
	sleep 5
	poweroff
else
	echo "Network configuration unsuccessfull"
	exit 1
fi

exit 0
