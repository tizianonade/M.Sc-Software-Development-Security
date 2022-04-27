import subprocess

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

