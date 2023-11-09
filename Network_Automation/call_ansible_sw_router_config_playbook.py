import os
import tempfile
import csv

# Prompt the user for username and password
username = input("Enter the username for Cisco devices: ")
password = input("Enter the password for Cisco devices: ")

# Read switch and router IPs from a CSV file
ip_file = 'devices.csv'  # Replace 'devices.csv' with the path to your CSV file

# Initialize the inventory string
inventory = ""

with open(ip_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if 'device_type' in row and row['device_type'] in ['switch', 'router']:  # ensure these columns are in the CSV
            inventory += f"[{row['device_type']}\n"
            inventory += f"{row['device_name']} ansible_host={row['ip']} ansible_user={username} ansible_password={password}\n"

# Define the Ansible playbook to configure switches and routers (same as before)
playbook = """
---
- name: Configure Cisco Switches and Routers
  hosts: switches:routers
  gather_facts: no
  tasks:
    - name: Configure VLANs
      ios_vlan:
        vlan_id: "{{ item }}"
        name: "VLAN {{ item }}"
        state: present
      with_sequence: start=1 end=16
      when: "'switch' in inventory_hostname"

    - name: Configure Trunk Ports
      ios_interface:
        name: "GigabitEthernet0/1"  # Change this to your trunk port
        description: "Trunk Port"
        switchport: true
        switchport_mode: trunk
        trunk_vlans: "all"
      when: "'switch' in inventory_hostname"

    - name: Configure RSTP
      ios_spanning_tree:
        mode: rapid-pvst
      when: "'switch' in inventory_hostname"

    - name: Configure OSPF Routing
      ios_ospf:
        process_id: 1
        router_id: 1.1.1.1  # Change this to the router's ID
        network:
          - { area: 0, prefix: 192.168.1.0/24 }  # Configure your OSPF networks
          - { area: 0, prefix: 192.168.2.0/24 }
      when: "'router' in inventory_hostname"
"""

# Create temporary inventory and playbook files (same as before)
with tempfile.NamedTemporaryFile(mode='w', delete=False) as inv_file, tempfile.NamedTemporaryFile(mode='w', delete=False) as pb_file:
    inv_file.write(inventory)
    pb_file.write(playbook)
    inventory_file_path = inv_file.name
    playbook_file_path = pb_file.name

# Run the Ansible playbook (same as before)
os.system(f"ansible-playbook -i {inventory_file_path} {playbook_file_path}")

# Clean up temporary files (same as before)
os.remove(inventory_file_path)
os.remove(playbook_file_path)
