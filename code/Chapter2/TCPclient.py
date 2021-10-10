import socket
serverHostName = "localhost"
serverPort = 2333
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverHostName, serverPort))
while(True):
    msg = input("lowercase:")
    clientSocket.send(msg.encode('utf-8'))
    if(msg == "stop"):
        print("Connection closed.")
        print("Server stopped.")
        break
    if(msg == "disconnect"):
        print("Connection closed.")
        break
    recv_msg = clientSocket.recv(2048).decode('utf-8')
    print("Receved message '{}' from {}:{}".format(recv_msg, serverHostName, serverPort))
clientSocket.close()