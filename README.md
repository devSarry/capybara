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

* Going to the directory which you have cloned this project (.../capybara/), then:
```
sudo pip3 install -r requirements.txt
```

* Then, install capybara app into system

```
sudo python3 setup.py install
```

* Next you will see where the project is installed in. It should be in: 
```
/usr/local/lib/python3.5/dist-packages/capybara...
```

* Next, you need go to dir where you have installed Capybara app, then you need to copy example.config.yaml to be config.yaml:
```
sudo cp example.config.yaml config.yaml
```

* Next, you need to ***erase*** the value of **NAME** in config.yaml to create new Device. Example:
```
NAME: 
PASSWORD: abc...xyz
SECRET_KEY: abc...xyz

```


### Installing unit file Capybara_App.service.
* You need to copy unit file Capybara_App.service into systemd/system. Example path:

```
/etc/systemd/system/
```

* After copying unit file into .../system, you need to give the permission to execute the unit file
```
sudo chmod 775 Capybara_App.service
```

* Then, you need reload all unit files to recongnize your new service:
```
sudo systemctl daemon-reload
```

* Then, you need to enable Capybara_App.service service:
```
sudo systemctl enable Capybara_App.service 
```

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


`capybara` was written by `Jonathan Sarry <jonathan.sarry@edu.turkuamk.fi>`_.
