from napalm import get_network_driver

# Define the network driver based on the vendor of the device
driver = get_network_driver('vendor')  # Replace 'vendor' with the actual vendor name

# Create a dictionary with the device information
device = driver(hostname='hostname or IP', username='username', password='password')

# Open the connection to the device
device.open()

# Configuration changes
config_commands = [
    'command 1',
    'command 3',
    # Add more commands as needed
]

# Apply the configuration
device.load_merge_candidate(config=config_commands)
device.commit_config()

# Close the connection
device.close()
