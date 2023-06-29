from atv3.Ingresso import Ingresso

class VIP(Ingresso):
    def __init__(self,valorAdd:float) -> None:
        self.__valorAdd = valorAdd

    def imprimirValor(self,valor:float):
        return super().imprimirValor()
        print(f"valor: R${self.__valorAdd:.2f}")

f1 = VIP(float(40.00))
f1.imprimirValor()        