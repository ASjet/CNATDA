import socket
serverPort = 2333
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server listening on port {}".format(serverPort))
while(True):
    connectionSocket, addr = serverSocket.accept()
    print("Connection with {}:{} established".format(addr[0], addr[1]))
    while(True):
        recv_msg = connectionSocket.recv(2048).decode('utf-8')
        print("Receved message '{}'".format(recv_msg))
        if(recv_msg == "disconnect" or recv_msg == "stop"):
            break
        connectionSocket.send(recv_msg.upper().encode('utf-8'))
    connectionSocket.close()
    print("Connection closed.")
    if(recv_msg == "stop"):
        break
print("Server stopped.")
serverSocket.close()