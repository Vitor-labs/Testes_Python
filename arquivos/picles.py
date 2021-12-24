import pickle
# yes, he turned out to be a pickle


def barra(func):
    def wrapper(*args, **kwargs):
        print('\n' + '*' * 30)
        func(*args, **kwargs)
    return wrapper


class Pessoa():
    def __init__(self, nome, idade, inf):
        self.nome = nome
        self.idade = idade
        self.inf = inf

    @barra
    def __str__(self):
        print(f'{self.nome} tem {self.idade} anos.')
        for k, v in self.inf.items():
            print(f'{k}: {v}')

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__ = state


gerald = Pessoa('Gerald', 20, {'altura': 1.80,
                               'peso': 80, 'cor': 'branco', 'sexo': 'M'})
# gerald.__str__()

serialized = pickle.dumps(gerald)
with open('gerald.pkl', 'wb') as f:
    f.write(serialized)

with open('gerald.pkl', 'rb') as f:
    gerald_serialized = f.read()

gerald_deserialized = pickle.loads(gerald_serialized)
gerald_deserialized.__str__()
