class Animal:
    def __init__(self,nome:str,especie:str) -> None:
        self.__nome = nome
        self.__especie = especie

    def get_informacoes(self):
        print(f"Nome: {self.__nome} \n raça: {self.__especie}")

class Gato(Animal):
    def __init__(self, nome: str, raca: str,miar:str) -> None:
        super().__init__(nome, raca)
        self.__miar:str = miar

    def miau(self):
        self.__miar = "miau  miau"
        return self.__miar
class Cachorro(Animal):
    def __init__(self, nome: str, raca: str,latir:str) -> None:
        super().__init__(nome, raca)
        self.__latir = latir
    def latir(self):
        self.__latir = "au au"
        return self.__latir
