#Faça um codigo para ler 5 nomes e suas senhas,e armazenar cada lista em um array diferente
#depois imprimir,nome,senha e posicao dos dados do array.

arrayNome = [0]*5
arraySenha = [0]*5
tam = len(arrayNome)
for x in range(tam):
    arrayNome[x] = input("Diga o nome do Usuario:")
    arraySenha[x] = input("Diga a senha do Usuario:")
for i in range(tam):
    print(f"Usuario:{arrayNome[i]} Senha:{arraySenha[i]} está na posição {i}.")
