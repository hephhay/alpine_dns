# Use Alpine Linux as the base image
FROM alpine:3.14

# Install Dnsmasq and Scapy with apk package manager
RUN apk add --no-cache dnsmasq scapy

# Copy the configuration file for Dnsmasq
COPY dnsmasq.conf /etc/dnsmasq.conf

# Copy the script for DNS cache poisoning attack with Scapy
COPY dns_poison.py /dns_poison.py

# Expose port 53 for DNS service
EXPOSE 53

# Start Dnsmasq as the entrypoint
ENTRYPOINT ["dnsmasq", "-k"]
