0. Justin Rhodes (jgr85), Greg Fuerte (grf27)

1. Within rs.py and ts.py, we initially instantialized a dictionary and populated it as we parsed through the PROJI-DNSRS.txt and PROJI-DNSTS.txt files respectively. These dictionaries will be used to look up the information for the hostnames throughout the program. Afterwards, rs.py and ts.py will both establish server sockets and waits for a connection from the client program using the user inputted port number.

When client.py is run, it uses the given port numbers to establish a connection with the rs server. It then reads the hostnames within PROJI-HNS.txt and for each host name, it sends the hostname as a query to the rs server where if found within the rs dns dictionary, it will send the IP address and the flag back to the client,  otherwise "NF:<hostname>" if not found.

If the IP address and the flag is returned back to the client, it writes the hostname as well as its IP address and flag into the RESOLVED.txt file. If the hostnames are not found within the rs dns dictionary, that is when the client will establish a connection to the ts server. There, it will do the same process where it will send the hostname as a query to the ts server, the ts server will then look up the hostname within its respective dns dictionary and return back the information of the hostname if not, otherwise an "Error:HOST NOT FOUND" message if not found. No matter the results, the client will write the result into the RESOLVED.txt file.

2. Currently, there are no known issues or bugs in our attached code.

3. We initially had some confusion about whether case sensitivity would play a part within the hostnames along with what was the proper approach to connecting to the ts server after a hostname was not found within the rs server. However, we were able to quickly solve these issues as well as any misunderstandings we incurred. 

4. This project was a good refresher of how sockets are used to connect clients and servers to each other. And this project served as a good introduction to python programming and it uses it especially since compared to Java or C, we're much less experienced with programming using Python. Overall, we were able to see how the abstract idea of DNS interacts with each other and the client through our code.
