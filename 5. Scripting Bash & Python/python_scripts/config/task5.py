import subprocess

def activate_interface(interfaceName):
    SUCCESS = 0

    p_interfaceUp = subprocess.run("sudo ip link set {} up".format(interfaceName), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_interfaceUp.returncode == SUCCESS:
        print("Interface {} UP!".format(interfaceName))
    else:
        print("Interface {} DOWN!".format(interfaceName))
