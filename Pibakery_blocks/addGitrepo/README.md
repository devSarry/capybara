# Building Energy project

Files for configuring for RPI - for building energy project
12/2017
	
## AddGitrepo	
This script will run in the first boot state. Sending the ip address of RPI to the specific Git repo and installing essential packages.

## Working:
	- addGitrepo shall create new folder name "Clone" in home directory
	- addGitrepo shall clone the specific Git repo - which you provide the link, git's folder, git's user.name and user.password to clone that Git repo.
	- addGitrepo read the ipaddress and push back to Git repo - to be able to check the ip address of RPI without monitor/keyboard - to be able to connect SSH after that.
	- addGitrepo shall install python3 package
	- addGitrepo shall install python3-pip package
	- addGitrepo shall use pip to install w1thermsensor lib

## Using addGitrepo
	- Enter the nessesary information for block 
	- Can be used for firstboot or everyboot
	- After everyboot, this block shall get the IP address and push to the git repository.

## Required
	- It must connect to the internet while running to setting up essentail packages and linking to Github
	- It should be connected Internet by using cable. (It might be failed if not)

## Note: 	
If you would like to import a folder to PiBakery, you can drap and drop. 
	
	If drap and drop is not working, you should (Ctrl Shift +) to add that folder (It's a fault of PiBakery)
	
	
