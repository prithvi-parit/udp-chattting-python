import socket
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def send():
    i=0
    while i==0:
     y=input("type to send server:")
     s.sendto(y.encode(),("192.168.43.223",1234))


def receive():
    ip="192.168.43.231"

    port=1234
    s.bind((ip,port))

    print("client ready")
    b=0
    while b==0:
     x=s.recvfrom(1024)
     print("server:", x)

x1=threading.Thread(target=send)
x2=threading.Thread(target=receive)

x2.start()
x1.start()
