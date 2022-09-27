import random
import socket
chiave = "biboplayer"

def crittografa(stringa):
    for k,lettera in enumerate(stringa):
        crittografato+= chr(((ord(chiave[k])-97) + (ord(lettera)-97))%26 + 97)
    return crittografato

def decrittografa(stringa):
    decrittografato = ""
    for k,lettera in enumerate(stringa):
        decrittografato+= chr(((ord(lettera)-97) - (ord(chiave[k])-97))%26 + 97)
    return decrittografato

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0",5000))
dati,ind = s.recvfrom(4096)
print(decrittografa(dati.decode()))

#cifrario di vernam ord() -->da char a numero, chr() -->da numero a carattere
parola,crittografato,decrittografato = "buongiorno","",""


#chiave = "".join(chr(random.randint(0,256)) for x in range(24))

#versione in cui la crittografia avviene su tutto il codice ascii
"""for k,lettera in enumerate(parola):
    crittografato+= chr((ord(chiave[k]) + ord(lettera))%256)
print(crittografato)

for k,lettera in enumerate(crittografato):
    decrittografato+= chr((ord(lettera) - ord(chiave[k]))%256)
print(decrittografato)"""

#versione in cui la crittografia avviene sono con le lettere dell' alfabeto
