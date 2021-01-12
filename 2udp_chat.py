import socket
import os
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system("clear")
sip = input("Type Sender's IP: ")
sport = int(input("Type Sender's Port: "))
rip = input("Type Receiver's IP: ")
rport = int(input("Type Receiver's Port: "))
s.bind((sip, int(sport)))
print("\n")
os.system("tput setaf 6")
print("\t\t Welcome to Chat App")
print("\t .................................. \n")
os.system("tput setaf 7")

#send
def send():
    while True:
        msg = input()
        s.sendto(msg.encode(), (rip, rport))
        if "Bye" in msg or "bye" in msg or "exit" in msg:
             os.system("tput setaf 6")
             print("\t\t\t Chat Over \n")
             os.system("tput setaf 7")      
             os._exit(1)

def receive():
    while True:
        msg = s.recvfrom(1024)
        os.system("tput setaf 3")
        print(" \t\t\t\t\t " + msg[0].decode())
        os.system("tput setaf 7")
        if "Bye" in msg[0].decode() or "bye" in msg[0].decode() or "exit" in msg[0].decode():
             os.system("tput setaf 6")
             print("\t\t\t Chat Over \n")
             os.system("tput setaf 7")      
             os._exit(1)

t1 = threading.Thread(target=send)
t2 = threading.Thread(target=receive)

t1.start()
t2.start()
