

# dict_lista_compras= {"produto1":"","produto2":"","produto3":""}

# produto1 = input("Digite p produto1: ")
# produto2 = input("Digite p produto2: ")
# produto3 = input("Digite p produto3: ")

# produtos_lista = [produto1, produto2, produto3]


# for p in produtos_lista:
#     print(p)

dict_lista_compras = {}

#dict_lista_compras= {'1':'Beterraba','2':'Pãozinho','3':'Café'}

# Criar Forma Dinamica de Adicionar Itens no Dicionario dict_lista_compras

qt_produots = int(input("Quantos Produtos Deseja em Sua Lista? \n"))
cont =0

while(True):
    if (qt_produots == 0):
        break
    else:
        cont +=1
        produto = input("Digite um Produto: \n")
        dict_lista_compras[cont] = produto
        qt_produots =  qt_produots -1

id_produtos = dict_lista_compras.keys()

lista_id_produtos = []

for produto in id_produtos:
    lista_id_produtos.append(produto)

print("\n")

#print (lista_id_produtos[:-1])

print("\n")

arquivo = open('lista_de_comptas.txt', 'w')
		

for id in lista_id_produtos:
    arquivo.writelines(str(id) + " : "+ dict_lista_compras[id]+"\n")

arquivo.close()