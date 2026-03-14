import random
Lista = []
for i in range(20):
    Lista.append(random.randint(1, 10))

print(Lista)
cont = 1
vez = 0
for j in range(1, 9):
    for i in range(20):
        if Lista[j] == Lista[i]:
            vez += 1
    print(f"numero {j} aparece {vez} vezes.")
    vez = 0