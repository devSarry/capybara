capybara
========

Building Energy IoT Client

Usage
-----

Installation
------------

### Installation in Windows

* Download and install [Python
  3.5.x](https://www.python.org/ftp/python/3.5.3/python-3.5.3.exe).  For this
  guide, we assume Python is installed in `C:\Python35`.
* Download the Pip (Python package installer) bootstrap script
  [get-pip.py](https://bootstrap.pypa.io/get-pip.py).
* In the command prompt, run `C:\Python35\python.exe get-pip.py` to install
  `pip`.
* In the command prompt, run `C:\Python35\scripts\pip install virtualenv` to
  install `virtualenv`.

```
c:\location_of_project>c:\Python35\scripts\virtualenv --system-site-packages venv
c:\location_of_project>venv\Scripts\activate
```


### Installation in Ubuntu / vagrant Ubuntu

**Note:** Working in Windows using an ubunutu box in vagrant has some pitfalls. The vagrant environment being used is "Homestead" mainly because I am comfortable with it and it provides out of the box a good working environment. 

**Environment Setup**

Follow the guide for setting up homestead on found on the [Laravel Page](https://laravel.com/docs/5.5/homestead) 

Once you have a *Homestead* box up and running we will need to modify the `Homestead.yaml` file a bit. You can find it in the root of the cloned Homestead folders. If you followed the above guide it will be in `C:\Users\UserName\Homestead`. Well add a virtualenvs folder by default and link it to a windows folder called `homesteadvirtualenvs`
```yaml
folders:
    - map: ~/homesteadvirtualenvs
      to: /home/vagrant/.virtualenvs
```

This will allow us to modify our file in a windows environment and have it mapped to the ubunut box.

Next we will need to add a to the provisioning script `after.sh` also found in the Homestead folder
```bash
#python3 virtual environments
sudo pip3 install virtualenvwrapper
```

Finally we need to add an alias, luckily there's an `alias` file where all our environment aliases are stored
```
source /usr/local/bin/virtualenvwrapper.sh
```

**Creating a virtualenv**
This is the Windows specific pit fall because of symlinked folders. You need the `--always-copy` flag.
```
mkvirtualenv --python=/usr/bin/python3 capybara --always-copy
```


```
workon capybara
```

Starting the project
--------------------

After activating the virtualenv do the following

```
sudo pip3 install -r requirements.txt #or sudo pip3 install --upgrade -r requirements.txt
```


Requirements
-------------

Compatibility
-------------

Licence
-------

Authors
-------


Using capybara
--------------------

### Installing python App (capybara) into the system to have absolute path.

* Cloning Capybara repository into RPI
```
git clone https://github.com/dopyoman/capybara
```

* Going to the directory which you have cloned this project (.../capybara/), then:
```
sudo pip3 install -r requirements.txt
```

* Next, you need to go to ~/capybara/app/ copy example.config.yaml to be config.yaml:
```
sudo cp example.config.yaml config.yaml

sudo nano config.yaml
```

* Next, you need to ***erase*** the value of **NAME** in config.yaml if you want to create new Device. Example:
```
NAME: 
PASSWORD: abc...xyz
SECRET_KEY: abc...xyz
```

* Next, go back to ~/capybara
```
cd ..
```

* Then, install capybara app into system

```
sudo python3 setup.py install
```

* Next you will see where the project is installed in. It should be in: 
```
/usr/local/lib/python3.5/dist-packages/capybara...
```

### Installing unit file Capybara_App.service.
* You need to copy unit file Capybara_App.service into systemd/system. Example command:

```
~/capybara $ sudo cp Capybara_App.service /etc/systemd/system/
```

* After copying unit file into .../system, you need to give the permission to execute the unit file. Example command: 
```
sudo chmod 775 /etc/systemd/system/Capybara_App.service
```

* Then, you need reload all unit files to recongnize your new service:
```
sudo systemctl daemon-reload
```

* Next, you need to enable Capybara_App.service service:
```
sudo systemctl enable Capybara_App.service 
```

* However, you need to reboot to enable RPI to read sensors
```
sudo reboot
```

***Before start the service, you need to install the email service first***

* After all, you can start/stop the service:
```
sudo service Capybara_App start
```

* To show the status of service:
```
systemctl status Capybara_App.service
```

* To show the systemd journal
```
Or: journalctl -xe 

Or: journalctl -f 
```

*Note*: the service will run continually, after the system is boot-up.

### Installing email service
* To analyse and inform to the manager to know if the system is stopped unintended.

* To Install email service. You can follow the instruction [here](http://www.raspberry-projects.com/pi/software_utilities/email/ssmtp-to-send-emails)

* Or follow the commands belows:
```
sudo apt-get install -y ssmtp
sudo apt-get install -y mailutils
``` 

* Now edit the SSMTP configuration file:
```
sudo nano /etc/ssmtp/ssmtp.conf
```

* Then you need to include this and specify the information of your_email_account:
```
root=postmaster
mailhub=smtp.gmail.com:587
hostname=raspberrypi
AuthUser=AGmailUserName@gmail.com
AuthPass=TheGmailPassword
FromLineOverride=YES
UseSTARTTLS=YES
```

* Then, save and exit

* Now, you can test the email service by using this:
```
echo "Hello world email body" | mail -s "Test Subject" your_email_address@domain.com
```

* Then, you need install *mpack* to send a file to email account:
```
sudo apt-get install -y mpack
```

* Now, you can test the service by using this:
```
mpack -s "Test" /home/pi/some_folder/somefile.ext your_email_address@domain.com
```

***If you got the error while sending email, then you have to change the security setting in your email account.*** 

* For example, if you are using Gmail, you can follow the instruction [here](https://stackoverflow.com/questions/38391412/raspberry-pi-send-mail-from-command-line-using-gmail-smtp-server)

```
1. Login to your gmail account
2. Go to: Settings -> Accounts and Import -> Other Google Account settings
3. Go to: Personal info & privacy -> Account overview
3. Go to: Sign-in & security -> Connect apps & sites
4. Set option Allow less secure apps to ON (on the bottom of page Sign-in & security)
```

* Then, you need to specify the email address in handle_error.py 
```
Example: sudo nano /usr/local/lib/python3.5/dist-packages/capybara-0.1-py3.5.egg/app/handle_error.py 
```

* Then: 
```
In line 7:
os.system("""mpack -s "System got error" /home/pi/error_log.txt your_email_address@gmail.com""")
```


`capybara` was written by `Jonathan Sarry <jonathan.sarry@edu.turkuamk.fi>`_.
