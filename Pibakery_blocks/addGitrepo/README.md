# Building Energy project

Files for configuring for RPI - for building energy project
12/2017
	
## AddGitrepo	
This script will run in the first boot state. Sending the ip address of RPI to the specific Git repo.

The python script file will:
	- Firstly, creating new folder name "Clone" in home directory
	- Secondly, cloning the specific Git repo - which you provide the link, git's folder, git's user.name - user.password to clone that Git repo.
	- Thirdly, reading the ipaddress and push back to Git repo - to be able to check the ip address of RPI without monitor/keyboard - to be able to connect SSH after that.

## Using addGitrepo
	- Enter the nessesary information for block 
	- Still need to install Git package before use. (would be added in the future)
	
### Note: 
	
If you would like to import a folder to PiBakery, you can drap and drop. 
	
	If drap and drop is not working, you should (Ctrl Shift +) to add that folder (It's a fault of PiBakery)
	
	
