import threading
import time
import random
import sys
import socket

dns = {}

file = open("PROJI-DNSTS.txt", "r")
for i in file:
    arr = i.split()
    temp = arr[0]
    arr[0] = arr[0].lower()
    dns[arr[0]] = temp + ' ' + arr[1] + ' ' + arr[2]

#print(dns)
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
while True:
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    # send a intro message to the client.  
    msg = "Successfully connected, waiting for query..."
    csockid.send(msg.encode('utf-8'))

    lenHost = csockid.recv(100)
    if lenHost == "DONE!":
        csockid.close()
        print("[S]: Finished querying, goodbye...")
        exit()

    lenHost = int(lenHost)
    csockid.send("success")
    query = csockid.recv(lenHost)
    csockid.send("success")
    csockid.recv(100)

    result = ""

    if query.lower() in dns:
        result = dns[query.lower()]
        #print(result)
    else:
        result = query + " - Error:HOST NOT FOUND"
        #print(result)

    resLength = str(len(result))
    csockid.send(resLength)
    csockid.recv(100)
    csockid.send(result)
    csockid.recv(100)
    print("[S]: Done!")

# Close the server socket

exit()