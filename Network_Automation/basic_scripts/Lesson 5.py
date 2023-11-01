# For some reason it hangs in PyCharm but works if ran outside this IDE
# This is for a switch, use to create baseline template
# Configure basics: user, enable pass, line vty, and ip on vlan

import getpass
import telnetlib

# HOST = "localhost"
user = input("Enter Username: ")
password = getpass.getpass()

f = open(r"C:\Users\dpierce\PycharmProjects\Burmese\Network_Automation\source_lists\SW_List.txt")

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

# Config Area
    tn.write(b"conf t\n")
    for n in range(12, 21):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name Placeholder_vlan" + str(n).encode('ascii') + b"\n")
    tn.write(b"end\n")

# Save Run
    tn.write(b"wr me\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
