class error(RuntimeError):
    def __init__(self, message):
        self.message = message


def calcimc(peso, altura):
    imc = peso/(altura * altura)
    avaliaResult(imc)
    return imc


def avaliaResult(result):
    if result < 18:
        print("Seu IMC está muito baixo ")
    elif result < 26:
        print("Seu IMC está normal")
    else:
        print("Seu IMC está muito alto")


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
