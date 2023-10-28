import getpass
import telnetlib

HOST = "10.0.0.150"
user = input("Enter Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username:  ")  # ensure you are using correct prompt
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password:  ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"pierce1\n")
tn.write(b"conf t\n")
tn.write(b"int loop 0\n")
tn.write(b"ip add 1.1.1.1 255.255.255.255\n")
tn.write(b"end\n")
tn.write(b"do wr me\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
