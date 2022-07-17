# testing file import
# file = open("port_dictionary.py", "r")
from port_dictionary import common_ports
print(common_ports[0]['Port'])

test_port = 80

for item in common_ports:
    if int(item['Port']) == test_port:
        print(item['Description'])  

