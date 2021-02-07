import threading
import time
import random
import sys
import socket


def sendQueries(queries,sock):
    file = open("RESOLVED.txt","w")
    #Need to send amount of items to be queried, then length of item, then item
    print("[C]: Sending number of queries...")
    qLength = len(queries)
    #print("Length {}".format(qLength))
    sock.send(str(qLength).encode('utf-8'))
    sock.recv(100)
    print("[C]: Sending over queries, populating RESOLVED.txt with query results...")
    for item in queries:
        msg = str(len(item))
        sock.send(msg.encode('utf-8'))
        sock.recv(100)
        sock.send(item.encode('utf-8'))
        sock.recv(100)
        sock.send("ready")

        resultLength = int(sock.recv(100))
        sock.send("ready")
        result = sock.recv(resultLength)
        file.write(result + "\n")


# works with other servers
if len(sys.argv) < 4:
    print(
        "Invalid port number, please use the following to start the server: python client.py <rsHostname> <rsListenPort> <tsListenPort>")
    exit()

rsHost = sys.argv[1]
rsPort = int(sys.argv[2])
tsPort = int(sys.argv[3])

#Read in hostnames to be queried
file = open("PROJI-HNS.txt", "r")
toQuery = file.read().splitlines()
#print(toQuery)
file.close()

# Establish client/server connection
try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# Define the port on which you want to connect to the server
localhost_addr = socket.gethostbyname(socket.gethostname())

# connect to the server on local machine
server_binding = (rsHost, rsPort)
cs.connect(server_binding)

# Receive data from the server
data_from_server = cs.recv(100)
print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

sendQueries(toQuery,cs)

# close the client socket
cs.close()
exit()
