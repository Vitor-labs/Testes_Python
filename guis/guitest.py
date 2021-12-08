from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Teste de Janela")
# window.geometry("640x520")
window.config(background="GRAY")

icon = PhotoImage(file='guis\\edit.png')
window.iconphoto(True, icon)

img = PhotoImage(file='guis\\back.png')

label = Label(window,
              text="Digite alguma coisa:",
              font=('arial', 12, 'bold'),
              fg='white',
              bg='black',
              compound="right")

#label.place(x=10, y=10)
label.pack()

entrada = Entry(window,
                font=('arial', 22),
                fg="#00ff00", bg="black")

entrada.pack(side='left')


def click():
    user = entrada.get()
    if user == "alguma coisa":
        messagebox.showinfo(title="Genial",
                            message="Que Criatividade exagerada é essa ein parça")

        return
    print(user)
    entrada.config(state=DISABLED)


def delete():
    entrada.delete(0, END)


but = PhotoImage(file='guis\\klipartz.png')

button = Button(window,
                text="continuar",
                command=click,
                font=("Comic Sans", 16),
                fg="red",
                bg="black",
                activeforeground="black",
                activebackground="red",
                state=ACTIVE,
                compound='bottom')

button_delete = Button(window,
                       text="limpar",
                       command=delete,
                       font=("Comic Sans", 16),
                       fg="red",
                       bg="black",
                       activeforeground="black",
                       activebackground="red",
                       state=ACTIVE,
                       compound='bottom')


button.pack(side=RIGHT)
button_delete.pack(side=BOTTOM)

window.mainloop()
