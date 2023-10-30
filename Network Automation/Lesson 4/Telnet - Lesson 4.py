# For some reason it hangs in PyCharm but works if ran outside this IDE
# This is for a switch, use to create baseline template
# Configure basics: user, enable pass, line vty, and ip on vlan

import getpass
import telnetlib

HOST = "localhost"
user = input("Enter Username: ")
password = getpass.getpass()

f = open(r"Z:\damori.pierce\PythonProjects\Burmese\Network Automation\Lesson 4\SW_List.txt")

for IP in f:

    IP = IP.strip()
    print("Configuring Switch " + str(IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")  # ensure you are using correct prompt
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"conf t\n")
    tn.write(b"vlan 2\n")
    tn.write(b"name test vlan\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name test vlan\n")
    tn.write(b"vlan 4\n")
    tn.write(b"name test vlan\n")
    tn.write(b"vlan 5\n")
    tn.write(b"name test vlan\n")
    tn.write(b"vlan 6\n")
    tn.write(b"name test vlan\n")
    tn.write(b"vlan 7\n")
    tn.write(b"name test vlan\n")
    tn.write(b"vlan 8\n")
    tn.write(b"name test vlan\n")
    tn.write(b"vlan 9\n")
    tn.write(b"name test vlan\n")
    tn.write(b"vlan 10\n")
    tn.write(b"name test vlan\n")
    tn.write(b"vlan 11\n")
    tn.write(b"name test vlan")
    tn.write(b"end\n")
# Save Run
    tn.write(b"wr me\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
