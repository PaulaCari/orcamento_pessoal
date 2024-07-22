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

from matplotlib.ticker import FixedLocator

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


#layout da janela
# criando 1ra frames dividir a tela
frameCima = Frame(janela, width=1043, height=50, bg=co0, relief="flat") #co1
frameCima.grid(row=0,column=0)

# criando 2do frames dividir a tela
frameMeio = Frame(janela, width=1043, height=345, bg=co0, pady=20, relief="raised")
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
    lista_categorias = ['Renda', 'Despesas', 'saldo']
    lista_valores = [3000, 2000, 6236]

#criação do grafico de barra
    #faça figura e atribua objetos de eixo
# Preta
    figura = plt.Figure(figsize=(4, 3.45), dpi=60, facecolor='#2e2d2b')#dimensão do gráfico e cor dasbordas
    ax = figura.add_subplot(111)
   

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9) #cores das barras

   #crie uma lista para coletar os dados plt.patches
    c = 0
   # define rótulos de barras individuais usando a lista acima
    for i in ax.patches:
        #get_x puxa para a esquerda ou para a direita; get_height empurra para cima ou para baixo
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='#ffffff')#cor lista de valores
        c += 1
   
    loc = FixedLocator([0, 1, 2])  #posição dos ticks  (inclui)
    ax.xaxis.set_major_locator(loc)  # ixedLocator para o eixo x  (inclui)
    ax.set_xticklabels(lista_categorias,fontsize=16,color='#ffffff') #cor da lista de cartegorias (inclui color)

    ax.patch.set_facecolor('#2e2d2b') #cor de fundo
    ax.spines['bottom'].set_color('#2e2d2b')#linha inferior das barras
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
    ax.yaxis.grid(False)#cor das row horizontais
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)



#Totais resumo renda, despesa , saldo
def  resumo():
    valor =[500,600,420]

    l_linha = Label(frameMeio, text="", width=225, height=1, anchor=NW, font=('Arial 1'), bg='#545454' )
    l_linha.place(x=309,y=52) #linha
    l_sumario = Label(frameMeio, text="Total renda mensal      ".upper(), anchor=NW, font=('Verdana 12'), bg=co0, fg='#83a9e6')
    l_sumario.place(x=309,y=35) 
    l_sumario = Label(frameMeio, text="R$ {:.2f}".format(valor[0]), anchor=NW, font=('Arial 17'), bg=co0, fg=co5)
    l_sumario.place(x=309,y=70) 

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454' )
    l_linha.place(x=309,y=132) #linha
    l_sumario = Label(frameMeio, text="Total despesas mensais     ".upper(), anchor=NW, font=('Verdana 12'), bg=co0, fg='#83a9e6')
    l_sumario.place(x=309,y=115) 
    l_sumario = Label(frameMeio, text="R$ {:.2f}".format(valor[1]), anchor=NW, font=('Arial 17'), bg=co0, fg=co5)
    l_sumario.place(x=309,y=150) 

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454' )
    l_linha.place(x=309,y=207) #linha
    l_sumario = Label(frameMeio, text="Total saldo caixa        ".upper(), anchor=NW, font=('Verdana 12'), bg=co0, fg='#83a9e6')
    l_sumario.place(x=309,y=190) 
    l_sumario = Label(frameMeio, text="R$ {:.2f}".format(valor[2]), anchor=NW, font=('Arial 17'), bg=co0, fg=co5)
    l_sumario.place(x=309,y=220) 



#criando 4to frame para o grafico do pizza
frame_gra_pie = Frame(frameMeio, width=580, height=250, bg=co0)
frame_gra_pie.place(x=415, y=5)
#grafico de pizza
def grafico_pie():
    figura = plt.Figure(figsize=(5.5,3), dpi=90, facecolor='#333') #deslocamento do grafico de pizza e cor de fundo
    ax = figura.add_subplot(111)

    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    explode = []
    for i in lista_categorias:
            explode.append(0.05) #separação entre cada fatia

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.3), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90, textprops={'color': co9, 'fontsize': 10,'weight': 'bold'})#width é a largura das fatia e cor do %

    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50), labelcolor=co9, facecolor='#333') #posição da caixinha de lista de categorias

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie) #posição do grafico dentro da janela
    canva_categoria.get_tk_widget().grid(row=0, column=0)
    

porcentagem()
grafico_bar()
resumo()
grafico_pie()

#criando 3 frame dentro do frame baixo
#1ro frame tablela renda tipo excel
frame_renda = Frame(frameBaixo, width=300, height=250, bg=co0)
frame_renda.grid(row=0,column=0)

#2do frame renda mensal
frame_operacoes = Frame(frameBaixo, width=220, height=250, bg=co0) 
frame_operacoes.grid(row=0,column=1, padx=5)

#3er frame
frame_configuracao = Frame(frameBaixo, width=220, height=250, bg=co0) 
frame_configuracao.grid(row=0,column=2, padx=5) 

#Renda mensal 1ro
app_tabela = Label(frameMeio, text=" Tabela Receitas e Despesas", anchor=NW, font=('Verdana'), bg=co0, fg=co5)
app_tabela.place(x=5,y=300)


def mostrar_renda():
    # #criando uma treeview com barras de rolagem duplas
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]

    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    # vertical scroll
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    # horizontal scroll
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100] #tamnaho das
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])#aparece a tabela
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)
       

mostrar_renda()


janela.mainloop()   #chamar a tela




