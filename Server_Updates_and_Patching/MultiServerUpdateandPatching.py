import paramiko
import winrm
import pandas as pd

# Assuming your Excel file has columns 'IP', 'Hostname', 'OS', 'Username', and 'Password'
df = pd.read_excel('servers.xlsx') # Location of server .xlsx

for index, row in df.iterrows():
    server_ip = row['IP']
    username = row['Username'] # replace this with a service account in spreadsheet and server(s)
    password = row['Password'] # replace this with API or PSK on server(s)
    os_type = row['OS']

# Perform actions based on the OS type (Linux or Windows)
    if os_type.lower() == 'linux':
# Use Paramiko for Linux servers
    elif os_type.lower() == 'windows':
# Use pywinrm for Windows servers

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_ip, username, password) # test these for proper functionality

    stdin, stdout, stderr = ssh.exec_command('sudo apt update && sudo apt upgrade -y')
    print(stdout.read().decode())
    ssh.close()

    session = winrm.Session('windows_server_ip', auth=('your_username', 'your_password'))
    encoded_ps = f'[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; Invoke-Expression (New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'); choco upgrade all -y'

    result = session.run_ps(encoded_ps)
    print(result.std_out.decode())
