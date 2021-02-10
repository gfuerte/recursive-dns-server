import threading
import time
import random
import sys
import socket

dns = {}
tsHost = ""
file = open("PROJI-DNSRS.txt", "r")
for i in file:
    arr = i.split()
    temp = arr[0]
    arr[0] = arr[0].lower() 
    if arr[1] == '-':
        tsHost = arr[0]
    else:
        dns[arr[0]] = temp + ' ' + arr[1] + ' ' + arr[2]

#print(tsHost)
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

#Amount of queries to be run
msg = csockid.recv(100)
count = int(msg)
csockid.send("success")

print("[S]: Processing client request, sending info on queries...")
#Begin to recieve queries from client and check in table
for x in range(count):
    msg = csockid.recv(100)
    csockid.send("success")
    #print(msg)
    msgLen = int(msg)
    msg = csockid.recv(msgLen)
    csockid.send("success")
    #print(msg)
    csockid.recv(100)
    result = ""

    if msg.lower() in dns:
        result = dns[msg.lower()]
    else: #We should probably just say "not found", then have a thread lookup in the TS server so all searches are in the order of their request
        result = "NF:{}".format(tsHost)

    resultLength = str(len(result))
    csockid.send(resultLength.encode('utf-8'))
    csockid.recv(100)
    csockid.send(result)


print("[S]: Done!")
# Close the server socket
ss.close()
exit()
