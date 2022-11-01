import random,socket

class Critto:
    def __init__(self):self.chiave ="" 
    def creaChiaveCasuale(self,dim): self.chiave =  "".join(chr(random.randint(0,256)) for x in range(dim))
    def impostaChiave(self,chiave): self.chiave = chiave
    def crittografaSoloLettere(self,stringa):
        crittografato = ""
        for k,lettera in enumerate(stringa):
            crittografato+= chr(((ord(self.chiave[k])-97) + (ord(lettera)-97))%26 + 97)
        return crittografato
    def decrittografaSoloLettere(self,stringa):
        decrittografato = ""
        for k,lettera in enumerate(stringa):
            decrittografato+= chr(((ord(lettera)-97) - (ord(self.chiave[k])-97))%26 + 97)
        return decrittografato
    def crittografaAscii(self,stringa):
        crittografato = ""
        for k,lettera in enumerate(stringa):
            crittografato+= chr((ord(self.chiave[k]) + ord(lettera))%256)
        return crittografato
    def decrittografaAscii(self,stringa):
        decrittografato = ""
        for k,lettera in enumerate(stringa):
            decrittografato+= chr((ord(lettera) - ord(self.chiave[k]))%256)
        return decrittografato
#cifrario di vernam ord() -->da char a numero, chr() -->da numero a carattere
parola,crittografato,decrittografato = "buongiorno","",""

def main():
    critto = Critto()
    critto.impostaChiave("itisdelpozzo")
    print(critto.crittografaSoloLettere("ciao"))
    print(critto.decrittografaSoloLettere(critto.crittografaSoloLettere("ciao")))

if __name__ == "__main__":
    main()

