import subprocess, re

def change_network_information(interfaceName,ipAddressNetMask):
    SUCCESS = 0
    numberBakUpfile = 0
    newNetworkSettings = ""

    # Get number of yaml.bak.number file within netplan folder:
    p_nbBak = subprocess.run("find /etc/netplan/ -type f -name '*.yaml.bak.*' | sed 's|.*\.||' | wc -l", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_nbBak.returncode == SUCCESS:
        numberBakUpfile = int(p_nbBak.stdout)
    else:
        print("Error: Something wrong when searching the number of back up files")
        exit(1)
    
    # Copy current yaml file 
    p_cpyYamlFile = subprocess.run("sudo cp /etc/netplan/00-installer-config.yaml /etc/netplan/00-installer-config.yaml.bak.{}".format(numberBakUpfile + 1), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_cpyYamlFile.returncode == SUCCESS:
        print("Copy older yaml file: successful")
    else:
        print("Error: Copy older yaml file: not successful")
        exit(1)

    # Get content of current yaml file
    p_catYaml = subprocess.run("cat /etc/netplan/00-installer-config.yaml", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_catYaml.returncode == SUCCESS:
        dataRaw = p_catYaml.stdout
        
        # Print out dataRaw: 
        #    # This is the network config written by 'subiquity'
        #    network:
        #    ethernets:
        #        enp0s3:
        #        dhcp4: true
        #        enp0s8:
        #        dhcp4: false
        #        addresses: [192.168.56.106/24]
        #    version: 2
    else:
        print("Error: Get current yaml file information")
        exit(1)
    
    # Remove first sentence
    dataRaw = dataRaw.split("'subiquity'", 1)[-1]
    
    # Split into a list base on the "\n" character
    listNet = dataRaw.split("\n",100)

    #Check index of the interface - 4 spaces before first character & ":"
    i = listNet.index("    {}:".format(interfaceName))    

    #Check dhcp configuration of the interface
    if listNet[i+1] == ("      dhcp4: true"):
        # DHCP == true -> false
        listNet[i+1] = "      dhcp4: false"
    else:
        # Delete old address
        del listNet[i+2]
    
    # Add new address + mask
    listNet.insert(i+2, "      addresses: [{}]".format(ipAddressNetMask))
    
    # Add \n character at the end of each elements
    i=0
    while i < len(listNet):
        listNet[i] = str(listNet[i]) + "\n" 
        i+=1

    # Remove all only \n character
    listNet = list(filter(("\n").__ne__, listNet))

    # List into string
    for elmt in listNet:
        newNetworkSettings += elmt

    # Delete current yaml file
    p_delYaml = subprocess.run("sudo rm /etc/netplan/00-installer-config.yaml", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_delYaml.returncode == SUCCESS:
        print("Old yaml file deleted")
    else:
        print("Error: Delete current yaml file")
        exit(1)

    # Add new yaml file with new settings
    p_addNewYaml = subprocess.run("sudo bash -c \"echo '{}' > /etc/netplan/00-installer-config.yaml\"".format(newNetworkSettings), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_addNewYaml.returncode == SUCCESS:
        print("New network setting written into the yaml file")
        print("\nOverview:\n...\n")
        print(newNetworkSettings)
        print("...\n")
    else:
        print("Error: New network not written into the yaml file")
        exit(1)
    
    # Apply netplan 
    p_netplanApply = subprocess.run("sudo netplan apply", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_netplanApply.returncode == SUCCESS:
        print("Network settings applied")
    else:
        print("Error: New settings no applied")
        exit(1)