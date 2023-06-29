class Animal:
    def __init__(self,nome,especie) -> None:
        self.__nome = nome
        self.__especie = especie
    def dormir(self):
        print('Zzz...')
n1 = Animal("Cachorro","Canino")
n1.dormir()        