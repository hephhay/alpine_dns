# Docker Compose for Testing DNS Spoofing

This Docker Compose file defines three services: `alpine-dns`, `actual_server`, and `fake_server`. It can be used to test for DNS spoofing.

## Services

### alpine-dns

The `alpine-dns` service is built from the current directory and exposes port 53.

### actual_server

The `actual_server` service is built from the `./actual_server` directory and exposes port 80 within its container. It is connected to the internal network named `internal`.

### fake_server

The `fake_server` service is built from the `./fake_server` directory and exposes port 80 within its container. It is also connected to the internal network named `internal`.

## Networks

An internal network named `internal` is created as a custom bridge network for communication between the `actual_server` and `fake_server` services.

## Running and Testing

To run this Docker Compose file, use the `docker-compose up` command in the same directory as the file. To test for DNS spoofing from outside the container, try to resolve a domain name using the `alpine-dns` service and see if it returns the IP address of the `fake_server` instead of the `actual_server`.
