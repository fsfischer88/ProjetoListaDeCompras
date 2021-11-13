



# dict_turma = {"Felipe":"3","Marcos":"3","Juliana":"3"}

# media = int(dict_turma["Felipe"])+int(dict_turma["Marcos"])+int(dict_turma["Juliana"])/3


# if media >= 7:
#     print("Turma aprovada!")
# elif media >= 5:
#     print("Turma em recuperação!")
# else: 
#     print("Turma está reprovado!")


dict_turma = {}
qt_alunos = int(input("Digite a quantidade de Aluno: \n"))
qt_notas = int(input("Digite a quantidade de Notas: \n"))

cont = 0
cont2 = 0
notas = []

while cont != qt_alunos:
    cont = cont + 1
    nome = input("Digite o Nome do Aluno"+str(cont)+ ":")
    cont2 = 0
    notas = []
    while cont2 != qt_notas:
        cont2 = cont2 + 1
        nota = float(input("Digite a nota"+str(cont2)+":"))
        notas.append(nota)

    media = (sum(notas)) / qt_notas
    dict_turma[nome] = media

    list_alunos = dict_turma.keys()

    for aluno in list_alunos:
        print("O aluno: " + aluno + "Possui a média: " + str(dict_turma[aluno]))

