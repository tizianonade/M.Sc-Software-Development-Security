import subprocess, re

# Task 3: Deactivate interface
def deactivate_interface(interfaceExist, interfaceName):
    SUCCESS = 0

    if interfaceExist:
        p_interfaceDown = subprocess.run("sudo ip link set " + interfaceName + " down", shell=True)
        if p_interfaceDown.returncode == SUCCESS:
            print("Interface {} is down".format(interfaceName))
        else:
            print("Error: interface still up")
            exit(1)
    else:
        print("Error: Interface doesn't exist")
        exit(1)