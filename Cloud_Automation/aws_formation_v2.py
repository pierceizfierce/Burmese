import boto3
from openpyxl import Workbook
import os

# AWS credentials and region configuration
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'
region_name = 'YOUR_AWS_REGION'

# Initialize AWS EC2 client
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key,
                   region_name=region_name)

# Define a function to create EC2 instances
def create_ec2_instances(instance_config):
    response = ec2.run_instances(
        ImageId=instance_config['image_id'],
        InstanceType=instance_config['instance_type'],
        MinCount=instance_config['min_count'],
        MaxCount=instance_config['max_count'],
        KeyName=instance_config['key_name']
        # Add more parameters as needed (e.g., SecurityGroupIds, SubnetId, etc.)
    )
    return response['Instances']

# Configuration for creating EC2 instances
instances_to_create = [
    {
        'image_id': 'ami-12345678',  # Example AMI ID
        'instance_type': 't2.micro',
        'min_count': 1,
        'max_count': 1,
        'key_name': 'my-keypair'  # Name of your EC2 key pair
    },
    # Add more instance configurations here as needed
]

# Create EC2 instances based on the configurations
created_instances = []
for config in instances_to_create:
    instances = create_ec2_instances(config)
    created_instances.extend(instances)

# Prepare to write IPs to an Excel file
workbook = Workbook()
sheet = workbook.active
sheet.title = 'EC2 IPs'
sheet['A1'] = 'Instance ID'
sheet['B1'] = 'Instance Type'
sheet['C1'] = 'Public IP'
sheet['D1'] = 'Private IP'

# Fill in the IP details into the Excel sheet
for index, instance in enumerate(created_instances, start=2):
    sheet[f'A{index}'] = instance['InstanceId']
    sheet[f'B{index}'] = instance['InstanceType']
    sheet[f'C{index}'] = instance.get('PublicIpAddress', 'N/A')
    sheet[f'D{index}'] = instance['PrivateIpAddress']

# Save the workbook to a file on the desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
excel_file_path = os.path.join(desktop_path, 'ec2_ips.xlsx')
workbook.save(excel_file_path)

print(f"EC2 instance details saved to: {excel_file_path}")
