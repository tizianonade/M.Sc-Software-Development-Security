#!/bin/bash

# Script that test if the the folder is up to date

#Tasks: 
# 1. Check if both folders exist
# 2. Check if an update is needed if no it means both dates are the same


folder_exist(){
    #$1: 1.source folder
    #$2: 2.test folder

    #Global variable
    value_returned=1

    if [ -d $1 ]; then
        value_returned=0
    else
        echo "Error: Client folder doesn't exist"
        exit 1
    fi 

    if [[ -e $2 ]]; then
        value_returned=0
    else
        echo "Error: Server folder doesn't exist"
        exit 1
    fi 

    return $value_returned
}

check_update_needed(){
    #$1: client folder name
    #$2: server folder name

    client_parent_folder=$(dirname $1)
    echo $client_parent_folder
    # #Get day + time of the client folder
    # list_months_client=$(ls -alh "$PWD/$1/" | awk '{print $6}')
    # list_days_client=$(ls -alh "$PWD/$1/" | awk '{print $7}')
    # list_times_client=$(ls -alh "$PWD/$1/" | awk '{print $8}')

    # c_month=$(echo $list_months_client | awk '{print $1}')
    # c_day=$(echo $list_days_client | awk '{print $1}')
    # c_time=$(echo $list_times_client | awk '{print $1}')
    # c_hour=$(echo $c_time | cut -d : -f1)
    # c_minute=$(echo $c_time | cut -d : -f2)

    # #Get day + time of server folder
    # list_months_server=$(ls -alh "$PWD/$2/" | awk '{print $6}')
    # list_days_server=$(ls -alh "$PWD/$2/" | awk '{print $7}')
    # list_times_server=$(ls -alh "$PWD/$2/" | awk '{print $8}')

    # s_month=$(echo $list_months_server | awk '{print $1}')
    # s_day=$(echo $list_days_server | awk '{print $1}')
    # s_time=$(echo $list_times_server | awk '{print $1}')
    # s_hour=$(echo $s_time | cut -d : -f1)
    # s_minute=$(echo $s_time | cut -d : -f2)

    # #Convertion client folder: from MONTH string to MONTH number
    # if [[ $c_month = "Jan" ]]; then
    #     c_month=1
    # elif [[ $c_month = "Feb" ]]; then
    #     c_month=2
    # elif [[ $c_month = "Mar" ]]; then
    #     c_month=3
    # elif [[ $c_month = "Apr" ]]; then
    #     c_month=4
    # elif [[ $c_month = "May" ]]; then
    #     c_month=5
    # elif [[ $c_month = "Jun" ]]; then
    #     c_month=6
    # elif [[ $c_month = "Jul" ]]; then
    #     c_month=7
    # elif [[ $c_month = "Aug" ]]; then
    #     c_month=8
    # elif [[ $c_month = "Sep" ]]; then
    #     c_month=9
    # elif [[ $c_month = "Oct" ]]; then
    #     c_month=10
    # elif [[ $c_month = "Nov" ]]; then
    #     c_month=11
    # elif [[ $c_month = "Dec" ]]; then
    #     c_month=12
    # else
    #     echo "Invalid month from the source folder"
    #     exit 1
    # fi

    # #Convertion server folder: from MONTH string to MONTH number
    # if [[ $s_month = "Jan" ]]; then
    #     s_month=1
    # elif [[ $s_month = "Feb" ]]; then
    #     c_month=2
    # elif [[ $s_month = "Mar" ]]; then
    #     s_month=3
    # elif [[ $s_month = "Apr" ]]; then
    #     s_month=4
    # elif [[ $s_month = "May" ]]; then
    #     s_month=5
    # elif [[ $s_month = "Jun" ]]; then
    #     s_month=6
    # elif [[ $s_month = "Jul" ]]; then
    #     s_month=7
    # elif [[ $s_month = "Aug" ]]; then
    #     s_month=8
    # elif [[ $s_month = "Sep" ]]; then
    #     s_month=9
    # elif [[ $s_month = "Oct" ]]; then
    #     s_month=10
    # elif [[ $s_month = "Nov" ]]; then
    #     s_month=11
    # elif [[ $s_month = "Dec" ]]; then
    #     s_month=12
    # else
    #     echo "Invalid month from the source folder"
    #     exit 1
    # fi

    # #Test month between client folder & server folder
    # if [[ $c_month -eq $s_month ]]; then
    #     #Test Day
    #     echo "Test days"
    # elif [[ $c_month -lt $s_month ]]; then
    #     echo "The client folder needs to be updated"
    # else
    #     echo "The server folder needs to be updated"
    # fi
}

if [[ $# -eq 2 ]]; then

    #Task 1:
    folder_exist $1 $2
    
    #Task 2:
    if [[ $? -eq 0 ]]; then
        check_update_needed $1 $2
    else
        echo "Some folder types don't exist"
        exit 1
    fi
else
    echo "Error: 2 arguments required:"
    echo "  1.client folder"
    echo "  2.server folder"
    exit 1
fi

exit 0