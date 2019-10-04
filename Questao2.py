class Retangulo:
    def __init__(self, Base, Altura):
        self.Base = Base
        self.Altura = Altura
     
    def setBase(self, Base):
        self.Base = Base
     
    def setAltura(self, Altura):
        self.Altura = Altura
     
    def getBase(self):
        return self.Base
         
    def getAltura(self):
        return self.setAltura

Local = int(input("Digite as medidas de um local: ? "))
perimetro  = 2*(Base + Altura)
area = Base*Altura
print("perimetro:", perimetro, "-", " area:", area)




Medidas= Retangulo(456 ,300)
print(Medidas.getBase())
print(Brena.getAltura())



