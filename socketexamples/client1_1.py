# client.py

#importing socket module
import socket

# creating socket instance
client_object = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# target ip address and port
ip_address = '127.0.0.1'
port = 5555

# instance requesting for connection to the specified address and port
client_object.connect((ip_address,port))

# receiving response from server
data_receive = client_object.recv(1024)

# if response is not null
if data_receive:
    # Connection is successful
    print("CLIENT CONNECTED TO SERVER")
    print(data_receive.decode('utf-8'))


    while data_receive:
        # user input
        client_input = input().encode('utf-8')

        # sending request to the server
        client_object.send(client_input)

        # receiving response from the server
        data_receive = client_object.recv(1024)
        if data_receive:
            print("{}: {}".format("SERVER",data_receive.decode('utf-8')))
