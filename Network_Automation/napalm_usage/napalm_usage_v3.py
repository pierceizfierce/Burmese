# get driver for supported devices at:
# https://napalm.readthedocs.io/en/latest/support/#configuration-support-matrix
# https://developer.arubanetworks.com/aruba-aoscx/docs/installing-arubas-napalm-drivers
import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('10.0.0.105', 'pierce', 'pierce1', '1')
iosvl2.open()

ios_output = iosvl2.get_mac_address_table()
print(json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = iosvl2.get_arp_table()
print(json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = iosvl2.get_mac_address_table()
print(json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = iosvl2.get_interfaces_ip()
print(json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = iosvl2.get_interfaces_counters()
print(json.dumps(ios_output,sort_keys=True, indent=4))

