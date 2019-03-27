import socket
import os

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

namafile="bart.png"
ukuran = os.stat(namafile).st_size

fp = open('bart.png','rb')
k = fp.read()
terkirim=0

for x in k:
   sock.connect((TCP_IP, TCP_PORT))
	sock.send(x)
	data = sock.recv(BUFFER_SIZE)
	terkirim = terkirim + 1
   print "\r terkirim {} of {} " . format(terkirim,ukuran)
   
sock.close()

print "received data:", data