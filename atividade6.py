lista = []

while True:
    numero= float(input("Digite um numero: "))

    if numero <0:
        numerao = max(lista)
        print(f"O maior número já digitado é: {numerao}")
        break

    elif numero >= 0:
        lista.append(numero)

    else:
        continue