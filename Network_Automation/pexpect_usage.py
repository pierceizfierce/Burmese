# You can use the pexpect library to automate console interactions,
#   specially when dealing with devices that require interactive input.

# Example using pexpect:
import pexpect

switch = pexpect.spawn('telnet switch_ip')
switch.expect('Username:')
switch.sendline('your_username')
switch.expect('Password:')
switch.sendline('your_password')
switch.expect('Switch>')
switch.sendline('show interfaces')
switch.expect('Switch>')
print(switch.before)

switch.close()