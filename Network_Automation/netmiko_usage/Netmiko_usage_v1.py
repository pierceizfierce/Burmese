import pandas as pd
from netmiko import ConnectHandler

# Replace 'your_device_info.xlsx' with the actual filename
df = pd.read_excel('your_device_info.xlsx')  # Placeholder .xlsx

for index, row in df.iterrows():
    device_info = {
        'device_type': row['Device Type'],
        'ip': row['IP Address'],
        'username': row['Username'],
        'password': row['Password'],
        # Add more parameters as needed
    }

    # Connect to the device
    connection = ConnectHandler(**device_info)

    # Send configuration commands
    config_commands = [
        'interface GigabitEthernet0/0',
        'ip address 192.168.1.2 255.255.255.0',  # Placeholder cmds
    ]
    connection.send_config_set(config_commands)

    # Disconnect from the device
    connection.disconnect()
