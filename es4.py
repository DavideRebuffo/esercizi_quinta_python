from threading import Thread
import datetime
#dato un numero intero dato dal prodotto di 2 primi trovare i numeri primi
f = open("C:\\Users\\Client\\Desktop\\SHULKER BOX\\SCUOLA\\5a\\TPSIT\\PYTHON\\primiMinori.txt","r")
lista = f.readlines()
f.close()
listaDivisa = [int(str(cella[:-1])) for cella in lista]
"""
def isPrimo(numero):
    ok = True
    rovescio = numero-1    
    while (ok == True) & (rovescio > 1):
        if numero % rovescio == 0:
            ok = False
        rovescio-=1
    if rovescio == 0:
        ok = False
    return (ok)"""

def primiMinoriTot():
    f = open("./primiMinori.txt","w")
    for k in range(10000000):
        if isPrimo(k):
            f.write(f"{k}\n")
    f.close()

class MyThread(Thread):
    def __init__(self,lista,num):
        Thread.__init__(self)
        self.lista = lista
        self.num = num
        self.ferma = False
    def run(self):
        while not self.ferma:
            for cella in self.lista:
                perc = self.num / cella
                if cella * int(perc) == self.num:
                    if int(perc) in listaDivisa:
                        print(f"i numeri sono: {cella} e {int(perc)}")
                        self.ferma = True
                        break
    def stop(self):
        self.ferma = True
        print("mi fermo")

def main():
    numero = 39325441
    nThread = 6
    inizio = datetime.datetime.now().microsecond
    listaDiListe= []    
    num = len(listaDivisa) // nThread
    for k in range(1,nThread):
        if k == 1: listaDiListe.append(listaDivisa[0:num])
        if k != 1 and k != nThread:
            listaDiListe.append(listaDivisa[num:num + num])
            num = num + num
        else: listaDiListe.append(listaDivisa[num:])
    listaThread = [MyThread(cella,numero) for cella in listaDiListe]
    for cella in listaThread:
        cella.start()
    n = True
    while n:
        for cella in listaThread:
            if cella.ferma:
                for t in listaThread:
                    t.stop()
                    t.join()
                break
        fine = datetime.datetime.now().microsecond
        break
    print(f"il programma ha elaborato in {(inizio - fine)/1000} millisecondi")

if __name__ == "__main__":
    main()