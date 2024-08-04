import socket
s=socket.socket()
s.bind(("localhost",50))
print("server")
s.listen(5)
t=s.accept()
cs=t[0]
b=cs.recv(1024)
msg=b.decode()
print(msg)
cs.send(b'Hello Client')