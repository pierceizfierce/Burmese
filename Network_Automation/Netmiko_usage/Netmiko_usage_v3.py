from netmiko import ConnectHandler

iosv1_l2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.101',
    'username': 'pierce',
    'password': 'pierce1',  # DO NOT HARDCODE PASSWORDS
}
iosv2_l2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.102',
    'username': 'pierce',
    'password': 'pierce1',  # DO NOT HARDCODE PASSWORDS
}
iosv3_l2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.103',
    'username': 'pierce',
    'password': 'pierce1',  # DO NOT HARDCODE PASSWORDS
}

all_devices = [iosv1_l2, iosv2_l2, iosv3_l2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    # output = net_connect.send_command('show ip int brief')
    # print(output)

    # Config Area
    #      config_commands = ['int loop 1',
    #                        'ip add 20.20.20.20 255.255.255.0']
    #     output = net_connect.send_config_set(config_commands)
    #     print(output)

    for n in range(30, 41):
        print("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
        