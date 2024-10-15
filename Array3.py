#Faça um codigo para ler 10 numeros e guardar num vetor.Em seguida,ler mais um numero qualquer
#Calcular e escrever quantas vezes esse numero aparece no vetor.

arrayNumero = [0]*10
cont = 0
for x in range(10):
    arrayNumero[x] = int(input("Diga o numero:"))
num = int(input("Diga o numero para calcular:"))
for i in range(10):
    if arrayNumero [i] == num:
        cont = cont +1
print(cont)
