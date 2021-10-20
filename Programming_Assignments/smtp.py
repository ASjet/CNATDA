from socket import *
import sys

username = "aw@aw.net"
destname = "sjet@raspi.net"
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
smtp_port = 25

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = sys.argv[1]

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, smtp_port))
#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '220'):
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if (recv1[:3] != '250'):
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailCommand = "MAIL FROM: " + username + '\r\n'
clientSocket.send(mailCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if (recv2[:3] != '250'):
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptCommand = "RCPT TO: " + destname + '\r\n'
clientSocket.send(rcptCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if (recv3[:3] != '250'):
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if (recv4[:3] != '354'):
    print('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
message = msg + '\r\n'
clientSocket.send(message.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if (recv5[:3] != '250'):
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send("quit\r\n".encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if (recv6[:3] != '221'):
    print('221 reply not received from server.')
# Fill in end

clientSocket.close()