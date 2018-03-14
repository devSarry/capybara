# Building Energy project

Files for configuring RPI - for building energy project
12/2017
	
## AddGitrepo	
This script would be run on first boot state or every time RPI is rebooted. 
This script would send the ip address of RPI to the specific Git repo and installing essential packages.

## Working:
	- addGitrepo shall create new folder name "Clone" in home directory
	- addGitrepo shall clone the specific Git repo - which you provide the link, git's repository, git's user.name and user.password to clone that Git repo.
	- addGitrepo shall install python3 package
	- addGitrepo shall install python3-pip package
	- addGitrepo shall use pip to install w1thermsensor lib

## Using addGitrepo
	- Importing addGitrepo to Pibakery
	- Enter the nessesary information for block or importing .xml file 
	- Can be used for firstboot or everytime RPI is rebooted
	- After everytime RPI is rebooted, this block shall get the IP address and push to the git repository.

## Required
	- It must be connected Internet by using Ethernet cable on the first time. (It might be failed if not)
	- It should connect to the internet while running to setting up essentail packages and linking to Github
	
## ***Enable GPIO pins to read 1-wire sensors***
* There are different ways to enable GPIO pins read 1-wire sensors

* Using addGitrepo.py script
* * By default, addGitrepo.py only enable 1 pins (GPIO 4) to read 1-wire sensors because it will ***cost many CPU resourses of RPI if you do not already have sensors on PINs*** which you have enabled.
* * If you would like to enable all of GPIO pins for reading 1-wire sensors, then you need to uncomment lines 22 -> 31 and commnent out lines 33 -> 38
For example:
```
line 22: GPIO_list = ['2', '3', '4', '5', '6', '7', '8', '9'...
line ...
```

* Editting /boot/config.txt file in RPI
* * If you forgot to edit addGitrepo.py before first boot or you would like to enable more some GPIO pins to read 1-wire, then you can add pin's number by following syntax:
```
(Open /boot/config.txt)
(Go to the bottom of file)

(Adding lines like this) 

dtoverlay=w1-gpio,gpiopin=GPIO_PIN_NUMBER
```  

* Using ***dtoverlay*** command
* * In the RPI terminal (or through SSH), you just need to enter the command like this:
```
sudo dtoverlay w1-gpio gpiopin=GPIO_PIN_NUMBER
```

* Command to checking CPU and Memory resource: `top`

## Note: 	
* If you would like to import a folder to PiBakery, you can drap and drop. 
	
	If drap and drop is not working, you should (Ctrl Shift +) to add that folder (It's a fault of PiBakery)

* ***Problem while connecting with RPI through SSH protocol***
* * ***Only can connect to RPI through Ethernet cable***, you can see the dicussion [here](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=81021)
* * After using `sudo tcpdump -i eth0 icmp` and `ping ip_address` (to analyse the connection), if you see that the connection of RPI always have to go through eth0 (Ethernet cable). Then you can try:
```
Alternatively you could manually change your routing table using the ip command

ip route

will show your current routes

eg. 
default via 192.168.0.1 dev eth0 
192.168.0.0/24 dev eth0 proto kernel scope link src 192.168.0.144


I'm not sure if it will create an entry for wlan0 if it already has one to 192.168.0.0.
Assuming not then you will need to remove the current and add a new one to point at the wireless lan

ip route del 192.168.0.0/24 dev eth0
ip route add 192.168.0.0/24 dev wlan0

Then do the same for the default route

ip route del default dev eth0
ip route add default via 192.168.0.1 dev wlan0

If that works then you can define the routes in the interfaces file so that they only come up when that link is active.

(user: penguintutor via www.raspberrypi.org)
``` 

* * My example:
```
#Set a default network (all package will go through wlan0 directly)
up ip route add 192.168.0.0/24 dev wlan0
down ip route del 192.168.0.0/24 dev eth0

#Set a default gateway
up ip route add default via 192.168.0.1 dev wlan0
down ip route del default dev eth0
```

