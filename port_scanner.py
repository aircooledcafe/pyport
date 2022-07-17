# port scanner
import socket
from threading import Thread
# from port_dictionary import common_ports
from port_descriptions import common_ports

# ask user fo an ip address to scan
print("Please input an IP address to scan:")
ip_address = input("> ")

results = []

# function to try and connect to a port on to see if it is open
def scanner(ip, p):
    result = client_socket.connect_ex((ip, p))
    # if result is 0 (the response code for a connection established) 111 for closed port
    if result == 0:
        # print("Port: " + str(p) + " Open")
        results.append(p)

# function to pull a brief definition from a dictionary of common ports and create a string
# to advice the user on the ports normal use case
def definition(scan_port):
    definition_string = str(scan_port) + " - "
    for i in range(0, len(common_ports)):
        # print(common_ports[i])
        if scan_port == common_ports[i]['Port']:
            definition_string = definition_string + common_ports[i]['Description']
    print(definition_string)

# function to itterate through a range of ports and create a socket to conect to
for port in range(1, 1080):
    # set up a socket for ipv 4 on tcp
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Creates new thread fro each scan to imporve performance
    new_thread = Thread(target=scanner, args=((ip_address, port)))
    new_thread.start()
    # close the socket on completion of scan
    client_socket.close()

# itterate through the results of the scan and provide some defintions of common uses for
# the open ports
if len(results) > 0:
    print("IP address " + ip_address + " has the following open ports:")
    for item in results:
        definition(item)      
else:
    print("All ports are closed.")



