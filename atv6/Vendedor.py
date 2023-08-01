from .Empregado import Empregado

class Vendedor(Empregado):
    def __init__(self, nome, salario, percentual_comissao):
        super().__init__(nome, salario)
        self.percentual_comissao = percentual_comissao

    def get_percentual_comissao(self):
        return self.percentual_comissao

    def set_percentual_comissao(self, percentual_comissao):
        self.percentual_comissao = percentual_comissao

    def calcular_salario(self):
        return self.salario + (self.salario * self.percentual_comissao / 100)

    def __str__(self):
        salario_com_comissao = self.calcular_salario()
        return f"{super().__str__()}, Salário com comissão: {salario_com_comissao}, Percentual de comissão: {self.percentual_comissao}"