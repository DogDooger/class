class Ingresso:
    def __init__(self,valor:float) -> None:
        self.__valor = valor

    def imprimirValor(self):
        print(f"Valor do ingresso: R${self.__valor:.2f}")

n1 = Ingresso(float(35.50))
n1.imprimirValor()