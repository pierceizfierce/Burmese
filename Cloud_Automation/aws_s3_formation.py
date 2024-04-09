import boto3
from openpyxl import Workbook
import os

# AWS credentials and region configuration
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'
region_name = 'YOUR_AWS_REGION'

# Initialize AWS S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key,
                   region_name=region_name)

# Define a function to create S3 buckets
def create_s3_bucket(bucket_name):
    response = s3.create_bucket(Bucket=bucket_name)
    return response

# Configuration for creating S3 buckets
buckets_to_create = [
    'my-bucket-1',
    'my-bucket-2',
    # Add more bucket names here as needed
]

# Create S3 buckets based on the configurations
created_buckets = []
for bucket_name in buckets_to_create:
    bucket_info = create_s3_bucket(bucket_name)
    created_buckets.append(bucket_info['Location'])

# Prepare to write bucket details to an Excel file
workbook = Workbook()
sheet = workbook.active
sheet.title = 'S3 Buckets'
sheet['A1'] = 'Bucket Name'
sheet['B1'] = 'Region'

# Fill in the bucket details into the Excel sheet
for index, bucket_name in enumerate(buckets_to_create, start=2):
    sheet[f'A{index}'] = bucket_name
    sheet[f'B{index}'] = created_buckets[index - 2]  # corresponding region info

# Save the workbook to a file on the desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
excel_file_path = os.path.join(desktop_path, 's3_buckets.xlsx')
workbook.save(excel_file_path)

print(f"S3 bucket details saved to: {excel_file_path}")
