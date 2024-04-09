<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NAPALM Usage Guide</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            font-family: Consolas, monospace;
            font-size: 1em;
            background-color: #f8f8f8;
            padding: 2px 5px;
            border-radius: 3px;
            word-wrap: break-word;
        }
    </style>
</head>
<body>
    <h1>NAPALM Usage Guide</h1>

    <h2>Introduction</h2>
    <p>NAPALM (Network Automation and Programmability Abstraction Layer with Multivendor support) is a Python library that provides a vendor-neutral interface for interacting with network devices. It supports various vendors and simplifies network automation tasks.</p>

    <h2>Installation</h2>
    <p>To use NAPALM, you need Python installed on your system. You can install NAPALM and its dependencies using pip:</p>
    <pre><code>pip install napalm</code></pre>

    <h2>Basic Usage</h2>
    <p>Here's a simple example of using NAPALM to connect to a network device and retrieve information:</p>
    <pre><code>import napalm

# Create a driver instance for the device (replace driver and hostname)
driver = napalm.get_network_driver('eos')
device = driver(hostname='device_ip_address', username='your_username', password='your_password')

# Open the connection to the device
device.open()

# Retrieve device facts (e.g., hostname, model, OS version)
facts = device.get_facts()
print(facts)

# Close the connection
device.close()
</code></pre>

    <h2>Supported Platforms</h2>
    <p>NAPALM supports a wide range of network platforms including Cisco IOS, Cisco NX-OS, Arista EOS, Juniper JunOS, and more. Refer to the <a href="https://napalm.readthedocs.io/en/latest/supported_platforms/index.html">official documentation</a> for a complete list of supported platforms.</p>

    <h2>Additional Resources</h2>
    <ul>
        <li><a href="https://napalm.readthedocs.io/en/latest/">NAPALM Documentation</a></li>
        <li><a href="https://github.com/napalm-automation/napalm">NAPALM GitHub Repository</a></li>
        <li><a href="https://github.com/napalm-automation/napalm/tree/develop/examples">NAPALM Examples</a></li>
    </ul>

    <p>For more detailed information and advanced usage of NAPALM, please refer to the <a href="https://napalm.readthedocs.io/en/latest/">official NAPALM documentation</a>.</p>
</body>
</html>
