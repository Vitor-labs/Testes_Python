from abc import ABC, abstractmethod


class Veiculo(ABC):
    __rodas = None
    lugares = None
    placa = None
    ano = None
    modelo = None
    cor = None

    def descricao(self):
        print("modelo: "+self.modelo +
              "\nano: "+str(self.ano) +
              "\ncor: "+self.cor +
              "\nplaca: "+self.placa)

    def dirigir(self):
        print("dirigindo...")

    def parar(self):
        print("...parando")
