import socket
from threading import Thread

dizioConnection = {}

server_s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_s.bind(("0.0.0.0",5000))
server_s.listen()

def letturaFilePerNome():
    f = open("dati.txt","r")
    righe = f.readlines()
    f.close()
    dizio={}
    for x in righe[1:]:
        nomeIP = x.split(",")
        dizio[nomeIP[0]] = nomeIP[1]
    return dizio

class myThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True
    def run(self):
        while self.running:
            print("In attesa di connessione...")
            connection, address = server_s.accept()
            dizioConnection[address[0]] = connection
            print("connessione stabilita")
            t = myThread()
            t.start()
            while True:
                dizio = letturaFilePerNome()
                dati = connection.recv(4096).decode().split("|")
                print(f"{dati[0]}  {dati[1]}")
                if dati[1] in dizio.keys():
                    print(dizio[dati[1]])
                    dizioConnection[dizio[dati[1]]].sendall(dati[0].encode())
    def stop(self):
        self.running = False

def main():
    t = myThread()
    t.start()

if __name__ == "__main__":
    main()