import paramiko
import winrm


# Assuming your Excel file has columns 'IP', 'Hostname', 'OS', 'Username', and 'Password'
df = pd.read_excel('servers.xlsx')

for index, row in df.iterrows():
    server_ip = row['IP']
    username = row['Username']
    password = row['Password']
    os_type = row['OS']

    # Perform actions based on the OS type (Linux or Windows)
    if os_type.lower() == 'linux':
    # Use Paramiko for Linux servers
    # ...
    elif os_type.lower() == 'windows':
# Use pywinrm for Windows servers