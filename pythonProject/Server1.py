import socket
s=socket.socket()
s.bind(("localhost",60))
print("server")
s.listen(5)
t=s.accept()
cs=t[0]
print("connection")