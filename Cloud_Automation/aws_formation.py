import boto3

# Initialize AWS clients
ec2 = boto3.client('ec2')
s3 = boto3.client('s3')
rds = boto3.client('rds')

# Create VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc_id = vpc['Vpc']['VpcId']

# Create subnets
subnet1 = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.0.0/24', AvailabilityZone='us-east-1a')
subnet2 = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24', AvailabilityZone='us-east-1b')

# Create an Internet Gateway and attach it to the VPC
igw = ec2.create_internet_gateway()
igw_id = igw['InternetGateway']['InternetGatewayId']
ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)

# Create a route table for the public subnet
route_table = ec2.create_route_table(VpcId=vpc_id)
ec2.create_route(RouteTableId=route_table['RouteTable']['RouteTableId'], DestinationCidrBlock='0.0.0.0/0', GatewayId=igw_id)
ec2.associate_route_table(SubnetId=subnet1['Subnet']['SubnetId'], RouteTableId=route_table['RouteTable']['RouteTableId'])

# Create security groups
security_group1 = ec2.create_security_group(GroupName='WebServerSG', Description='Web Server Security Group', VpcId=vpc_id)
security_group2 = ec2.create_security_group(GroupName='DatabaseSG', Description='Database Security Group', VpcId=vpc_id)

# Create S3 buckets
s3.create_bucket(Bucket='my-first-bucket')
s3.create_bucket(Bucket='my-second-bucket')

# Create an RDS instance
rds.create_db_instance(DBName='mydb', DBInstanceIdentifier='mydbinstance', AllocatedStorage=20,
                       DBInstanceClass='db.t2.micro', Engine='mysql', MasterUsername='admin',
                       MasterUserPassword='mypassword', VPCSecurityGroups=[security_group2['GroupId']])

# Launch EC2 instances in the subnets
ec2.run_instances(ImageId='your-ami-id', MinCount=1, MaxCount=1, KeyName='your-key-pair', InstanceType='t2.micro',
                 SubnetId=subnet1['Subnet']['SubnetId'], SecurityGroupIds=[security_group1['GroupId']])
ec2.run_instances(ImageId='your-ami-id', MinCount=1, MaxCount=1, KeyName='your-key-pair', InstanceType='t2.micro',
                 SubnetId=subnet2['Subnet']['SubnetId'], SecurityGroupIds=[security_group1['GroupId']])

# Attach EBS volumes to EC2 instances
ec2.create_volume(AvailabilityZone='us-east-1a', Size=8, VolumeType='gp2')
ec2.create_volume(AvailabilityZone='us-east-1b', Size=8, VolumeType='gp2')

# Wait for the instances to be running (you can use a more robust approach here)
import time
time.sleep(60)

# Assign private IP addresses to the instances
ec2.modify_network_interface_attribute(NetworkInterfaceId='your-network-interface-id', SourceDestCheck={'Value': False})
ec2.modify_network_interface_attribute(NetworkInterfaceId='your-network-interface-id', PrivateIpAddresses=[
    {
        'PrivateIpAddress': '10.0.0.10',
        'Primary': True
    }
])
