class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
     
    def setNome(self, nome):
        self.nome = nome
     
    def setsalario(self, salario):
        self.salario = salario
     
    def getNome(self):
        return self.nome
         
    def getsalario(self):
        return self.salario




Brena = Funcionario('Brena',679)
print(Brena.getNome())
print(Brena.getsalario())

Brena.setsalario(456)
print(Brena.getsalario())


Aninha= Funcionario('Aninha',345)
print(Aninha.getNome())
print(Aninha.getsalario())

Aninha.setsalario(780)
print(Aninha.getsalario())