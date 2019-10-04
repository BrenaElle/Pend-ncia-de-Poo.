class Carro:
    def __init__(self,combustivel,ObterGasolina,adicionarGasolina):
      self.ObterGasolina = ObterGasolina
      self.adicionarGasolina = adicionarGasolina
      self.combustivel = combustivel


    def getObterGasolina(self):
        return self.ObterGasolina

    def getadicionarGasolina(self):
        return self.adicionarGasolina

    def andar(self, km):
        self.combustivel = (km-self.combustivel)
        print(self.combustivel)
         
    def adicionarGasolina(self,combustivel):
        self.combustivel += self.combustivel
        print(self.combustivel)



 