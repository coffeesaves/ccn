import socket

host = "127.0.0.1"
port = 10000

ss=socket.socket()
ss.bind((host,port))
ss.listen()

conn,addr = ss.accept()
print("connection successfull")
x="1"
while(x!="bye"):
    x=(conn.recv(1024)).decode()
    print(x)
    y=input("enter data:")
    data=y.encode()
    conn.send(data)
conn.close()
