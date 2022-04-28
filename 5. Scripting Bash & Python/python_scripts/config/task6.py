import subprocess, re

def modify_dns(dnsAddress):
    SUCCESS = 0
    # OLD : nameserver 127.0.0.53

    p_modifyDNS = subprocess.run("sudo sed -i \"s/nameserver .*/nameserver {}/\" /etc/resolv.conf".format(dnsAddress), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_modifyDNS.returncode == SUCCESS:
        print("New DNS server: {}".format(dnsAddress))
    else:
        print("Error: DNS server still is")
