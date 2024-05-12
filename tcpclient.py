import socket
host = "127.0.0.1"
port = 10000

cs = socket.socket()
cs.connect((host,port))
x='1'
while(x!='bye'):
    x = input("Enter client message: ")
    y = x.encode()
    cs.send(y)
    data = cs.recv(1024)
    z = data.decode()
    print(z)
cs.close()
