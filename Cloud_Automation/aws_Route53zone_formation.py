import boto3


def create_hosted_zone(domain_name):
    """
    Create a Route 53 hosted zone for a given domain name.

    Parameters:
    domain_name (str): The domain name for the hosted zone.

    Returns:
    dict: Information about the created hosted zone.
    """
    client = boto3.client('route53')

    response = client.create_hosted_zone(
        Name=domain_name,
        CallerReference=str(hash(domain_name))  # Generate a unique reference
    )

    return response['HostedZone']


def create_a_record(hosted_zone_id, dns_name, instance_ip):
    """
    Create an A record in a Route 53 hosted zone.

    Parameters:
    hosted_zone_id (str): The ID of the Route 53 hosted zone.
    dns_name (str): The DNS name to associate with the A record.
    instance_ip (str): The IP address of the instance.

    Returns:
    dict: Information about the created DNS record set.
    """
    client = boto3.client('route53')

    response = client.change_resource_record_sets(
        HostedZoneId=hosted_zone_id,
        ChangeBatch={
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': dns_name,
                        'Type': 'A',
                        'TTL': 300,
                        'ResourceRecords': [
                            {
                                'Value': instance_ip
                            },
                        ]
                    }
                }
            ]
        }
    )

    return response['ChangeInfo']


if __name__ == "__main__":
    # Example usage:
    hosted_zone_name = 'example.com'
    instance_dns_name = 'app.example.com'
    instance_ip_address = '192.168.1.100'  # Replace with your instance's IP

    # Create hosted zone
    hosted_zone_info = create_hosted_zone(hosted_zone_name)
    hosted_zone_id = hosted_zone_info['Id'].split('/')[-1]

    print(f"Created hosted zone with ID: {hosted_zone_id}")

    # Create A record
    change_info = create_a_record(hosted_zone_id, instance_dns_name, instance_ip_address)

    print(f"Created A record for {instance_dns_name} pointing to {instance_ip_address}")
    print(f"Change info: {change_info}")
