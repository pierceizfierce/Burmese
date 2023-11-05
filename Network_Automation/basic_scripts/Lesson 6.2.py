# For some reason it hangs in PyCharm but works if ran outside this IDE
# This is for a switch, use to create baseline template
# Configure basics: user, enable pass, line vty, and ip on vlan

import getpass
import telnetlib

# HOST = "localhost"
user = input("Enter Username: ")
password = getpass.getpass()

f = open(r"/Network_Automation/source_lists/core_sw_list.txt")

for IP in f:

    IP = IP.strip()
    print('Getting running config from SW: ' + str(IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")  # ensure you are using correct prompt
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

# Config Area
    tn.write(b"terminal length 0\n")  # so you don't have to hit the space-bar
    tn.write(b"show run\n")
    tn.write(b"exit\n")

# Enable SSH
    tn.write(b"ip domain-name damori.com\n")
    tn.write(b"crypto key generate rsa\n")
    tn.write(b"1024\n")
    tn.write(b"end\n")

# Save config to a file
    readoutput = tn.read_all()
    saveoutput = open("switch " + HOST, "w")
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close()

    print(tn.read_all().decode('ascii'))
