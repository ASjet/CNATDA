#import socket module
from socket import *
import sys # In order to terminate the program
BUF_SIZE = 0x4000
port = int(sys.argv[1])
serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
try :
    #Fill in start
    serverSocket.bind(('', port))
    #Fill in end
    serverSocket.listen(1)

    while True:

        #Establish the connection
        print("Listening on {}".format(port))

        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(BUF_SIZE).decode('utf-8')

            filename = message.split()[1]

            f = open(filename[1:],'r')

            outputdata = f.read().split('\n')
            f.close()
            #Send one HTTP header line into socket
            header = "HTTP/1.1 200 OK\r\n\r\n"
            #Send the content of the requested file to the client
            content = ""
            for l in outputdata:
                content += l + "\r\n"
            resp = header + content + '\r\n'
            connectionSocket.send(resp.encode('utf-8'))
        except IOError:
            #Send response message for file not found
            header = "HTTP/1.1 404 NotFound\r\n\r\n"
            content = ""
            with open("404.html", 'r') as f:
                for l in f.read().split('\n'):
                    content += l + '\r\n'
            resp = header + content + '\r\n'
            connectionSocket.send(resp.encode('utf-8'))
        #Close client socket
        connectionSocket.close()
except OSError:
    serverSocket.close()
    sys.exit()
#Terminate the program after sending the corresponding data