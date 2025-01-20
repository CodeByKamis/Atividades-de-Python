nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))
nota4 = float(input("Digite a sua quarta nota: "))
nota5 = float(input("Digite a sua quinta nota: "))
notas = nota1+nota2+nota3+nota4+nota5
calculo = notas /5

if calculo >= 5:
    print(f"APROVADO! Nota {calculo}.")
elif calculo >= 2.5 and calculo <5:
    print(f"RECUPERÇÃO! Nota {calculo}")
else:
    print(f"REPROVADO! Nota {calculo}.")