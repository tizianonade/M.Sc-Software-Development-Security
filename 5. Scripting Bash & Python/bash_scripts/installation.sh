#!/bin/bash

# *** Information Script ***
# Goal: Extract an archive and install the package
# Task:
# 1. Extract 
# 2. Check rights
# 3. Install 

# Arguments:
# $1: name of the archive
# $2: Directory where the file must be installed

# Main function
if [ $# -eq 2 ]
then 
    #Check permision of the file
    userPermission=$(stat -L -c "%a" hello.txt | awk '{print substr($1,1,1)}')
    if [ "$userPermission" = "7" or "$userPermission" = "5" or  "$userPermission" = "3" or "$userPermission" = "1" ]
    then
        #Extract
        format=$(echo $1 |awk -F "." 'END{print $2}')
        if [ "$format" = "zip" ]
        then
            unzip $1
        elif [ "$format" = "tar" ] 
        then
            tar -xf $1
        elif [ "$format" = "tgz" ]
        then 
            tar -tzf $1
        else
            echo "Error"
        fi

        #Get filename
        filename=format=$(echo $1 |awk -F "." 'END{print $1}')
        
        #Installation
        chmod u+x $filename/configure
        bash $filename/configure    
        bash $filename/make
        bash $filename/make install

    else
        echo "Permission denied"
        exit 1
    fi
else   
    echo "2 arguments required"
    exit 1
fi 