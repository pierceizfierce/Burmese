# get driver for supported devices at:
# https://napalm.readthedocs.io/en/latest/support/#configuration-support-matrix
# https://developer.arubanetworks.com/aruba-aoscx/docs/installing-arubas-napalm-drivers
import json
import socket

from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('10.0.0.100', 'pierce', 'pierce1', 1)
iosvl2.open()

ios_output = iosvl2.get_mac_address_table()
print(json.dumps(ios_output, sort_keys=True, indent=4))

# Define the target FQDN
target_fqdn = "google.com"

# Resolve the FQDN to an IP address
try:
    ip_address = socket.gethostbyname(target_fqdn)
except socket.gaierror:
    print(f"Failed to resolve {target_fqdn} to an IP address")
else:
    # Use the IP address with Napalm's ping method
    device = iosvl2
    device.open()

    result = device.ping(ip_address)

    print(json.dumps(result, sort_keys=True, indent=4))
    device.close()
