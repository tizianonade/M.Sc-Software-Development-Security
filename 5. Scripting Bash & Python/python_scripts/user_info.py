#!/bin/python3.8

# *** Information of Script ***
# Goal : Get information from new users created
# Tasks:
#   Task 1: Get information from /etc/passwd
#   Task 2: Create a file

import subprocess

#Main function
SUCCESS = 0

#Create a directory containing user information when they are creation
p_createDir = subprocess.run("mkdir -p /home/tub/users_created'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
if p_createDir.returncode == SUCCESS:

    #Get information last user
    p_getUsername = subprocess.run("cat /etc/passwd | awk -F ":" 'END{print $1}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_getUsername.returncode == SUCCESS:
        username = str(p_getUsername.stdout)
    else:
        print("Error: Unable to get username")
        exit(1)

    p_getUuid = subprocess.run("cat /etc/passwd | awk -F ":" 'END{print $3}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_getUuid.returncode == SUCCESS:
        uuid = str(p_getUuid.stdout)
    else:
        print("Error: Unable to get uuid")
        exit(1)

    p_getGuid = subprocess.run("cat /etc/passwd | awk -F ":" 'END{print $4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_getGuid.returncode == SUCCESS:
        guid = str(p_getGuid.stdout)
    else:
        print("Error: Unable to get Guid")
        exit(1)
    
    #Creation of the filename with path
    pathname = "/home/tub/user_created/{}_info.txt".format(username)

    #Create file 
    p_createFile = subprocess.run("echo \"*** User information ***\n{}\n{}\n{}\" > pathname".format(username, uuid, guid), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_createFile.returncode == SUCCESS:
        print("Success: File created")
    else:
        print("Error: unable to create the file")
        exit(1)

else:
    print("Error: unable to create a directory")
    exit(1)

exit(0)