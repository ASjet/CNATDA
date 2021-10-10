import socket
serverPort = 2333
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("Server listening on port {0}".format(serverPort))
while(True):
    msg, client_addr = serverSocket.recvfrom(2048)
    msg = msg.decode('utf-8')
    print("Receved message: '{}' from {}:{}".format(msg,client_addr[0],client_addr[1]))
    if(msg == "stop"):
        break
    mod_msg = msg.upper()
    serverSocket.sendto(mod_msg.encode('utf-8'),client_addr)
print("Server stoped")
serverSocket.close()
