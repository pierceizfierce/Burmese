# For some reason it hangs in PyCharm but works if ran outside this IDE
# This is for a switch, use to create baseline template
# Configure basics: user, enable pass, line vty, and ip on vlan

import getpass
import telnetlib

HOST = "10.0.0.103"
user = input("Enter Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")  # ensure you are using correct prompt
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"pierce1\n")  # DO NOT HARDCODE PASSWORD
tn.write(b"conf t\n")

for n in range (2,11):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name Placeholder_vlan" + str(n).encode('ascii') + b"\n")

# # use these individual CMDs for single changes
# tn.write(b"vlan 2\n")
# tn.write(b"name test vlan\n")
# tn.write(b"exit\n")
# tn.write(b"int vlan2\n")
# tn.write(b"ip add 10.0.0.103 255.255.255.0\n")
# tn.write(b"no shut\n")
# tn.write(b"exit\n")
# tn.write(b"exit\n")

# Save Run
tn.write(b"wr me\n")
tn.write(b"end\n")

print(tn.read_all().decode('ascii'))
