import json
import os


class Inventory:
    pets = {}

    def __init__(self):
        self.load_inventory()

    def add_item(self, name, qtd):
        quantity = 0
        if name in self.pets:
            valor = self.pets[name]
            quantity = valor + qtd
        else:
            quantity = qtd
        self.pets[name] = quantity
        print('Adicionado {} {}: Total: {}'.format(qtd, name, self.pets[name]))

    def get_items(self):
        return self.items

    def show_inventory(self):
        for key, value in self.pets.items():
            print('{} = {}'.format(value, key))

    def remove(self, name, qtd):
        quantity = 0
        if name in self.pets:
            valor = self.pets[name]
            quantity = valor - qtd
        if quantity < 0:
            print('Esgotado: {} {}'.format(qtd, name))
            quantity = 0
        self.pets[name] = quantity
        print('Removido {} {}: Total: {}'.format(qtd, name, self.pets[name]))

    def load_inventory(self):
        print('Carregando inventário...')
        if os.path.isfile('inventory.json'):
            print('Inventário encontrado!')
            with open('inventory.json', 'r') as f:
                self.pets = json.load(f)
        else:
            print('Inventário não encontrado!')
            self.pets = {}
            return
        print('Inventário carregado!')

    def save_inventory(self):
        print('Salvando inventário...')
        with open('inventory.json', 'w') as f:
            json.dump(self.pets, f)
        print('Inventário salvo!')


def main():
    inventory = Inventory()
    while True:
        print('\nInventário')
        print('1 - Adicionar item')
        print('2 - Remover item')
        print('3 - Mostrar inventário')
        print('4 - Salvar inventário')
        print('5 - Sair')
        opcao = input('Opção: ')
        if opcao == '1' or opcao == '2':
            name = input('Nome do item: ')
            qtd = int(input('Quantidade: '))
            if opcao == '1':
                inventory.add_item(name, qtd)
            if opcao == '2':
                inventory.remove(name, qtd)
        elif opcao == '3':
            inventory.show_inventory()
        elif opcao == '4':
            inventory.save_inventory()
        elif opcao == '5':
            break
        else:
            print('Opção inválida')

    inventory.save_inventory()


if __name__ == '__main__':
    main()
