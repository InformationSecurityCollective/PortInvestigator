# Port Scanning Tool

This is a simple, yet effective, Port Scanning tool written in Python. The tool scans for open ports on a given host within a specified range and identifies the services running on those open ports. It's a handy utility for network diagnostics, security assessments, and understanding your network better.

## Dependencies

This script requires the following Python packages:
- `socket`
- `argparse`
- `pandas`
- `prettytable`
- `nmap`

Make sure to install them using pip:

pip install python-nmap pandas prettytable argparse

## How It Works

The `scan_ports` function is the core of this script. It takes two arguments: 
- `host`: The target host to scan.
- `port_range`: The range of ports to scan on the host.

The function creates an instance of `nmap.PortScanner()` and uses it to scan each port in the given range for the host. If a port is open, it is added to the `open_ports` list.

Then, for each open port, the script tries to identify the service using the `socket.getservbyport()` function. If the service cannot be identified, 'Unknown' is appended to the `services` list.

The script then uses `prettytable` to create a nicely formatted table of the open ports and their corresponding services, which is printed to the console. This table is also saved to an 'output.txt' file.

Finally, the user is asked whether they want to save the results to a CSV file. If the answer is 'yes', a `pandas` DataFrame is created from the open ports and services data, and this DataFrame is saved to an 'output.csv' file.

## Usage

To run the script, you need to provide the host and the start and end of the port range as command-line arguments:

python port_scanner.py <host> <start_port> <end_port>

For example, to scan ports 70 to 90 on localhost, you would run:

python port_investigator.py localhost 70 90
