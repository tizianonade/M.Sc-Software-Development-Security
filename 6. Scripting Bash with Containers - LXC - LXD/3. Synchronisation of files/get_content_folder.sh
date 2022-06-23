#!/bin/bash

#Bash script that get the content of a folder

get_content(){
    #$1: location to print
    cmd=$(ls -alh "$PWD" | awk '{print $6}')
    echo $cmd
}


if [[ $# -eq 1 ]]; then
    get_content $1
else
    echo "Error: 1 argument expected - path"
    exit 1
fi

exit 0