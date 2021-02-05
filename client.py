import threading
import time
import random
import sys
import socket

if (len(sys.argv) < 4):
    print("Invalid port number, please use the following to start the server: python client.py <rsHostname> <rsListenPort> <tsListenPort>")
    exit()

rsHost = sys.argv[1]
rsPort = int(sys.argv[2])
tsPort = int(sys.argv[3])
#Establish server socket

#Establish client/server connection
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
data_from_server=cs.recv(100)
print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

# close the client socket
cs.close()
exit()