
import requests

# Replace these values with your own
domain = "example.com"  # The domain you want to validate
dcv_token = "your_dcv_token_here"  # The DCV token provided by your Certificate Authority
dcv_endpoint = f"https://{domain}/.well-known/pki-validation/{dcv_token}"  # The DCV endpoint URL

# Path to your client certificate and private key
client_cert = ('/path/to/client_certificate.crt', '/path/to/client_private_key.key')

# Send a PUT request to the DCV endpoint to validate control with the client certificate
try:
    response = requests.put(dcv_endpoint, cert=client_cert)
    if response.status_code == 200:
        print(f"Domain Control Validation successful for {domain}!")
    else:
        print(f"Domain Control Validation failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
