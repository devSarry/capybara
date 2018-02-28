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
	

## Note: 	
If you would like to import a folder to PiBakery, you can drap and drop. 
	
	If drap and drop is not working, you should (Ctrl Shift +) to add that folder (It's a fault of PiBakery)
	
	
