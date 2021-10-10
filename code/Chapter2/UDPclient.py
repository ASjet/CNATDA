import socket
serverHostName = "vpshk.itfs127.com"
serverPort = 2333
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while(True):
    msg = input("lowercase:")
    clientSocket.sendto(msg.encode('utf-8'),(serverHostName,serverPort))
    if(msg == 'stop'):
        break
    recv_msg, recv_addr = clientSocket.recvfrom(2048)
    print("Receved message '{}' from {}:{}".format(recv_msg.decode('utf-8'),recv_addr[0],recv_addr[1]))
print("Server stoped.")
clientSocket.close()