from json import JSONEncoder
import json


class Pessoa:
    def __init__(self, nome, snome, idade):
        self.nome = nome
        self.sobrenome = snome
        self.idade = idade

    def __str__(self):
        return f'{self.nome} {self.sobrenome}, {self.idade}'


def encode_pessoa(obj):
    if isinstance(obj, Pessoa):
        return {'nome': obj.nome, 'sobrenome': obj.sobrenome,
                'idade': obj.idade, obj.__class__.__name__: True}
    else:
        raise TypeError(
            f'Object of type {obj.__class__.__name__} is not JSON serializable')


user = json.dumps(Pessoa('João', 'Silva', 25), default=encode_pessoa)
print(user)


class PessoaEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Pessoa):
            return {'nome': obj.nome, 'sobrenome': obj.sobrenome,
                    'idade': obj.idade, obj.__class__.__name__: True}
        else:
            return JSONEncoder.default(self, obj)


user = json.dumps(Pessoa('João', 'Silva', 25), cls=PessoaEncoder)
print(user)

#

# with open('py.json', 'r') as f:
#     person = json.load(f)
#     print(person)

# with open('py.json', 'w') as f:
#     json.dump(person, f, indent=4, sort_keys=True)
# person = {
#     "firstName": "Kathleen", "lastName": "Hernandez",
#     "locations": ["Palo Alto", "white house", "San Francisco"], "age": 25,
#     "social_media": 3, "accounts": [
#         {"site": "Facebook", "user": "Kathleen", "password": "jubleu5463"},
#         {"site": "Twitter", "user": "Kathleen", "password": "kathdan32!"},
#         {"site": "Instagram", "user": "Kathleen", "password": "kathleen_hernandez"}]
# }
# person_py = json.dumps(person, indent=4, sort_keys=True)
# print(person_py)
# person = json.loads(person_py)
# print(person)
