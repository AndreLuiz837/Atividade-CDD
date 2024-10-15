#Faca um algaritmo que leia 10 valores do tipo inteiro e armazene em um vetor.
#A seguir,o algaritmo devera informar.
#Todos os numeros pares que existem no vetor;
#O menor e maior valor existente no vetor;
#Quantos valores do vetor sao maiores que a media desses valores.

arrayNum = [0]*10
valor = 0
tam = len(arrayNum)
media = 0
soma=0
cont =0
for x in range(tam):
    arrayNum[x] = int(input("Diga o numero:"))
    soma += arrayNum[x]
media = soma/tam
for i in range(tam):
    if arrayNum[i] %2 == 0:
        print({arrayNum[i]})
for j in range(tam):
    maior=max(arrayNum)
    menor=min(arrayNum)
for y in range(tam):
    if arrayNum[y] > media:
        cont = cont + 1
print(f"O {maior} é o maior e {menor} é o menor \n"
      f"{cont} numeros maior que a media.")