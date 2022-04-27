import subprocess, re

"""Popen class:
    Executes within a shell:
        shell=True
    
    Example of use (Check return):
    p = subprocess.Popen(cmd, shell=True)
    p.wait()

    if p.returncode == 0 
        success
    else
        failure

    Example of use (Output):
    control output/Error:
        -> stdout=subprocess.PIPE -> output to stdout
        -> stderr=subprocess.PIPE -> output to stderr
        -> stdout=subprocess.DEVNULL -> No output

    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print("Output: {}".format(out))
    print("Error: {}".format(err))

    Pretty output:
        universal_newlines=True

    Run class: 

    try:
        p = subprocess.run("cmd", shell=True check=True)
    except subprocess.CalledProcessError as err:
        print("Error: {}". format(err))
        exit(1)
"""

# Task1: Change hostname
def change_hostname(newName):
    try:
        p = subprocess.run("hostnamectl set-hostname " + newName, shell=True, check=True)
    except subprocess.CalledProcessError as err:
        print("Error: {}". format(err))
        exit(1)

# Task 2: Check the presence of a network interface
def check_interface(interfaceName):

    SUCCESS = 0

    # Get the total number of interfaces (lo included)
    p_iplink = subprocess.run("ip link show | awk '{print $2'}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
    if p_iplink.returncode == SUCCESS:
        print(p_iplink.stdout)
        
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
            result = 1
        else:
            print("Interface doesn't exist")
            result = 0

    else:
        print("Error: Command ip link not successful")
        print("...")
        print(p_iplink.stderr)
        exit(1)
    
    return result