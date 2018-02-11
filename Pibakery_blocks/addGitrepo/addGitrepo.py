#!/usr/bin/python

import os
import sys
import os.path
import subprocess
import time

#Enable all GPIO pins to read 1-wire device - all device's addresses will be stored in /sys/bus/w1
if ( "dtoverlay=w1-gpio,gpiopin=2") in open("/boot/config.txt").read():
    print("existing")
else:
    appendtext = """
    dtoverlay=w1-gpio,gpiopin=2
    dtoverlay=w1-gpio,gpiopin=3
    dtoverlay=w1-gpio,gpiopin=4
    dtoverlay=w1-gpio,gpiopin=5
    dtoverlay=w1-gpio,gpiopin=6
    dtoverlay=w1-gpio,gpiopin=7
    dtoverlay=w1-gpio,gpiopin=8
    dtoverlay=w1-gpio,gpiopin=9
    dtoverlay=w1-gpio,gpiopin=10
    dtoverlay=w1-gpio,gpiopin=11
    dtoverlay=w1-gpio,gpiopin=12
    dtoverlay=w1-gpio,gpiopin=13
    dtoverlay=w1-gpio,gpiopin=16
    dtoverlay=w1-gpio,gpiopin=17
    dtoverlay=w1-gpio,gpiopin=18
    dtoverlay=w1-gpio,gpiopin=19
    dtoverlay=w1-gpio,gpiopin=20
    dtoverlay=w1-gpio,gpiopin=21
    dtoverlay=w1-gpio,gpiopin=22
    dtoverlay=w1-gpio,gpiopin=23
    dtoverlay=w1-gpio,gpiopin=24
    dtoverlay=w1-gpio,gpiopin=25
    dtoverlay=w1-gpio,gpiopin=26
    dtoverlay=w1-gpio,gpiopin=27
    """
    with open("/boot/config.txt", "a") as sudoFile:
        sudoFile.write(appendtext)

#os.system("sudo modprobe w1-gpio")
#os.system("sudo modprobe w1-therm")
os.system("sudo apt-get install -y python3")
os.system("sudo apt-get install -y python3-pip")
os.system("pip3 install w1thermsensor")

def updateInfo():
    # Reading the IP address and send them to "ipAddress" file
    os.system("ifconfig > ipAdrress.txt")

    # Adding email to RPI to identify to push Git
    os.system("sudo git config --global user.email"+ " " + sys.argv[3])

    # Adding name to push to Git
    os.system("sudo git config --global user.name" + " " + sys.argv[4])
    os.system("sudo git add .")

    # Add empty commit.
    os.system("""sudo git commit -m "update the ipaddress" """)

    # Pushing to Git with user.name and user.passwd
    os.system("sudo git push --repo http://"+sys.argv[5]+":"+sys.argv[6]+"@github.com/"+sys.argv[5]+"/"+sys.argv[2]+".git")
    sys.exit(0)
    return


def cloning():
    # Clone Git repo to working directory
    subprocess.check_call(["sudo","git", "clone", sys.argv[1]])

    # Chaing to Git repo
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
    cloning()
else:
    os.chdir("/home/pi/Clone")
    Updating()
