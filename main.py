# biblioteca para fazer a interfase

from tkinter import * 
from tkinter import Tk, ttk

#instalar  pip install pillow
from PIL import Image, ImageTk

#importtanto barra progresso do tkinder
from tkinter.ttk import Progressbar

#importando mgraficos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Core da interfase
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"  

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

# tela vazia
janela = Tk()
janela.title()
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE) #bloquear maximizar

style= ttk.Style(janela)
style.theme_use("clam")


# criando 1ra frames dividir a tela
frameCima = Frame(janela, width=1043, height=50, bg=co0, relief="flat") #co1
frameCima.grid(row=0,column=0)

# criando 2do frames dividir a tela
frameMeio = Frame(janela, width=1043, height=361, bg=co0, pady=20, relief="raised")
frameMeio.grid(row=1,column=0, pady=1,padx=0, sticky=NSEW)

# criando 3ro frames dividir a tela
frameBaixo = Frame(janela, width=1043, height=300, bg=co0, relief="flat")
frameBaixo.grid(row=2,column=0, pady=0, padx=0, sticky=NSEW)


#logo imagem frame e title
app_img = Image.open('logo.png')
app_img = app_img.resize ((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Orçamento Pessoal", width=900, compound=LEFT, padx=5,relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co0, fg=co1)
app_logo.place(x=0,y=0)


# 2da fase text 
def porcentagem():
    label_nome = Label(frameMeio, text="Porcentagem da Receita Gasta", height=1, anchor=NW, font=('Verdana 12'), bg=co8, fg=co5)
    label_nome.place(x=7, y=5)

# barra porcentagem stilizada
    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness=28)

    #faz aparecera barra
    bar =Progressbar(frameMeio, length=180,style='black.Horizontal.TProgressbar')
    bar.place(x=10, y=35)
    bar['value'] = 50

#text do %
    valor = 50
    label_percentagem = Label(frameMeio, text="{:.2f}%".format(valor), anchor=NW, font=('Verdana 12'), bg=co8, fg=co5)
    label_percentagem.place(x=200, y=35)

###############

# 2da fase grafico de barra
def grafico_bar():
    lista_categorias = ['Renda', 'Despesaa', 'saldo']
    lista_valores = [3000, 2000, 6236]

#criação do grafico de barra
    #faça figura e atribua objetos de eixo
# Preta
    figura = plt.Figure(figsize=(4, 3.45), dpi=60, facecolor='#2e2d2b')
    ax = figura.add_subplot(111)
    #ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9) #cores das barras
    #create a list to collect the plt.patches data

    c = 0
   # set individual bar lables using above list
    for i in ax.patches:
        #get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='#ffffff')#cor lista de valores
        c += 1

    ax.set_xticklabels(lista_categorias,fontsize=16, color='#ffffff') #cor da lista de cartegorias

    ax.patch.set_facecolor('#2e2d2b')
    ax.spines['bottom'].set_color('#2e2d2b')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#2e2d2b')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False, labelcolor='#ffffff')#cores do eixo Y numeros de 0 a 6000
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#111111')#cor das row horizontais
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)







porcentagem()
grafico_bar()

janela.mainloop()   #chamar a tela




