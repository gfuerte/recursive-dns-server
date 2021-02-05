import threading
import time
import random
import sys
import socket

dns = {}

file = open("PROJI-DNSRS.txt", "r")
for i in file:
    arr = i.split()
    if arr[0] == 'localhost':
        dns['localhost'] = 'NS'
    else:
        dns[arr[0]] = arr[1] + ' ' + arr[2]

print(dns)
file.close()

#works with other servers
if len(sys.argv) < 2:
    print("Invalid port number, please use the following to start the server: python ts.py <PORT_NUM>")
    exit()

portNum = int(sys.argv[1])
#Establish server socket
try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', portNum)
ss.bind(server_binding)
ss.listen(1)
host = socket.gethostname()
print("[S]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[S]: Server IP address is {}".format(localhost_ip))
csockid, addr = ss.accept()
print ("[S]: Got a connection request from a client at {}".format(addr))

# send a intro message to the client.  
msg = "Successfully connected, waiting for queries..."
csockid.send(msg.encode('utf-8'))


# Close the server socket
ss.close()
exit()