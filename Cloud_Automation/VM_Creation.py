from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim

# Set your ESXi host, username, and password
host = "10.0.0.241"
username = "root"
password = "QEZCczeq08^$qaz"

# Connect to the ESXi host
si = SmartConnect(host=host, user=username, pwd=password)

# Create a new VM
def create_vm(vm_name, datacenter_name, datastore_name, cluster_name, network_name):
    content = si.RetrieveContent()

    # Specify the VM configuration
    vm_folder = content.rootFolder
    datacenter = content.rootFolder.childEntity[0]
    vm_resource_pool = content.rootFolder.childEntity[0].hostFolder.childEntity[0].resourcePool
    datastore = content.rootFolder.childEntity[0].datastoreFolder.childEntity[0]
    network = content.rootFolder.childEntity[0].networkFolder.childEntity[0]

    # Create VM config spec
    vmx_file = vim.vm.FileInfo(logDirectory=None, snapshotDirectory=None, suspendDirectory=None, vmPathName=datastore_name)
    config = vim.vm.ConfigSpec(name=vm_name, memoryMB=1024, numCPUs=1, files=vmx_file, guestId="rhel7_64Guest")

    # Create VM
    task = vm_folder.CreateVM_Task(config=config, pool=vm_resource_pool)

    # Wait for the task to complete
    while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
        pass

    if task.info.state == vim.TaskInfo.State.success:
        print(f"VM '{vm_name}' created successfully.")
    else:
        print(f"Error creating VM '{vm_name}': {task.info.error.msg}")

# Call the function to create a VM
create_vm(vm_name="DamorisPC",
          datacenter_name="Lab",
          datastore_name=".241 NAS",
          cluster_name="Lab Cluster",
          network_name="VM Network")

# Disconnect from the ESXi host
Disconnect(si)