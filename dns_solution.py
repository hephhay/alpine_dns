# Import Scapy and socket
from scapy.all import *
import socket

# Define the target domain
target_domain = "example.com"

# Get the expected IP address for the target domain
expected_ip = socket.gethostbyname(target_domain)

# Define a function to process DNS packets


def process_packet(packet):
    # Check if the packet has DNS layer and DNS response
    if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 1:
        # Get the DNS query name and answer
        query = packet.getlayer(DNS).qd.qname
        answer = packet.getlayer(DNS).an.rdata
        # Check if the query matches the target domain and the answer does not match the expected IP address
        if query.decode() == target_domain + "." and answer != expected_ip:
            # Print a warning message
            print(f"Warning: DNS cache poisoning attack detected!")
            print(f"Query: {query.decode()}")
            print(f"Answer: {answer}")
            print(f"Expected: {expected_ip}")


# Sniff DNS packets on the network interface eth0 with a filter for the container's IP address
sniff(iface="eth0", filter="port 53 and host 172.18.5.10", prn=process_packet)
