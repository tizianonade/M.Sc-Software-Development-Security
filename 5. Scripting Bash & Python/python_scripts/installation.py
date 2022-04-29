#!/bin/python3.8

"""*** Information Script ***
Goal: Extract an archive and install the package
Task:
1. Extract 
2. Check rights
3. Install 

Arguments:
1: name of the archive
2: Directory where the file must be installed"""

# Scenario:
# Download archive
# chmod u+x alpine.tgz
# tar -xvzf archive.tgz 
# cd archive folder

import sys, subprocess
arguments = sys.argv


NB_ARGUMENTS = 2
SUCCESS = 0

ACCESS_GRANTED = (7,5,3,1) # -> always executable
# r:4 - w:2 - x:1
# 7 : rwx
# 5 : r-x
# 3 : -wx
# 1 : --x

# Check number of arguments
if (len(arguments) - 1) == NB_ARGUMENTS:

    # Get user permission
    p_permission = subprocess.run("stat -L -c \"%a\" {} | awk '{{print substr($1,1,1)}}'".format(arguments[1]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    if p_permission.returncode == SUCCESS:
        
        # Check rights
        rights = int(p_permission.stdout)
        print("Right: " + str(rights))
        if rights in ACCESS_GRANTED:
            
            # Get format of the archive 
            p_getFormat = subprocess.run("echo {} | awk -F \".\" 'END{{print $2}}'".format(arguments[1]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            if p_getFormat.returncode == SUCCESS:
                format = str(p_getFormat.stdout)

                # Extract - ZIP
                if format == "zip":
                    p_unzip = subprocess.run("unzip {}".format(arguments[1]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                    if p_unzip.returncode == SUCCESS:
                        print("Unzip file succeded")
                    else:
                        print("Error: unzip file failed")
                        exit(1)

                # Extract - TAR
                elif format == "tar":
                    p_untar = subprocess.run("tar -xf {}".format(arguments[1]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                    if p_untar.returncode == SUCCESS:
                        print("Untar file succeded")
                    else:
                        print("Error: untar file failed")
                        exit(1)
                
                # Extract - TGZ
                elif format == "tgz":
                    p_untgz = subprocess.run("tar -xvzf {}".format(arguments[1]), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                    if p_untgz.returncode == SUCCESS:
                        print("Untgz file succeded")
                    else:
                        print("Error: untgz file failed")
                        exit(1)
                
                else:
                    print("Error: Unknown format - excepted: zip, tar, tgz")
                    exit(1)

                # Change folder ######################################################################################################
                p_cd = subprocess.run("cd foldername/", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                if p_cd.returncode == SUCCESS:
                    
                    # Make configuration
                    p_configure = subprocess.run("./configure", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                    if p_configure.returncode == SUCCESS:
                        
                        # make
                        p_make = subprocess.run("make", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                        if p_make.returncode == SUCCESS:
                            
                            # Install
                            p_make = subprocess.run("make install", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                            if p_make.returncode == SUCCESS:
                                print("Installation succeded")
                            else:
                                print("Error: install failed")
                                exit(1)

                        else:
                            print("Error: make failed")
                            exit(1)
                    
                    else:
                        print("Error: Cannot configure")
                        exit(1)

                else:
                    print("Error: cannot change directory")
                    exit(1)
                #######################################################################################################################  
            else:
                print("Error: Cannot get format of the file")
                exit(1)
        else:
            print("Error: access refused")
            exit(1)
    else:
        print("Error: Get permission of the file failed")
        exit(1)
else:
    print("Error: {} arguments required".format(NB_ARGUMENTS))
    exit(1)

exit(0)