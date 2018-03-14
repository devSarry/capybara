#!/usr/bin/python

import os
import sys
import os.path
import subprocess
import time


#This script shall used for updating ip_address of RPI and sending to Git repository.
#This script shall enable GPIO pins to read 1-wire sensors by using dtoverlay...
#Cause RPI will cost too many CPU resources to find sensors on GPIO pins if there is not any sensors on those PINs,
#then, the default GPIO pin to read 1-wire sensor cable will be only on GPIO pin 4 (dtvoerlay=w1-gpio,gpiopin=4)
#If you would like to enable to all GPIO pins, you need to uncomment lines 22 -> 31 and commnent out lines 33 -> 38

#On the first boot, it shall install essentail packages (Git, python3,...)
#On the next every boots, it will automatically update ip_address of RPI and push to GIT repository


#Enable all GPIO pins to read 1-wire device - all device's addresses will be stored in /sys/bus/w1
#Uncomment those line to enable all GPIO pins to read 1-wire sensors
#GPIO_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '16', '17', '18', '19', '20', '21', '22', '23', '24','25', '26', '27']

#if ( "dtoverlay=w1-gpio,gpiopin=2") in open("/boot/config.txt").read():
#    print("existing")
#else:
#    with open("/boot/config.txt", "a") as sudoFile:
#        for i in range(len(GPIO_list)):
#            appendtext = "dtoverlay=w1-gpio,gpiopin={}\n".format(GPIO_list[i])
#            sudoFile.write(appendtext)

#By default, only enable GPIO pin 4 to read 1-wire sensor cable.
#Comment out if you have uncommented those line above
if ( "dtoverlay=w1-gpio,gpiopin=4") in open("/boot/config.txt").read():
    print("existing")
else:
    with open("/boot/config.txt", "a") as sudoFile:
        appendtext = "dtoverlay=w1-gpio,gpiopin=4\n"
        sudoFile.write(appendtext)


#Updating ip_address of RPI.
def updateInfo():
    # Updating git repository
    os.system("git pull")

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
    os.system("sudo git push https://" + sys.argv[5] + ":" + sys.argv[6] + "@" + sys.argv[1])
    sys.exit(0)
    return

#Cloning Git repository into the RPI - creating new directory to store repository
#This should be run only on first boot.
#On the first boot, this function will install essential packages also
def Cloning():
    #Install essential packages
    os.system("sudo apt-get install -y git")
    os.system("sudo apt-get install -y python3")
    os.system("sudo apt-get install -y python3-pip")
    os.system("pip3 install w1thermsensor")

    # Clone Git repo to working directory
    os.system("git clone https://" + sys.argv[5] + ":" + sys.argv[6] + "@" + sys.argv[1])
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
