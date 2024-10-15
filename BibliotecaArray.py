def texto(letras):
    cont = 0
    for x in letras:
      if x not in " !@$%":
        cont +=1
    print(f"O texto tem {cont} letras")
    print(letras[::-1])

def listaUnica(a):
    nova_lista=[]
    for x in a:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)

def numero_primo(n):
    if n==1:
        return n,"Nao é primo"
    elif n==2:
        return"E primo"
    else:
        for x in range (2,n):
            if n % x==0:
                return n,"Nao é primo"
            return n,"E primo"