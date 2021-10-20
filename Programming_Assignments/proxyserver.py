from socket import *
import sys
BUF_SIZE = 0x4000
HTTP_PORT = 80
HTTPS_PORT = 443
# if len(sys.argv) <= 1:
#     print('Usage : "python {} server_ip"\n[server_ip : It is the IP Address Of Proxy Server'.format(sys.argv[0]))
#     sys.exit(2)
address = str(sys.argv[1])
port = int(sys.argv[2])
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
# Fill in start.
tcpSerSock.bind((address, port))
tcpSerSock.listen(1)
# Fill in end.
while True:
    # Strat receiving data from the client
    print('Ready to listening on {}:{}'.format(address, port))
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from {}:{}'.format(address, port))
    message = tcpCliSock.recv(BUF_SIZE).decode()
    print(message)
    # Extract the filename from the given message
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    print(filetouse)
    try:# Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        # outputdata = f.readlines()
        outputdata = f.read()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
        # Fill in start.
        tcpCliSock.send(outputdata.encode())
        f.close()
        # Fill in end.
        print('Read from cache')
        # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.","",1)
            print(hostn)
            try:
                # Connect to the socket to port 80
                # Fill in start.
                c.connect((hostn, HTTP_PORT))
                # Fill in end.
                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                fileobj = c.makefile('r', 0)
                fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")
                # Read the response into buffer
                # Fill in start.
                buf = c.recv(BUF_SIZE).decode()
                # Fill in end.
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                tcpCliSock.send(buf.encode())
                tmpFile = open("./" + filename,"wb")
                # Fill in start.
                tmpFile.write(buf)
                tmpFile.close()
                # Fill in end.
            except:
                print("Illegal request")
        else:
            # HTTP response message for file not found
            # Fill in start.
            tcpCliSock.send("HTTP/1.0 404 FileNotFound\r\n\r\n".encode())
            with open('404.html', 'r')  as f:
                page = f.read()
            tcpCliSock.send(page.encode())
            # Fill in end.
        # Close the client and the server sockets
        tcpCliSock.close()
# Fill in start.
# Fill in end.