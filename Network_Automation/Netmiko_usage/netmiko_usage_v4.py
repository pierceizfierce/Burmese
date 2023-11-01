import os
from netmiko import ConnectHandler

iosv0_l2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.100',
    'username': 'pierce',
    'password': 'pierce1',  # DO NOT HARDCODE PASSWORDS
}

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
iosv4_l2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.104',
    'username': 'pierce',
    'password': 'pierce1',  # DO NOT HARDCODE PASSWORDS
}
iosv5_l2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.0.105',
    'username': 'pierce',
    'password': 'pierce1',  # DO NOT HARDCODE PASSWORDS
}

sw_config = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(sw_config, r'C:\Users\dpierce\PycharmProjects\Burmese\Network_Automation\source_lists\iosv_l2_cisco_access_switch_design.txt')

with open(filename) as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [iosv0_l2, iosv1_l2, iosv2_l2, iosv3_l2, iosv4_l2, iosv5_l2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    # output = net_connect.send_command('show ip int brief')
    print(output)
