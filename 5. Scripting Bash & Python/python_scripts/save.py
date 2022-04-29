#!/bin/python3.8

# *** Information of Script ***
# Goal : Get information from new users created
# Tasks:
#   Task 1: Get information from /etc/passwd
#   Task 2: Create a file

# Arguments: 
# $1: name of the archive
# $2: name of the directory where the file must be saved
# $3: address of the server where to save the file
# $4: login of the account
# $5: password of the account

#Main function

import sys, subprocess
arguments = sys.argv


NB_ARGUMENTS = 5
SUCCESS = 0

# Check number of arguments
if (len(arguments) - 1) == NB_ARGUMENTS:
    p_compress = subprocess.run("tar -zcvf {}.tar.gz {}".format(arguments[1],arguments[1]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_compress.returncode == SUCCESS:
        
        p_cpy = subprocess.run("scp {}.tar.gz {}@{} {}".format(arguments[1],arguments[4],arguments[3],arguments[5]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        if p_cpy.returncode == SUCCESS:
            print("Copy succeded")
        else:
            print("Error: copy failed")
            exit(1)

    else:
        print("Error: Archive creation failed")
        exit(1)
else:
    print("Error: Excepting {} arguments".format(NB_ARGUMENTS))
    exit(1)

exit(0)