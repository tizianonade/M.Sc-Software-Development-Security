#!/bin/bash

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

#Check argument 
if [ $# -eq 4 ]
then 
#Create the archive
    if [ -e $1 ]
    then
        archive=$1.tar.gz
        tar -zcvf $archive $1
        scp $archive $4@$3 $5
    else
        echo "Error while creating the archive - file doesn't exist"
        exit 1
    fi
else
    echo "Error: excepting 4 arguments"
fi