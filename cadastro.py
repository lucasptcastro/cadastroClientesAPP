import tkinter as tk
from tkinter import ttk
import datetime as dt
from tkinter.constants import GROOVE

listaCodigos = [] #lista criada para salvar os dados

#FUNÇÕES PARA FAZER O PROGRAMA COLETAR OS DADOS
def funcoesProgr():
    nomeCliente = entry_nome.get() #(get)comando para coletar os dados inseridos no nome do cliente
    produto = cbSelecionarProdutos.get()
    quantidade = cbSelecionarQuantidade.get()
    dataCodigo = dt.datetime.now() #comando para gerar uma data do dia atual
    dataCodigo = dataCodigo.strftime('%d/%m/%Y') #comando para formatar a data 
    id = len(listaProdutos)+1 #comando para criar um id dos clientes
    codigoId = f'ID ({id})' #comando para formatar o id
    listaCodigos.append((codigoId, nomeCliente, produto, quantidade, dataCodigo)) #comando para adicionar os dados em uma lista


#JANELA
janela = tk.Tk() #criar uma janela
janela.title('Cadastro de Compras') #título da janela

#TEXTO COM NOME DO CLIENTE
label_nome = tk.Label(text='Nome do cliente') #criar uma label para o nome do cliente
label_nome.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=4) #definir as propriedades da label dentro da janela

#CAIXA PARA RECEBER O NOME DO CLIENTE
entry_nome = tk.Entry() #criar uma caixa de recebimento de dados
entry_nome.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4) #definir as praopriedades da caixa dentro da janela

#TEXTO COM NOME DOS PRODUTOS
label_nomeProdutos = tk.Label(text='Produto')
label_nomeProdutos.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

#CAIXA COM SELEÇÃO DOS PRODUTOS
listaProdutos = ['Whey Concentrado', 'Whey Basic', 'Hipercalórico', 'Albumina', 'Creatina Monohidratada', 'Creatina Creapure', 'Creme Branco', 'Termogênico',
'Multivitamínico', 'Cafeína', 'Pré-Treino Nuclear Rush']
cbSelecionarProdutos = ttk.Combobox(values=listaProdutos)
cbSelecionarProdutos.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

#TEXTO COM QUANTIDADE DE PRODUTOS
label_quantidade = tk.Label(text='Quantidade') #criar uma label para a quantidade de produtos
label_quantidade.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

#CAIXA COM SELEÇÃO DA QUANTIDADE DE PRODUTOS
listaQuant = ['1', '2', '3', '4', '5'] #listagem dos itens que irão ficar no combobox
cbSelecionarQuantidade = ttk.Combobox(values=listaQuant) #criar um combobox, que é uma caixa selecionável
cbSelecionarQuantidade.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2) 

#BOTÃO PARA SALVAR O CÓDIGO
botaoSalvarCompra = tk.Button(text='Salvar compra', command=funcoesProgr) #criar botão clicável e executar as funções criadas com o def
botaoSalvarCompra.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

janela.mainloop() #comando usado para que a interface seja exibida

print(listaCodigos) #mostrar os dados que foram salvos