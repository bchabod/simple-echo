#!/usr/bin/python
import socket, sys

if (len(sys.argv) < 2):
	print "Client usage: python client.py SERVER_ADDR SERVER_PORT"
	sys.exit(0)

server = (sys.argv[1], int(sys.argv[2]))
print "Simple echo client is going to ping %s on port %s" % server

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.connect(server)

try:
	message = "GET /echo.php?message=hello+world HTTP/1.0\r\n\r\n"
	print "Sending message: %s" % message
	socket_obj.sendall(message)
	response = socket_obj.recv(4096)
	while response != "":
		print "Received chunk of data: %s" % response
		response = socket_obj.recv(4096)

finally:
	print "Disconnecting from server"
	socket_obj.close()
