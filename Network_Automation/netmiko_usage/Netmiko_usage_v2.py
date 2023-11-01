from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.100',
    'username': 'pierce',
    'password': 'pierce1',  # DO NOT HARDCODE PASSWORDS
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print(output)

# Config Area
config_commands = ['int loop 2',
                   'ip add 20.20.20.20 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range(31, 101):
    print("Creating VLAN " + str(n))
    config_commands = ['int ' + str(n), 'name Python_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)
