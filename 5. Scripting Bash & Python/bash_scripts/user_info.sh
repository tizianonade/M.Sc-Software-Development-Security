#!/bin/bash

# *** Information of Script ***
# Goal : Get information from new users created
# Tasks:
#   Task 1: Get information from /etc/passwd
#   Task 2: Create a file

#Main function

#Create a directory containing user information when they are creation
mkdir -p /home/tub/users_created

#Get information last user
username=$(cat /etc/passwd | awk -F ":" 'END{print $1}')
uuid=$(cat /etc/passwd | awk -F ":" 'END{print $3}')
guid=$(cat /etc/passwd | awk -F ":" 'END{print $4}')

#Creation of the filename
eof="_info.txt"
filename=$username$eof
pathname="/home/tub/users_created/"$filename

#If the file doesn't exist
if [  ! -e $pathname ] 
then
    touch $pathname
    echo " *** User information ***" > $pathname 
    echo "Username: $username" >> $pathname
    echo "Uuid: $uuid" >> $pathname
    echo "Guid: $guid" >> $pathname
else
    echo  "File already exist"
    exit 1
fi

exit 0
