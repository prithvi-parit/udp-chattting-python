import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def receive():


    ip="192.168.43.223"

    port=1234
    s.bind((ip,port))
    print("server ready")
    b=0
    while b==0:
     x=s.recvfrom(1024)
     print("client:", x)

def send():
     i=0
     while i==0:
      y=input("type to send server:")
      s.sendto(y.encode(),("192.168.43.231",1234))


x1=threading.Thread(target=send)
x2=threading.Thread(target=receive)

x2.start()
x1.start()
