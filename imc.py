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


try:
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    print("Seu IMC é: " + str(calcimc(peso, altura)))

except ZeroDivisionError as exc:
    print(str(exc)+" Digite apenas valores acima de 0")
except ValueError as exc:
    print(str(exc)+" Digite apenas valores numericos")
except Exception as exc:
    print(str(exc)+" Algo deu errado :(")

else:
    print("Fim.")
finally:
    print("Have a good day")
