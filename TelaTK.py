from pathlib import Path
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# Classe da Interface com Usuário
#
class Tela(ttk.Frame):


    def __init__(self, master):
        super(Tela, self).__init__()
        #
        # ttk.Frame.__init__(self, master)
        self.master = master
        self.title = "Tratamento Espectros"
        #
        # dataframe familia terá todos os espectros carregados
        #
        global familia
        familia = pd.DataFrame([],columns=['lambda'])
        #
        # define tamanho da janela
        #
        self.master.geometry('600x400')
        #
        # Botões e Texto no MasterFrame
        #
        self.caixa1 = tk.Frame(master, borderwidth=2, relief='raised')
        self.caixa1.grid(column=1, row=2)
        self.texto1 = tk.Label(self.caixa1, text='---------Tratamento - Espectros -----------')
        self.texto1.grid(column=2, row=1)
        self.texto2 = tk.Label(master, text='----')  # a ser criado - sem extensão')
        self.texto2.grid(column=1, row=3)

        #self.nome = tk.Entry(master)
        #self.nome.grid(column=2, row=3)

        self.botaoArquivo = tk.Button(master, text=' Selecionar Arquivo  ', command=self.select_file)
        self.botaoArquivo.grid(column=2, row=6)
        self.botaoGrafico = tk.Button(master, text=' Grafico  ', command=self.grafico_preparo)
        self.botaoGrafico.grid(column=3, row=6)
        self.botaoSalvar = tk.Button(master, text='   Salvar      ', command=self.salvar_excel)
        self.botaoSalvar.grid(column=4, row=6)
        self.botaoSair = tk.Button(master, text='     Sair    ', command=master.destroy)
        self.botaoSair.grid(column=5, row=20)

        self.caixa_grafico = tk.Frame(master, borderwidth=10, relief='ridge')
        self.caixa_grafico.grid(column=0, row=6, padx=10, pady=10)

        figura = Figure(figsize=(6, 4), dpi=100)
        canva = FigureCanvasTkAgg(figura, self)
        canva.get_tk_widget().grid(column=0, row=6, padx=10, pady=10)

        #self.botaoLeitura = tk.Button(master, text='  Obter Dados   ', command=self.leitura(filename))
        #self.botaoLeitura.grid(column=1, row=6)
        #
        self.master.mainloop()
        #

    def select_file(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        #identifica o user logado e abre na pasta Documents
        user = os.getlogin()
        filename = fd.askopenfilename(
            title='Open a file',
            filetypes=filetypes
            )
        # Split the filepath to get the directory
        #directory = os.path.split(filename)[0]
        #
        self.leitura(filename)
        return filename

    def diretorio(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        global folder_path
        filename = filedialog.askdirectory()
        folder_path.set(filename)
        # definir folder_path como diretorio ativo
        sourcePath = folder_path.get()
        os.chdir(sourcePath)  # Provide the path here
        # print(filename)
    def leitura(self,filename):
        global familia
        global directory
        print("Alô:::::",filename, familia)
        arquivo=open(filename,'r',encoding='utf8')
        directory = os.path.split(filename)[0]
        nome_arquivo=filename[len(directory)+1:len(filename)-4]
        espectro = pd.read_csv(
            arquivo, sep='\t', header=None)
        if (len(familia)==0):
            familia=espectro
            print('primeira vez', espectro[0])
        else:
            coluna_atual=familia.shape[1]
            familia[coluna_atual]=espectro[1]
            #familia[coluna_atual]=pd.to_numeric(familia[coluna_atual], errors='coerce')
            print(familia)
        return familia

    def salvar_excel(self):
        global familia
        global directory

        nome=directory+"excel"
        # salvar com arquivo Excel
        familia.to_excel(f"{nome}.xlsx")
        print("arquivo criado")

        return

    def popup_showinfo(self):
        #
        #  Tratamento de Erro:
        #print('chegou em popup_showinfo')
        showinfo("ATENÇÃO", "Definir o nome do arquivo para armazenar o espectro!!")
        #
        ###########################################################################
        #
        #


    def grafico(x,y):
        plt.style.use('_mpl-gallery')
        #
        #criando figura dentro do TkInter
        #
        print('tentando fazer o grafico')
        figura=plt.Figure(figsize=(8,4), dpi=50)
        ax=figura.add_subplot(111)

        #
        #                                figura externa ao tk inter     fig, ax = plt.subplots()
        #print('grafico',x,y)
        ax.plot(x, y, linewidth=2.0)
        ax.set(xlim=(0, 14), xticks=np.arange(1, 14),
               ylim=(0, 1), yticks=np.arange(0, 1))
        #plt.show()

    def graficos(self):
        global familia
        print(familia)
        #fig = plt.figure(figsize=(5, 4))
        #ax = fig.add_axes([1, 1, 1, 1])
        #ax.plot(familia[0],familia[1])
        tamanho=familia.shape[1]
        for i in range(1,tamanho):
            plt.plot(familia[0],familia[i])
        #
        #
        plt.show()

    def grafico_preparo(self):
        #
        # ------------funções gráfico
        #
        self.graficos()

# ---------------------------------
if __name__ == '__main__':
    window = tk.Tk()
    folder_path = tk.StringVar()
    app = Tela(window)