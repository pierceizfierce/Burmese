import paramiko
import winrm
import pandas as pd

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('linux_server_ip', username='your_username', password='your_password')

stdin, stdout, stderr = ssh.exec_command('sudo apt update && sudo apt upgrade -y')
print(stdout.read().decode())
ssh.close()

session = winrm.Session('windows_server_ip', auth=('your_username', 'your_password'))
encoded_ps = f'[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; Invoke-Expression (New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'); choco upgrade all -y'

result = session.run_ps(encoded_ps)
print(result.std_out.decode())




