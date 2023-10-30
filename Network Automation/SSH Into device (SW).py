import time

import paramiko

# Define switch details
switch_ip = 'your_switch_ip'
switch_username = 'your_username'
switch_password = 'your_password'

# SSH into the switch
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(switch_ip, username=switch_username, password=switch_password)
    print("SSH connection established.")
except paramiko.AuthenticationException:
    print("Authentication failed. Please check your credentials.")
except paramiko.SSHException as e:
    print("SSH connection failed:", str(e))

# Create VLANs
vlan_commands = [
    'enable',
    'configure terminal',
    'vlan 10',
    'name VLAN10',
    'exit',
    'vlan 20',
    'name VLAN20',
    'exit',
    'exit',
]

for command in vlan_commands:
    ssh.exec_command(command)
    time.sleep(1)

# Configure IP addresses
ip_commands = [
    'enable',
    'configure terminal',
    'interface vlan 10',
    'ip address 192.168.10.1 255.255.255.0',
    'no shutdown',
    'exit',
    'interface vlan 20',
    'ip address 192.168.20.1 255.255.255.0',
    'no shutdown',
    'exit',
]

for command in ip_commands:
    ssh.exec_command(command)
    time.sleep(1)

# Configure OSPF
ospf_commands = [
    'router ospf [process-id]',
    'router-id [router-id]',
    'network [network-address] [wildcard-mask] area [area-id]',  # define other networks if needed
    'interface [interface-type] [interface-number]',
    'ip ospf [process-id] area [area-id]',
    'ip ospf priority [priority]',
    'ip ospf authentication [message-digest]',  # Authentication (optional)
    'ip ospf message-digest-key [key-id] md5 [key]',  # Authentication (optional)
    'exit',
    'exit',
]

for command in ospf_commands:
    ssh.exec_command(command)
    time.sleep(1)

# Save Config
save_config = [
    'write memory'
]

for command in save_config:
    ssh.exec_command(command)
    time.sleep(1)

# Close the SSH session
ssh.close()
print("SSH connection closed.")
