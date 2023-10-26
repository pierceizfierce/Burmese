import telnetlib3
import asyncio
import logging

async def configure_cisco_router():
    # Replace these with your router's details
    host = str("10.0.0.150")
    username = str("pierce")
    password = str("pierce1")
    loopback_number = str("99")  # Change this to the desired loopback number
    ip_address = str("1.1.1.1")  # Change this to the desired IP address

    reader, writer = await telnetlib3.open_connection(host, port=23)
    await reader.readuntil(b"Username: ")
    writer.write(username.encode('utf-8') + b"\n")
    await reader.readuntil(b"Password: ")
    writer.write(password.encode('utf-8') + b"\n")

    await reader.readuntil(b"RouterPrompt# ")  # Adjust the expected prompt as per your router's prompt

    # Configure the loopback interface
    writer.write(f"conf t\n".encode('utf-8'))
    writer.write(f"int Loopback{loopback_number}\n".encode('utf-8'))
    writer.write(f"ip address {ip_address} 255.255.255.255\n".encode('utf-8'))
    writer.write(b"end\n")
    writer.write(b"exit\n")

    await writer.drain()
    writer.close()

    print(f"Loopback interface {loopback_number} configured with IP address {ip_address}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(configure_cisco_router())

async def configure_cisco_router():
    try:
        # Your code here
        # ...
    except Exception as e:
        # Log the exception
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(configure_cisco_router())