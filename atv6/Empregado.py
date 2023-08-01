class Empregado:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario
    def __str__(self):
        return f"Nome: {self.nome}, Salário: {self.salario}"