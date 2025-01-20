s = input("Digite uma palavra: ")

def inverter_string(s):
    invertido = ""

    for i in s:
        invertido = i + invertido

    return invertido

resposta = inverter_string(s)

print(resposta)
