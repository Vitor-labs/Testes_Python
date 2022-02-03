from sre_constants import SUCCESS
from rich.console import Console
from rich.text import Text
#from rich.table import Table
from rich.theme import Theme
from rich import print

tema = Theme({"SUCCESS": "green", "FAIL": "bold red"})
console = Console(theme=tema)


class error(RuntimeError):
    def __init__(self, message):
        self.message = message


def calcimc(peso, altura):
    imc = peso/(altura * altura)
    avaliaResult(imc)
    return imc


def avaliaResult(result):
    text = Text("")
    if result < 18:
        text.append("Você está abaixo do peso", style="FAIL")
        console.print(text)
    elif result < 26:
        text.append("Você está no peso ideal", style="SUCCESS")
        console.print(text)
    else:
        text.append("Você está acima do peso", style="FAIL")
        console.print(text)


altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

try:
    assert(altura > 0)
    assert(peso > 0)

    result = str(calcimc(peso, altura))

except AssertionError:
    print('Altura ou peso inválido')
except ZeroDivisionError as exc:
    print(str(exc)+" Digite apenas valores acima de 0")
except ValueError as exc:
    print(str(exc)+" Digite apenas valores numericos")
except Exception as exc:
    print(str(exc)+" Algo deu errado :(")

else:
    print("Seu IMC é: " + result)
finally:
    print("END, Have a good day")
