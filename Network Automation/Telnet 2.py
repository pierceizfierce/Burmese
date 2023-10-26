from __future__ import print_function
from __future__ import print_function

from netlib import *
from netlib import *

# system parameters
switch_username = 'admin' # edit to reflect
switch_telnet_password = 'C1sc0123' # edit to reflect
switch_enable_password = 'C1sc0123'  # edit to reflect
ftp_username = 'user'  # edit to reflect
ftp_password = 'password'  # edit to reflect
configuration_server = "10.0.0.100"  # edit to reflect

host_list = open('/root/PycharmProjects/scripting/ip_address_list.txt', 'r')

firmware_2960 ='c2960-ipbase-mz.122-35.SE5.bin'
firmware_3560 = 'c3560-ipbase-mz.122-35.SE5.bin'

min_flash_req = 10000000

rsa_key_length = 2048


def login_to_node():
    # use Telnet
    try:
        child = pexpect.spawn('telnet %s' % (host))
        child.expect('Username:')
        child.sendline(switch_username)
        child.expect('Password:')
        child.sendline(switch_telnet_password)
        child.expect('#')
    print(("Successfully Telnetted to host "), (host))
    except
    try:
        # child.expect('>')
        child.sendline('enable')
        child.expect('Password:')
        child.sendline(switch_enable_password)
        child.expect('#')
    print(("Successfully Telneted to host "), (host), (',and enabled console'))

except:
print(("Failed to Telnet to host "), (host))
return


# update firmware
def update_firmware():
    try:
        # check platform
        # child = pexpect.spawn()

        # check model
        child.sendline('show version | include Model number')
        # child.expect('(?:Processor\sboard\sID\s)(\d|\w{11})')
        # hardware_model = child.after[-11:]

        # check running firmware
        child.sendline('show version | include MSystem image')
        # child.expect('(?:Processor\sboard\sID\s)(\d|\w{11})')
        # firmware = child.after[-11:]

        # check available space
        child.sendline('show flash | include bytes total')
        # child.expect('(?:Processor\sboard\sID\s)(\d|\w{11})')
        # flash_available = child.after[-11:]

        # upload new firmware
        # confirm md5
        # set boot variable
        # delete old firmware
        # notify upgrade
        # reboot
        print(("Successfully updated firmware on host "), (host))
    except:
        print(("Failed to update firmware on host "), (host))
    return


# load configuration update
def load_config_update():
    try:
        # copy config file to unit
        # child = pexpect.spawn()
        child.sendline('copy ftp: flash:')
        child.expect('[Address or name of remote host []?]')
        child.sendline(configuration_server)
        child.expect('[Source filename []?]')
        child.sendline('temp_config.cfg')
    print("Using device config file temp_config.cfg")
    child.sendline('temp_config.cfg')
    child.expect('[Source filename []?]')
    child.sendline('temp_config.cfg')
    child.expect('#')


print(("Successfully copied files to flash "), (host))

# copy config to running config (append current)
try:
    child.sendline('copy flash:temp_config.cfg running-config')
    child.expect('[?]')
    child.sendline('running-config')
    child.expect('#')
print(("Successfully copied files to running-config "), (host))
except:
print(("Failed to copy files to running-config "), (host))
except:
print(("Failed to copy files to flash "), (host))
return


# load custom config
def load_custom_config():
    try:
        # get unit info
        # child = pexpect.spawn()
        child.sendline('show version | include Processor')
        child.expect('(?:Processor\sboard\sID\s)(\d|\w{11})')
        device_id = child.after[-11:]
        serial_number = device_id
    print(("This is Device-ID "), (device_id))
    print(("This is Device-SN "), (serial_number))
    config_file = '%s.cfg' % serial_number


# copy config file to unit
child.sendline('copy ftp: flash:')
child.expect('[Address or name of remote host []?]')
child.sendline(configuration_server)
child.expect('[Source filename []?]')
print(("Using device config file "), (config_file))
child.sendline(config_file)
child.expect('[Source filename []?]')
child.sendline('temp_config.cfg')
child.expect('#')
print(("Successfully copied files to flash "), (host))

# copy config to running config (replace current)
try:
    child.sendline('copy flash:temp_config.cfg running-config')
    child.expect('[?]')
    child.sendline('running-config')
    child.expect('#')
    print(("Successfully copied files to running-config "), (host))
except:
    print(("Failed to copy files to running-config "), (host))
except:
    print(("Failed to copy files to flash "), (host))
return


# generate new crypto key
def generate_rsa_key():
    # check current key
    # ?
    # generate new key
    try:
        # child = pexpect.spawn()
        child.sendline('crypto key generate rsa')
        child.expect('(512)')
        child.sendline(rsa_key_length)
        child.expect('#')
    print(("Successfully generated new RSA key on host "), (host))

except:
print(("RSA key gen failed on host "), (host))
return


# save running config
def save_running_config():
    try:
        # child = pexpect.spawn()
        child.expect('#')
        child.sendline('write memory')
        child.expect('[OK]')
        child.expect('#')
    print(("Successfully saved the running-config on "), (host))

except:
print(("Failed to save the running-config on "), (host))


return

# backup running config
def backup_deployed_congig():
    # child.sendline('quit')
    return


# test function
def test_function():
    try:
        print(("Successfully ran the test function on host "), (host))
    except:
        print(("Test function failed on host "), (host))
    return


for line in host_list:
    host = line.split()[0]
print(("Start configuration on host "), (host))
platform = None
hardware_model = None
firmware = None
flash_available = None
device_id = None
serial_number = None
config_file = None

login_to_node()
# update_firmware ()
# load_config_update ()
# load_custom_config ()
# generate_rsa_key ()
save_running_config()
# backup_deployed_congig ()
test_function()