import socket
import time

# Set the target domain
target_domain = "example.com"

while True:
    # Resolve the domain name to an IP address
    actual_server_ip = socket.gethostbyname(target_domain)

    # Create a socket for network communication
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the actual server
    client_socket.connect((actual_server_ip, 80))

    # Send an HTTP request for the target domain
    request = f"GET / HTTP/1.1\r\nHost: {target_domain}\r\n\r\n"
    client_socket.send(request.encode())

    # Receive the response from the server
    response = client_socket.recv(1024)

    # Print the response
    print(response.decode())

    # Close the socket
    client_socket.close()

    # Wait for 10 seconds before sending the next request
    time.sleep(10)
