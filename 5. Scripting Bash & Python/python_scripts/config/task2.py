import subprocess, re

# Task 2: Check the presence of a network interface
def check_interface(interfaceName):

    SUCCESS = 0

    # Get the total number of interfaces (lo included)
    p_iplink = subprocess.run("ip link show | awk '{print $2'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
    if p_iplink.returncode == SUCCESS:
       
        # print(p_iplink.stdout) - Output:
        #   lo:
        #   00:00:00:00:00:00
        #   enp0s3:
        #   08:00:27:5c:68:7b
        #   enp0s8:
        #   08:00:27:0c:f3:27

        # Select only all name of interfaces within a list
        ipLinkOutputRaw = str(p_iplink.stdout)
        interfacesPresent = re.findall(r"(^[a-z]{,2}|enp0s[0-9])",ipLinkOutputRaw)

        if interfaceName in interfacesPresent:
            print("Interface exist")
            result = True
        else:
            print("Interface doesn't exist")
            result = False

    else:
        print("Error: Command ip link not successful")
        print("...")
        print(p_iplink.stderr)
        exit(1)
    
    return result