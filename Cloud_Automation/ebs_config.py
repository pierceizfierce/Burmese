import boto3

eb = boto3.client('elasticbeanstalk')

# Create an Elastic Beanstalk application
application_name = 'MyWebApp'
eb.create_application(ApplicationName=application_name)

# Create an Elastic Beanstalk environment within an existing VPC
environment_name = 'MyWebApp-Environment'
solution_stack_name = '64bit Amazon Linux 2 v5.6.0 running Python 3.7'
subnet_ids = ['subnet-1', 'subnet-2']  # Replace with your actual subnet IDs
security_group_ids = ['sg-1', 'sg-2']  # Replace with your actual security group IDs

eb.create_environment(
    ApplicationName=application_name,
    EnvironmentName=environment_name,
    SolutionStackName=solution_stack_name,
    OptionSettings=[
        {
            'Namespace': 'aws:ec2:vpc',
            'OptionName': 'VPCId',
            'Value': 'vpc-12345678'  # Replace with your VPC ID
        },
        {
            'Namespace': 'aws:ec2:vpc',
            'OptionName': 'Subnets',
            'Value': ','.join(subnet_ids)
        },
        {
            'Namespace': 'aws:ec2:instances',
            'OptionName': 'SecurityGroups',
            'Value': ','.join(security_group_ids)
        },
    ]
)

# Creating EBS environment variables

elasticbeanstalk = boto3.client('elasticbeanstalk')

# Define your application and environment names
application_name = 'MyWebApp'
environment_name = 'MyWebApp-Environment'

# Prompt the user for database connection details
db_host = input("Enter the database host: ")
db_user = input("Enter the database username: ")
db_password = input("Enter the database password: ")

# Define the environment variables as a dictionary
environment_variables = [
    {
        'Name': 'DB_HOST',
        'Value': db_host,
        'OptionSettings': [
            {
                'Namespace': 'aws:elasticbeanstalk:application:environment',
                'OptionName': 'DB_HOST'
            }
        ]
    },
    {
        'Name': 'DB_USER',
        'Value': db_user,
        'OptionSettings': [
            {
                'Namespace': 'aws:elasticbeanstalk:application:environment',
                'OptionName': 'DB_USER'
            }
        ]
    },
    {
        'Name': 'DB_PASSWORD',
        'Value': db_password,
        'OptionSettings': [
            {
                'Namespace': 'aws:elasticbeanstalk:application:environment',
                'OptionName': 'DB_PASSWORD'
            }
        ]
    }
]

# Update the environment with the new environment variables
elasticbeanstalk.update_environment(
    ApplicationName=application_name,
    EnvironmentName=environment_name,
    OptionSettings=environment_variables
)

print("Environment variables updated successfully.")
