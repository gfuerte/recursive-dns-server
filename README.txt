0. Justin Rhodes (jgr85), Greg Fuerte (grf27)

1. Within rs.py and ts.py, we initially instantialized a dictionary and populated it as we parsed through the PROJI-DNSRS.txt and PROJI-DNSTS.txt files respectively. These dictionaries will be used to look up the information for the hostnames throughout the program. Afterwards, rs.py and ts.py will both establish server sockets and waits for a connection from the client program using the user inputted port number.

When client.py is run, it uses the given port numbers to establish a connection with the rs server. It then reads the hostnames within PROJI-HNS.txt and for each host name, it sends the hostname as a query to the rs server where if found within the rs dns dictionary, it will send the IP address and the flag back to the client,  otherwise "NF:<hostname>" if not found.

If the IP address and the flag is returned back to the client, it writes the hostname as well as its IP address and flag into the RESOLVED.txt file. If the hostnames are not found within the rs dns dictionary, that is when the client will establish a connection to the ts server. There, it will do the same process where it will send the hostname as a query to the ts server, the ts server will then look up the hostname within its respective dns dictionary and return back the information of the hostname if not, otherwise an "Error:HOST NOT FOUND" message if not found. No matter the results, the client will write the result into the RESOLVED.txt file.

Once RESOLVED.txt is written, all the python programs close, and are able to be started back up immediately for other test cases. We chose to implement it like this because once the client finishes querying, there is no work left to be done, and we are only using one client. This just makes the implementation easier, and also makes the programs easier to test.

2. Currently, there are no known issues or bugs in our attached code.

3. We initially had some confusion about whether case sensitivity would play a part within the hostnames along with what was the proper approach to connecting to the ts server after a hostname was not found within the rs server. We were able to compare the hostnames in each table by setting each one to the lower case form of the word, if these two matched, we would return how it appeared on the server side table, otherwise, it would return the requested hostname by the client. In order to connect to the TS server, we simply just made another socket designated for that server, and whenever we needed to connect, we use that socket. Another issue we ran into is that the RS server could not immediately start back up after being closed. This was actually a bug that was a result of some leftover data being held in the socket stream, and we fixed it by recieving (recv) the rest of the data, which allowed the socket to close properly, allowing us to instantly run the servers again.

4. This project was a good refresher of how sockets are used to connect clients and servers to each other. And this project served as a good introduction to python programming and it uses it especially since compared to Java or C, we're much less experienced with programming using Python. Overall, we were able to see how the abstract idea of DNS interacts with each other and the client through our code.

To Run Use Command Lines:
python ts.py tsListenPort
python rs.py rsListenPort
python client.py rsHostname rsListenPort tsListenPort

This zip file should include:
client.py
rs.py
ts.py
README.txt
