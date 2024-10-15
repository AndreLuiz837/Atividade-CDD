#Criar um array tamanho 5 e preencher com nomes dos 5 Alunos
#informado pelo Usuario.

arrayAlunos = [0]*5
tam = len(arrayAlunos)
for x in range(tam):
    arrayAlunos [x] = input("Diga o nome dos Alunos:")
print(arrayAlunos)