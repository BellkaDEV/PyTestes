
def decimal(num):
    valbin = 0
    soma = 0
    exp = 0
    while(num != 0):
        valbin = num % 10
        soma += valbin * (2**exp)
        num = num // 10
        exp += 1
    print(soma)
        

valor = int(input("insira o numero em binario: "))
decimal(valor)