import subprocess

# Define the playbook file and inventory file
playbook_file = 'your_playbook.yml'
inventory_file = 'your_inventory.ini'

# Build the Ansible command
ansible_command = f'ansible-playbook -i {inventory_file} {playbook_file}'

# Execute the Ansible playbook using subprocess
try:
    subprocess.run(ansible_command, shell=True, check=True)
    print("Ansible playbook executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing Ansible playbook: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
