# -*- coding: cp1252 -*-
#coding: utf8
# Menu Basico para TKinter

from Tkinter import *
from functools import partial

janela = Tk()
janela.title("JANELA DE MENU")
txtinc = Label(janela, text="PROGRAMA DE MENU")
txtinc.place(x=10, y=10)

#Função
def bt_click(botao):
    print(botao["text"])
    lbbotao["text"] = "OLA MUNDO!!!"
    
def bt3_onclick():
    print(ed.get())
    lb["text"] = ed.get()

class Sistema:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.menu = Menu(master)

        self.menuArquivo = Menu(self.menu)
        self.menuArquivo.add_command(label="Novo")
        self.menuArquivo.add_command(label="Abrir")
        self.menuArquivo.add_command(label="Salvar")
        self.menuArquivo.add_command(label="Salvar Como")
        self.menuArquivo.add_command(label="Sair")
        self.menu.add_cascade(label="Arquivo", menu=self.menuArquivo)

        self.menuExibir = Menu(self.menu)
        self.menuExibir.add_command(label="Tela Cheia F5")
        self.menuExibir.add_command(label="Caixas")
        self.menu.add_cascade(label="Exibir", menu=self.menuExibir)

        self.menuFerramentas = Menu(self.menu)
        self.menuFerramentas.add_command(label="Opções")
        self.menuFerramentas.add_command(label="Linguagem")
        self.menu.add_cascade(label="Ferramnetas", menu=self.menuFerramentas)

        self.menuAjuda = Menu(self.menu)
        self.menuAjuda.add_command(label="Sobre")
        self.menuAjuda.add_command(label="Help")
        self.menu.add_cascade(label="Ajuda", menu=self.menuAjuda)

        master.config(menu=self.menu)
Sistema(janela)

#Programa de Botão
lbbotao = Label(janela, text="")
lbbotao.place(x=10, y=70)

bt1 = Button(janela, width=20, text="Botão 1")
bt1["command"] = partial(bt_click, bt1)
bt1.place(x=100, y=50)

bt2 = Button(janela, width=20, text="Botão 2")
bt2["command"] = partial(bt_click, bt2)
bt2.place(x=100, y=90)


# janela INPUT CAIXA DE ENTRADA
  
ed = Entry(janela)
ed.place(x=100, y=180)

bt3 = Button(janela, width=10, text="OK", command=bt3_onclick)
bt3.place(x=100, y=220)

lb = Label(janela, text="")
lb.place(x=100, y=280)



janela.geometry("600x400")
janela.mainloop()
    
        
