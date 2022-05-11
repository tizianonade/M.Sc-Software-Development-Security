#!/bin/bash

# Bash script that launch containers

# Arguments given:
#   $1: name of container or joker like "ctn*"

# Tasks:
#   1. check argument
#   2. launch container(s) if containers found

launch_cont(){
    #$1: name of container or joker like "ctn*" 
 
    # Check if argument is string name of container or ctn*
    if [[ $1 =~ ^[a-z]+[*]$ ]]; then 
        
        # if argument = "ctn*"
        if [[ $1 =~ ^ctn\*$ ]]; then 
 
            # From ctn* to ctn
            joker=$1
            cont_str=${joker::-1}

            # Get list of containers 
            print_cont=$(lxc list | awk '{print $2}')

            i=0
            j=2
            container=$(echo $print_cont | awk '{print $'"$j"'}')

            while [ "$container" != "" ]
            do
                list_cont[i]=$container 
                let i++
                let j++
                container=$(echo $print_cont | awk '{print $'"$j"'}')  
            done

            #Launch container
            for ctn in ${list_cont[*]}
            do 
                firstThreeCharacters=${ctn::3}

                #if container start with "ctn"
                if [[ $firstThreeCharacters =~ ^"$cont_str"$ ]]; then
                    #launch
                    lxc start $ctn
                fi
            done 
        else
            echo "Error: expected only the joker: \"ctn*\""
            exit 1
        fi           
    elif [[ $1 =~ ^[a-z0-9]+$ ]]; then
        # if argument = nameOfContainer

        # Get list of containers 
        print_cont=$(lxc list | awk '{print $2}')

        i=0
        j=2
        container=$(echo $print_cont | awk '{print $'"$j"'}')

        while [ "$container" != "" ]
        do
            list_cont[i]=$container 
            let i++
            let j++
            container=$(echo $print_cont | awk '{print $'"$j"'}')  
        done

        #Check if container exist
        ctn_exist=0
        for ctn in ${list_cont[*]}
        do
            if [ $ctn = $1 ]; then
                ctn_exist=1
           elif [ $ctn != $1 -a $ctn_exist -eq 1 ]; then
                ctn_exist=1
            else 
                ctn_exist=0
            fi
        done
        
        # Launch if container exist
        if [ $ctn_exist -eq 1 ]; then
            lxc start $1
        else
            echo "Error: Container not found"
            exit 1
        fi

    else
        echo "Error: expected a string with or without numbers or the joker: \"ctn*\""
        exit 1
    fi
}

# Main function
if [ $# -ge 1 ]; then

    for var in $*
    do 
        launch_cont $var
    done

else
    echo "Error: at least 1 argument required"
    exit 1
fi

exit 0