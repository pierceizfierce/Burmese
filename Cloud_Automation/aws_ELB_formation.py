import boto3
from openpyxl import Workbook
import os

# AWS credentials and region configuration
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'
region_name = 'YOUR_AWS_REGION'

# Initialize AWS clients for EC2 and ELB
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key,
                   region_name=region_name)

elb = boto3.client('elb', aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key,
                   region_name=region_name)

# Define a function to create an ELB and attach EC2 instances
def create_elb_with_instances(elb_name, instance_ids):
    # Create ELB
    elb_response = elb.create_load_balancer(
        LoadBalancerName=elb_name,
        Listeners=[
            {
                'Protocol': 'HTTP',
                'LoadBalancerPort': 80,
                'InstancePort': 80
            },
        ],
        AvailabilityZones=[
            region_name + 'a',  # Adjust availability zones as needed
        ],
    )

    # Attach instances to ELB
    elb.register_instances_with_load_balancer(
        LoadBalancerName=elb_name,
        Instances=[
            {'InstanceId': instance_id} for instance_id in instance_ids
        ]
    )

    return elb_response

# Configuration for creating ELB and attaching instances
elb_name = 'my-load-balancer'
instance_ids_to_attach = [
    'i-1234567890abcdef0',  # Replace with your EC2 instance IDs
    'i-abcdef1234567890',
    # Add more instance IDs here as needed
]

# Create ELB and attach instances based on the configurations
elb_info = create_elb_with_instances(elb_name, instance_ids_to_attach)

# Prepare to write ELB and instance details to an Excel file
workbook = Workbook()
sheet = workbook.active
sheet.title = 'ELB with Instances'
sheet['A1'] = 'ELB Name'
sheet['B1'] = 'ELB DNS Name'
sheet['A2'] = elb_info['LoadBalancers'][0]['LoadBalancerName']
sheet['B2'] = elb_info['LoadBalancers'][0]['DNSName']
sheet['D1'] = 'Instance ID'
sheet['E1'] = 'Instance Type'
sheet['F1'] = 'Public IP'
sheet['G1'] = 'Private IP'

# Retrieve instance details for attached instances
instances_info = ec2.describe_instances(InstanceIds=instance_ids_to_attach)

# Fill in the instance details into the Excel sheet
row_index = 3
for reservation in instances_info['Reservations']:
    for instance in reservation['Instances']:
        sheet[f'D{row_index}'] = instance['InstanceId']
        sheet[f'E{row_index}'] = instance['InstanceType']
        sheet[f'F{row_index}'] = instance.get('PublicIpAddress', 'N/A')
        sheet[f'G{row_index}'] = instance['PrivateIpAddress']
        row_index += 1

# Save the workbook to a file on the desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
excel_file_path = os.path.join(desktop_path, 'elb_with_instances.xlsx')
workbook.save(excel_file_path)

print(f"ELB details with associated instances saved to: {excel_file_path}")
