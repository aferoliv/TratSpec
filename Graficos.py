import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#
# ------------funções gráfico
#
def grafico(x,y):
    plt.style.use('_mpl-gallery')
    #
    #criando figura dentro do TkInter
    #
    print('tentando fazer o grafico')
    figura=plt.Figure(figsize=(8,4), dpi=50)
    ax=figura.add_subplot(111)
    canva=FigureCanvasTkAgg(caixa_grafico,janela)
    canva.get_tk_widget().grid(column=0, row=6, padx=10, pady=10)
    #
    #                                figura externa ao tk inter     fig, ax = plt.subplots()
    #print('grafico',x,y)
    ax.plot(x, y, linewidth=2.0)
    ax.set(xlim=(0, 14), xticks=np.arange(1, 14),
           ylim=(0, 1), yticks=np.arange(0, 1))
    #plt.show()
def arredonda (valor):
    if valor > 0.001:
        texto ='{:.5f}'.format((valor))
    else:
        texto = '{:.5e}'.format((valor))
    return texto

def graficos(x,dados,carga):
    figura = plt.figure(figsize=(4,4))
    plt.subplot(211)                # linha, coluna, número do grafico
    plt.axis([0,14,0,1.05])         #lista [xmin, xmax, ymin, ymax]
    plt.plot(x,dados)
    plt.subplot(212)
    plt.axis([0, 14,min(carga)-.5,max(carga)+.5])  # lista [xmin, xmax, ymin, ymax]
    plt.plot(x,carga)
    #
    #
    #
    canva = FigureCanvasTkAgg(figura, caixa_grafico)
    canva.get_tk_widget().grid(column=0, row=6, padx=10, pady=10)
    #
    #plt.show()
