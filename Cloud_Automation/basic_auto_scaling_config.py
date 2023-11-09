import boto3

# Create an EC2 client
ec2_client = boto3.client('ec2', region_name='us-east-1')

# Create an Auto Scaling client
autoscaling_client = boto3.client('autoscaling', region_name='us-east-1')

# Create a CloudWatch client
cloudwatch_client = boto3.client('cloudwatch', region_name='us-east-1')

# Define launch configuration
launch_config_name = 'my-launch-config'
instance_type = 't2.micro'
ami_id = 'ami-12345678'  # Replace with your AMI ID

autoscaling_client.create_launch_configuration(
    LaunchConfigurationName=launch_config_name,
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName='your-key-pair',  # Replace with your key pair name
)

# Define an Auto Scaling group
asg_name = 'my-auto-scaling-group'
min_size = 2
max_size = 5
desired_capacity = 3
availability_zones = ['us-east-1a', 'us-east-1b']  # Replace with your desired AZs

autoscaling_client.create_auto_scaling_group(
    AutoScalingGroupName=asg_name,
    LaunchConfigurationName=launch_config_name,
    MinSize=min_size,
    MaxSize=max_size,
    DesiredCapacity=desired_capacity,
    AvailabilityZones=availability_zones,
)

# Create a scaling policy
scaling_policy_name = 'my-scaling-policy'
adjustment_type = 'ChangeInCapacity'
scaling_adjustment = 1

response = autoscaling_client.put_scaling_policy(
    AutoScalingGroupName=asg_name,
    PolicyName=scaling_policy_name,
    AdjustmentType=adjustment_type,
    ScalingAdjustment=scaling_adjustment,
)

# Create a CloudWatch alarm to trigger the scaling policy
alarm_name = 'my-cpu-alarm'
metric_name = 'CPUUtilization'
namespace = 'AWS/EC2'
comparison_operator = 'GreaterThanThreshold'
threshold = 80  # Set your threshold
evaluation_periods = 1
alarm_description = 'Scale up when CPU utilization is high'
alarm_actions = [response['PolicyARN']]  # Use the ARN of the scaling policy

cloudwatch_client.put_metric_alarm(
    AlarmName=alarm_name,
    AlarmDescription=alarm_description,
    ActionsEnabled=True,
    MetricName=metric_name,
    Namespace=namespace,
    Statistic='Average',
    Period=300,  # 5-minute intervals
    EvaluationPeriods=evaluation_periods,
    Threshold=threshold,
    ComparisonOperator=comparison_operator,
    AlarmActions=alarm_actions,
)

# Attach the alarm to the Auto Scaling group
autoscaling_client.put_notification_configuration(
    AutoScalingGroupName=asg_name,
    NotificationTypes=['autoscaling:EC2_INSTANCE_TERMINATE'],
    TopicARN='arn:aws:sns:us-east-1:123456789012:my-sns-topic',  # Replace with your SNS topic ARN
)

# You can add more alarms and scaling policies as needed

# Save your configuration in a text file
with open('auto_scaling_config.txt', 'w') as file:
    file.write(f'Auto Scaling Group Name: {asg_name}\n')
    file.write(f'Launch Configuration Name: {launch_config_name}\n')
    file.write(f'Scaling Policy Name: {scaling_policy_name}\n')
    file.write(f'CloudWatch Alarm Name: {alarm_name}\n')

print('Auto-scaling configuration created and saved to auto_scaling_config.txt')
