# -*- coding: cp1252 -*-
#coding: utf8
# Menu Basico para TKinter

from Tkinter import *

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

root = Tk()
root.geometry("600x400")
root.title("Menu TKinter")
Sistema(root)
root.mainloop()
    
        
