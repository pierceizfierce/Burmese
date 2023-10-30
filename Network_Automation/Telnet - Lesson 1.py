# For some reason it hangs in PyCharm but works if ran outside this IDE
# This is for a router, use to create baseline template
# Configure basics: user, enable pass, line vty, and ip on int

import getpass
import telnetlib

HOST = "10.0.0.102"
user = input("Enter Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")  # ensure you are using correct prompt
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# tn.write(b"enable\n")
# tn.write(b"pierce1\n") # DO NOT HARDCODE PASSWORD
tn.write(b"conf t\n")
tn.write(b"int loop 0\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
tn.write(b"no shut\n")
tn.write(b"ip add 2.2.2.2 255.255.255.255\n")
tn.write(b"exit\n")
# tn.write(b"router ospf 1")
# tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.write(b"exit\n")

#Save Run
tn.write(b"wr me\n")
tn.write(b"end\n")


print(tn.read_all().decode('ascii'))
