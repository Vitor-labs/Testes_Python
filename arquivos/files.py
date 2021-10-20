import os
import shutil

try:
    file = input("digite o nome do arquivo: ")+".txt"
    arquivo = open(file, 'a')
    caminho = str(os.path.abspath(file))

    if os.path.exists(caminho):
        print("arquivo criado")
    else:
        print("arquivo não criado")

    with open(file, 'w') as file:
        text = input("digite algo para escrever:\n")
        file.write(text)

except FileNotFoundError as exc:
    print(str(exc))
