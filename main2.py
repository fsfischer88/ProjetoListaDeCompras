

nome = input("Digite seu nome: ")

# ano_ncs: 2021

# idade = 2021 - 1988

# print("Seu nome é " + nome + " e você tem " + str(idade) + " anos de idade")


# Criar 3 variavéis de nota, uma variavel de nome e exibir o nome e a media do aluno

nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota : ")
nota3 = input("Digite a terceira nota : ")

# nota1 = 7
# nota2 = 9
# nota3 = 8

media = int((nota1 + nota2 + nota3))/3

print("Seu nome é " + nome + " e sua média foi de " + str(media))


if media >= 7:
    print("Parabéns, você está aprovado!")
elif media >= 5:
    print("Você está em recuperação!")
else: 
    print("Você está reprovado!")

dict_turma = {"Felipe":"7","Marcos":"8","Juliana":"9"}


# list_med = [7,9,8]
# list_result = ["Passou","Recuperação","Reprovou"]

# cont = 0
# for x in list_med:
#     if media >= int(x):
#         print(list_result[cont])
#         break
#     cont = cont +1

#Transformar em dinamico

