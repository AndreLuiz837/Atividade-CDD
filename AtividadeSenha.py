#Faça um codigo para ler a senha de um usuario e apos 3 tentativas erradas sair do programa
#informando que a senha está bloqueada.

pin = 1234

senha = int(input("Insira sua senha: "))
tent=1
while senha != pin and tent<3:
    senha = int(input(f"Senha errada \n"
                      f"voce tem {3-tent} \n "
                      f"Informe sua senha novamente:"))

    tent+=1

if tent == 3 and senha != pin:
    print("Senha bloqueada!")
else:
    print("Login efetuado com sucesso!")