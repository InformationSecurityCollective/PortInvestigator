import socket
import argparse
import pandas as pd
import prettytable as pt
import nmap

def scan_ports(host, port_range):
    open_ports = []
    nm = nmap.PortScanner()
    for port in port_range:
        res = nm.scan(host, str(port))
        res = res['scan'][host]['tcp'][port]['state']
        if res == 'open':
            open_ports.append(port)

    services = []
    for port in open_ports:
        try:
            service = socket.getservbyport(port)
            services.append(service)
        except:
            services.append('Unknown')

    tb = pt.PrettyTable()
    tb.field_names = ["Port", "Service"]
    for i in range(len(open_ports)):
        tb.add_row([open_ports[i], services[i]])
    print(tb)
    with open('output.txt', 'w') as file:
        file.write(str(tb))

    if input('Do you want to output the data to a CSV file? (yes/no): ').lower() == 'yes':
        df = pd.DataFrame(list(zip(open_ports, services)), columns=['Port', 'Service'])
        df.to_csv('output.csv', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Port Scanning Tool')
    parser.add_argument('host', help='Host to scan')
    parser.add_argument('start_port', type=int, help='Start of port range')
    parser.add_argument('end_port', type=int, help='End of port range')
    args = parser.parse_args()

    port_range = range(args.start_port, args.end_port + 1)
    scan_ports(args.host, port_range)
