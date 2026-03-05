import random

while True:
    a = int(input("informe o valor de a: "))
    b = int(input("informe o valor de b: "))
    if b <= a:
        print("b menor ou igual a a, tente novamente...")
    else:
        break

poss = False
while True:
    z = int(input(f"Informe o valor alvo (z) para a soma de x+y: "))
    if 2*a <= z <= 2*b:
        poss = True
        break
    else:
        print(f"Impossível! A soma deve estar entre {2*a} e {2*b}. Tente novamente.")
temp = ""
lista = []
for x in range(a, b, 1):
    for y in range(a, b, 1):
        if x+y == z and x != y:
            temp = str(y) + " = " + str(x)
            if temp in lista:
                continue
            else:
                lista.append(str(x) + " = " + str(y))
        



print(lista)
print(f"z = x + y = {z}")

 