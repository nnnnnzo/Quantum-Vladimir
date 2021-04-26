import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

 

# Bind and listen

serverSocket.bind(("0.0.0.0",9093));

serverSocket.listen();
(clientConnected, clientAddress) = serverSocket.accept();


# Accept connections

while(True):
   

    dataFromClient = clientConnected.recv(1024)

    print(dataFromClient.decode());
