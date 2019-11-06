#python script to backup config of router
#netmiko script

import getpass
import telnetlib
import sys
import errno
import errno
import datetime
import os
from netmiko import ConnectHandler                                                                                  
import datetime
path = '/root/netmiko'
I = open('hosts')
for IP in I:
        print ('\n  '+ IP.strip() + '  \n' )
        RTR ={
        'ip':   IP,
        'username': 'prabin',
        'password': 'prabin',
        'secret':'cisco',
        'device_type': 'cisco_ios',
        }
        
        net_connect = ConnectHandler(**RTR)
        net_connect.enable()
        output = net_connect.send_command("show run")
        SAVE_FILE = open(os.path.join(path,IP), 'w+')
        #SAVE_FILE = open("IP" + "w")
        SAVE_FILE.write(output)
        SAVE_FILE.close
