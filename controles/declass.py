class contador:
    def __init__(self, func):
        self.func = func
        self.valor = 0

    def __call__(self, *args, **kwargs):
        self.valor += 1
        print(f'Executado: {self.valor} vezes')
        return self.func(*args, **kwargs)


@contador
def olha_eu(nome):
    print(f'Olha eu, {nome}')


olha_eu('João')
olha_eu('Maria')
olha_eu('José')