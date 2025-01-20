numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

calculo = numero1 + numero2

if calculo % 2 == 0:
    print(f"A soma dos numeros {numero1} e {numero2} é {calculo} e é par")
if calculo % 2 != 0:
    print(f"A soma dos numeros {numero1} e {numero2} é {calculo} e é ímpar")
