#!/usr/bin/python

import os
import sys
import os.path
import subprocess
import time


#Make sure that those packages have been installed
#os.system("sudo apt-get install -y update")
#os.system("sudo apt-get install -y upgrade")
os.system("sudo apt-get install -y git")
os.system("sudo apt-get install -y python3")
os.system("sudo apt-get install -y python3-pip")
os.system("pip3 install w1thermsensor")

#Enable all GPIO pins to read 1-wire device - all device's addresses will be stored in /sys/bus/w1
GPIO_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '16', '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27']

if ( "dtoverlay=w1-gpio,gpiopin=2") in open("/boot/config.txt").read():
    print("existing")
else:
    with open("/boot/config.txt", "a") as sudoFile:
        for i in range(len(GPIO_list)):
            appendtext = "dtoverlay=w1-gpio,gpiopin={}\n".format(GPIO_list[i])
            sudoFile.write(appendtext)

#Updating ip_address of RPI.
def updateInfo():
    # Reading the IP address and send them to "ipAddress" file
    os.system("ifconfig > ipAdrress.txt")

    # Adding email to RPI to identify to push Git
    os.system("sudo git config --global user.email"+ " " + sys.argv[3])

    # Adding name to push to Git
    os.system("sudo git config --global user.name" + " " + sys.argv[4])
    os.system("sudo git add .")

    # Add empty commit.
    os.system("""sudo git commit -m "updating the ipaddress" """)

    # Pushing to Git with user.name and user.passwd
    os.system("sudo git push http://" + sys.argv[5] + ":" + sys.argv[6] + "@" + sys.argv[1])
    sys.exit(0)
    return

#Cloning Git repository into the RPI
def Cloning():
    # Clone Git repo to working directory
    os.system("git clone http://" + sys.argv[5] + ":" + sys.argv[6] + "@" + sys.argv[1])
    # Going to Git repo
    os.chdir(sys.argv[2])

    # Checking whether Info dir is not exist
    if not os.path.exists("Info"):
        os.system("mkdir Info")

        # Changing to Info dir for Git repo
        os.chdir("Info")
        updateInfo()
    else:
        # Changing to Info dir for Git repo
        os.chdir("Info")
        updateInfo()
    return

#Calling updateInfor() if you have already cloned Git repository into RPI 
def Updating():
    # Chaing to Git repo
    os.chdir(sys.argv[2])

    # Changing to Info dir for Git repo
    os.chdir("Info")
    updateInfo()

# Checking whether Clone dir is not exist
if not os.path.exists("/home/pi/Clone"):
    os.system("mkdir -p /home/pi/Clone")
    os.chdir("/home/pi/Clone")
    Cloning()
else:
    os.chdir("/home/pi/Clone")
    Updating()
