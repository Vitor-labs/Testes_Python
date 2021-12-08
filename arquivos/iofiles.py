import pywhatkit as kit
from tkinter import *
from tkinter import filedialog, messagebox, colorchooser, font
import os
"""
    FALTA FAZER:
    > editor de fonte
    > editor de tamanho da fonte
    > algum adicional opcional
"""


def open_file():
    filepath = filedialog.askopenfilename(defaultextension=".txt",
                                          initialdir="C:\\Users\\Computador\\Downloads",
                                          title="Escolha o Arquivo",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    if filepath is None:
        return

    else:
        try:
            window.title(os.path.basename(filepath))
            texto.delete(1.0, END)
            filename = open(filepath, 'r')
            texto.insert(1.0, filename.read())
            filename.close()

        except FileNotFoundError as exc:
            messagebox.showinfo(title=exc+": Erro",
                                message="O arquivo não pode ser aberto :(")

        except FileExistsError as exc:
            messagebox.showinfo(title=exc+": Erro inesperado",
                                message="O arquivo não pode ser aberto :(")

        except Exception as exc:
            messagebox.showinfo(title=exc+": Erro inesperado",
                                message="O arquivo não pode ser aberto :(")


def save_file():
    filename = filedialog.asksaveasfilename(initialdir="C:\\Users\\Computador\\Desktop",
                                            defaultextension='.txt',
                                            initialfile='unititled.txt',
                                            filetypes=[("Text File", ".txt"),
                                                       ("HTML File", ".html"),
                                                       ("All Files", ".*")])
    if filename is None:
        return

    else:
        try:
            window.title(os.path.basename(filename))
            filename = open(filename, "w")
            filename.write(str(texto.get(1.0, END)))
            filename.close()

        except Exception:
            messagebox.showinfo(title="Erro inesperado",
                                message="O arquivo não pode ser salvo :(")


def cor_texto():
    cor = colorchooser.askcolor()
    texto.config(fg=str(cor[1]))


def fonte_texto():
    janela_fonte = Toplevel()

    fontes = OptionMenu(janela_fonte, fonte, *
                        font.families()).grid(row=0, column=0)
    botao = Button(janela_fonte, text="Aplicar", command=texto.config(font=(fonte.get(), fonte_tam.get())))\
        .grid(row=0, column=1)


def tamanho_texto():
    janela_tamanho = Toplevel()
    size_box = Spinbox(janela_tamanho, from_=6, to=68,
                       textvariable=fonte_tam).grid(row=0, column=0)
    botao = Button(janela_tamanho, text="Aplicar", command=texto.config(font=(fonte.get(), size_box.get())))\
        .grid(row=0, column=1)


def transformar_texto():
    textomao = texto.get(1.0, END)
    kit.text_to_handwriting(textomao, save_to="a mao.png")


def cor_editor():
    cor = colorchooser.askcolor()
    texto.config(bg=str(cor[1]))


window = Tk()
# Configuração da janela
window.title("Editor de texto feião do Vitor")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (550 / 2))
y = int((screen_height / 2) - (650 / 2))

window.geometry("{}x{}+{}+{}".format(550, 600, x, y))
icon = PhotoImage(file="arquivos/rob.png")
window.iconphoto(True, icon)
# ======================
# Configurações do editor de texto
fonte = StringVar(window)
fonte.set("Consolas")
fonte_tam = StringVar(window)
fonte_tam.set("18")

texto = Text(window,
             background="#484848",
             foreground="white",
             font=(fonte.get(), fonte_tam.get()))

scroll = Scrollbar(texto)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
texto.grid(sticky=N+E+S+W)

scroll.pack(side=RIGHT, fill=Y)
texto.config(yscrollcommand=scroll.set)
# =====================
# Configurações da barra de menu
menuBar = Menu(window, bg="#686868", fg="white", relief=RAISED)

filemenu = Menu(menuBar, tearoff=0, bg="#686868", fg="white", relief=RAISED)
menuBar.add_cascade(label="Arquivo", menu=filemenu)
filemenu.add_command(label="Abrir", command=open_file)
filemenu.add_command(label="Salvar", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Sair", command=quit)

textoMenu = Menu(menuBar, tearoff=0, bg="#686868", fg="white", relief=RAISED)
menuBar.add_cascade(label="Texto", menu=textoMenu)
textoMenu.add_command(label="Fonte", command=fonte_texto)
textoMenu.add_command(label="Tamanho", command=tamanho_texto)
textoMenu.add_command(label="Cor", command=cor_texto)
textoMenu.add_command(label="Transformar a mão", command=transformar_texto)

editorMenu = Menu(menuBar, tearoff=0, bg="#686868", fg="white", relief=RAISED)
menuBar.add_cascade(label="Editor", menu=editorMenu)
editorMenu.add_command(label="Cor", command=cor_editor)

window.config(menu=menuBar)
# ======================
window.mainloop()
