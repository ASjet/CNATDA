import time
# import socket
from socket import *
import sys

BUF_SIZE = 0x400
timeout = 1.0
address = str(sys.argv[1])
port = int(sys.argv[2])
# address = "localhost"

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(timeout)

for i in range(10):
    msg = "Ping {} {}".format(i, time.time())
    try:
        clientSocket.sendto(msg.encode(),(address, port))
        # start = time.process_time_ns()
        start = time.time_ns()
        recvmsg, serveraddr = clientSocket.recvfrom(BUF_SIZE)
        # end = time.process_time_ns()
        end = time.time_ns()
        rtt = (end - start) / 10e6
        recvmsg = recvmsg.decode()
        print("{} bytes from {}:{} RTT={:.3} ms".format(len(recvmsg), serveraddr[0], serveraddr[1], rtt))
    except OSError:
        print("Timeout")
