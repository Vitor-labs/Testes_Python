from tkinter import *


def action(numero):
    global operation
    operation += str(numero)
    label_operation.set(operation)


def igual():
    global operation
    try:
        total = str(eval(operation))
        label_operation.set(total)
        operation = total
    except SystemError:
        label_operation.set("Erro de Sintaxe")
        operation = 0
    except ZeroDivisionError:
        label_operation.set("Não é possivel dividir por 0")
        operation = ""


def limpar():
    global operation
    label_operation.set("")
    operation = ""


window = Tk()
window.title("Brazuca Calculator 3000")
window.config(background="#000000")

icon = PhotoImage(file='ibagens\\icom.png')
window.iconphoto(True, icon)

operation = ""

label_operation = StringVar()
label = Label(window,
              textvariable=label_operation,
              font=("Arial", 18),
              bg="gray",
              fg="black",
              relief=RAISED,
              width=19,
              height=2).pack()

frame = Frame(window, relief=SUNKEN)

limpa = Button(frame, text="CE", font=("Arial", 25),
               command=limpar, width=3, bg="#000080", fg="#707070").grid(row=0, column=0)
cs = Button(frame, text="C", font=("Arial", 25),
            width=3, bg="#000080", fg="#707070").grid(row=0, column=1)
corrige = Button(frame, text="⌫", font=("Arial", 25),
                 width=3, bg="#000080", fg="#707070").grid(row=0, column=2)
resultado = Button(frame, text="=", font=("Arial", 25),
                   command=igual, width=3, bg="#000080", fg="#707070").grid(row=0, column=3)

mais = Button(frame, text="+", font=("Arial", 25),
              command=lambda: action('+'), width=3, bg="#101010", fg="#707070").grid(row=1, column=3)
menos = Button(frame, text="-", font=("Arial", 25),
               command=lambda: action('-'), width=3, bg="#101010", fg="#707070").grid(row=2, column=3)
vezes = Button(frame, text="x", font=("Arial", 25),
               command=lambda: action('*'), width=3, bg="#101010", fg="#707070").grid(row=3, column=3)
divide = Button(frame, text="÷", font=("Arial", 25),
                command=lambda: action('/'), width=3, bg="#101010", fg="#707070").grid(row=4, column=3)

um = Button(frame, text="1", font=("Arial", 25),
            command=lambda: action(1), width=3, bg="#101010", fg="#707070").grid(row=1, column=0)
dois = Button(frame, text="2", font=("Arial", 25),
              command=lambda: action(2), width=3, bg="#101010", fg="#707070").grid(row=1, column=1)
tres = Button(frame, text="3", font=("Arial", 25),
              command=lambda: action(3), width=3, bg="#101010", fg="#707070").grid(row=1, column=2)
quatro = Button(frame, text="4", font=("Arial", 25),
                command=lambda: action(4), width=3, bg="#101010", fg="#707070").grid(row=2, column=0)
cinco = Button(frame, text="5", font=("Arial", 25),
               command=lambda: action(5), width=3, bg="#101010", fg="#707070").grid(row=2, column=1)
seis = Button(frame, text="6", font=("Arial", 25),
              command=lambda: action(6), width=3, bg="#101010", fg="#707070").grid(row=2, column=2)
sete = Button(frame, text="7", font=("Arial", 25),
              command=lambda: (action(7)), width=3, bg="#101010", fg="#707070").grid(row=3, column=0)
oito = Button(frame, text="8", font=("Arial", 25),
              command=lambda: action(8), width=3, bg="#101010", fg="#707070").grid(row=3, column=1)
nove = Button(frame, text="9", font=("Arial", 25),
              command=lambda: action(9), width=3, bg="#101010", fg="#707070").grid(row=3, column=2)
zero = Button(frame, text="0", font=("Arial", 25),
              command=lambda: action(0), width=3, bg="#101010", fg="#707070").grid(row=4, column=1)
inverte = Button(frame, text="±", font=("Arial", 25),
                 command=action, width=3, bg="#101010", fg="#707070").grid(row=4, column=0)
ponto = Button(frame, text=".", font=("Arial", 25),
               command=action, width=3, bg="#101010", fg="#707070").grid(row=4, column=2)

frame.pack()

window.resizable(False, False)
window.mainloop()
