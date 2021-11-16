import tkinter as tk
from tkinter import ttk
import datetime as dt
from tkinter.constants import GROOVE, RIDGE

#VARIÁVEIS
listaCodigos = [] #lista criada para salvar os dados
arquivo = 'teste.txt' #bloco de notas para mostrar os dados

#FUNÇÕES PARA FAZER O PROGRAMA COLETAR OS DADOS
def funcoesProgr():
    contador = 0 #variável de um contador 
    nomeCliente = entry_nome.get().title() #(get)comando para coletar os dados inseridos no nome do cliente
    produto = cbSelecionarProdutos.get()
    quantidade = entry_Quantidade.get()
    dataCodigo = dt.datetime.now() #comando para gerar uma data do dia atual
    dataCodigo = dataCodigo.strftime('%d/%m/%Y') #comando para formatar a data 
    codigoId = f'ID ({contador})' #comando para formatar o id
    listaCodigos.append((codigoId, nomeCliente, produto, quantidade, dataCodigo)) #comando para adicionar os dados em uma lista

def salvarDados(): 
    contador = 0
    abrirArquivo = open(arquivo, 'at') #abrir o documento de texto
    for c in range(0,len(listaCodigos)): #comandos para listar as entradas já formatadas
        for v in range(0, len(listaCodigos[contador])):
            abrirArquivo.write(f'{listaCodigos[contador][v]} | ') #comando para abrir o arquivo e escrever as entradas formatadas
        abrirArquivo.write(f'\n') #comando para abrir o arquivo e escrever um quebra linha
        contador = contador + 1
    abrirArquivo.close()


#JANELA
janela = tk.Tk() #criar uma janela
janela.title('Cadastro de Compras SV') #título da janela
janela.iconbitmap('images\icone.ico') #escolher o ícone da janela
janela.geometry("282x250") #definir as dimensões da tela
janela['bg'] = '#000000' #definir a cor de fundo da janela

#TEXTO COM NOME DO CLIENTE
label_nome = tk.Label(text='NOME DO CLIENTE', bg='#ffff00') #criar uma label para o nome do cliente
label_nome.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=5) #definir as propriedades da label dentro da janela

#CAIXA PARA RECEBER O NOME DO CLIENTE
entry_nome = tk.Entry() #criar uma caixa de recebimento de dados
entry_nome.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=5) #definir as praopriedades da caixa dentro da janela

#TEXTO COM NOME DOS PRODUTOS
label_nomeProdutos = tk.Label(text='PRODUTO', bg='#ffff00')
label_nomeProdutos.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

#CAIXA COM SELEÇÃO DOS PRODUTOS
listaProdutos = ['Whey Concentrado', 'Whey Basic', 'Hipercalórico', 'Albumina', 'Creatina Monohidratada', 'Creatina Creapure', 'Creme Branco', 'Termogênico',
'Multivitamínico', 'Cafeína', 'Pré-Treino Nuclear Rush']
cbSelecionarProdutos = ttk.Combobox(values=listaProdutos)
cbSelecionarProdutos.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=3)

#TEXTO COM QUANTIDADE
label_quantidade = tk.Label(text='QUANTIDADE', bg='#ffff00') #criar uma label para a quantidade de produtos
label_quantidade.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=3)

#CAIXA PARA RECEBER A QUANTIDADE
entry_Quantidade = tk.Entry() #criar uma caixa para receber a quantidade
entry_Quantidade.grid(row=4, column=3, padx=30, pady=10, sticky='nswe', columnspan=2)

#TEXTO COM PREÇO
label_preco = tk.Label(text='PREÇO R$', bg='#ffff00')
label_preco.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

#CAIXA PARA RECEBER O PREÇO
entry_preco = tk.Entry() #criar caixa para receber o preço
entry_preco.grid(row=5, column=4, padx=20, pady=10, sticky='nswe', columnspan=1)

#BOTÃO PARA SALVAR O CÓDIGO
botaoSalvarCompra = tk.Button(text='SALVAR', command=funcoesProgr, bg='#ffff00', relief=RIDGE, border=3) #criar botão clicável e executar as funções criadas com o def
botaoSalvarCompra.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=5)

janela.mainloop() #comando usado para que a interface seja exibida


salvarDados()
print(listaCodigos) #mostrar os dados que foram salvos
#print(len(listaCodigos))
