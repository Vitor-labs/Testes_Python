from typing import overload
from veiculo import Veiculo


class Carro(Veiculo):

    porta_malas = None

    def __init__(self, placa, ano, modelo, cor, conteudo):
        self.porta_malas = conteudo
        self.__rodas = 4
        self.lugares = 5
        self.placa = placa
        self.ano = ano
        self.modelo = modelo
        self.cor = cor

    def descricao(self):
        print("\nLugares: "+str(self.lugares))
        super().descricao()
        print("no porta malas: "+self.porta_malas)

    def dirigir(self):
        print("dirigindo o carro...")
        return self

    def parar(self):
        print("...parando o carro")
        return self

    def pintar(self, cor):
        self.cor = cor


if __name__ == "__main__":
    carro = Carro("ABC1234", 1990, "monza", "verde", "malas")
    carro.dirigir().parar()
    carro.descricao()
    carro.pintar("rosa")
    print(carro.cor)
