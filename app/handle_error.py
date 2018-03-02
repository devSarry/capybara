#!/usr/bin/python

import os, sys

#Copying -last 50 lines from journalctl to error_log.txt file and sending them to email.
os.system("journalctl -u Capybara_App.service -e -n 50 --no-pager > /home/pi/error_log.txt")
os.system("""mpack -s "System got error" /home/pi/error_log.txt your_email_address@gmail.com""")
