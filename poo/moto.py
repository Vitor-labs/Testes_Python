from typing import overload
from veiculo import Veiculo


class moto(Veiculo):
    def __init__(self, placa, ano, modelo, cor):
        self.__rodas = 2
        self.lugares = 2
        self.placa = placa
        self.ano = ano
        self.modelo = modelo
        self.cor = cor

    def descricao(self):
        print("\nLugares: "+str(self.lugares))
        super().descricao()

    def dirigir(self):
        print("dirigindo a moto...")
        return self

    def parar(self):
        print("...parando a moto")
        return self

    def pintar(self, cor):
        self.cor = cor


if __name__ == "__main__":
    moto = moto("AEIO109", 2012, "150", "azul")
    moto.descricao()
    moto.dirigir().parar()
    moto.pintar("rosa")
    print(moto.cor)
