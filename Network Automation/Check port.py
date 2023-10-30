import socket

server_ip = "10.0.0.102"  # Replace with the actual server IP address
server_port = 23  # Replace with the actual port number

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    # You can send and receive data here if the connection is successful
except ConnectionRefusedError:
    print("Connection refused. Check the server and port.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client_socket.close()