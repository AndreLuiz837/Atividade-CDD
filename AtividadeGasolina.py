tipo = str(input(f"Qual o tipo do combustivel ('G' para gasolina e 'E' para etanol):")
litros = float(input(f"Diga a quantidade de litros:"))

if tipo == "G" or tipo == "E" or tipo == "g" or tipo == "e":
    if tipo == "G" or tipo == "g":
        valor = litros * 5.80
    else:
        valor = litros * 4.90
    print(f"O valor a pagar sera {valor}.")
else:
    print(f"O tipo de combustivel é invalido.")
