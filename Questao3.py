class Conta :
    def __init__(self, nome, numero,Saldo):
        self.nome = nome
        self.numero= numero
        self.Saldo = Saldo
     
    def setnome(self, nome):
        self.nome= nome
     
    def setnumero(self, numero):
        self.numero = numero

    def setSaldo(self, Saldo):
        self.Saldo = Saldo   
     
    def getnome(self):
        return self.nome
         
    def getnumero(self):
        return self.numero

    def getSaldo(self):
        return self.Saldo


Brena = Conta('Brena',00.456,1000)
print(Brena.getnome())
print(Brena.getnumero())
print(Brena.getSaldo())

Brena.setnome('Aninha')
print(Brena.getnome())

Brena.setnumero(00.9998)
print(Brena.getnumero())

Brena.setSaldo(2000)
print(Brena.getSaldo())