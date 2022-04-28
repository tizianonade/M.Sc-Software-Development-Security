import subprocess

def test_net_config():
    SUCCESS = 0

    p_ipLink = subprocess.run("ip a", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_ipLink.returncode == SUCCESS:
        print(p_ipLink.stdout)
    else:
        print(p_ipLink.stderr)

    p_ping = subprocess.run("ping -c 4 8.8.8.8", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_ping.returncode == SUCCESS:
        print(p_ping.stdout)
    else:
        print(p_ping.stderr)
