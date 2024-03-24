import os
from netmiko import ConnectHandler
from getpass import getpass

nexus1 = {
    "host": 'nxos1.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(), 
    "device_type": 'cisco_ios',
    "session_log": 'my_session.txt',
    
}

nexus2 = {
    "host": 'nxos2.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(), 
    "device_type": 'cisco_ios',
    "session_log": 'my_session.txt',
    
}
#net_connect = ConnectHandler(**nexus1)
#print(net_connect.find_prompt())

for devices in (nexus1, nexus2):
    net_connect = ConnectHandler(**devices)
    print(net_connect.find_prompt())
