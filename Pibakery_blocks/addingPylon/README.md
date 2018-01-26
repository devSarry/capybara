# Building Energy project

Files for configuring the sensor addresses - for building energy project
01/2018

## addingPylon block	
	- Including: 
		- addingPylon.py - run every time after boot to take the input sensor addresses by using Pibakey
		- readingTemp.py - to get sensor address from files and reading temperature from those sensors

## Describe:
### addingpython script:
	- addingpython shall get the Sensor_IDs from setting in Pibakery (sensor addresse from sensor cable)
	- addingpython shall put the sensor's objects to the list 
	- addingpython shall print out the data of each sensor's objects in list
	- addingpython shall export sensor addresses in list to files according to it's Pylon_ID - in Sensor dir

### readingTemp script:
	- readingTemp shall get the sensor addresses in files in Sensor dir 
	- readingTemp shall store as sensor objects in list and reading temperature from sensors
	- readingTemp shall export the reading value to files which named readingData_{}

## Using addingPylon
	- Enter the Pylon_ID (this could be any 1,2...n) 
	- Enter the address of each sensor in order from deepest.
	- To expand for more sensors, need to add more input arguments in json file and redefine number in for loop in addingPylon.py (line 33)

## Using readingTemp
	- Only need to execute file 
	
## Note: 	
If you would like to import a folder to PiBakery, you can drap and drop. 
	
	If drap and drop is not working, you should (Ctrl Shift +) to add that folder (It's a fault of PiBakery)

## Required:
	- addGitrepo block must be run successful (it will install essentail packages)
	- w1thermsensor lib must be install before running this.
	- w1thermsensor lib must be install by using python3-pip
	
