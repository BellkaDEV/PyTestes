import random
Lista = []

for i in range(50):
    Lista.append(random.randint(1, 100))

num = int(input("insira um numero: "))

if num in Lista:
    for i in range(49):
        if Lista[i] == num:
            print(f"Achado na posição {i}.")
            print(Lista[i])
else:
    print(f"Numero {num} não achado.")     

print(Lista)      

