import math

def primo(N):
    if N < 2: return False
    if N == 2: return True
    i = 2
    while(True):
        if (N % i) == 0:
            return False
        elif (i > math.sqrt(N)):
            return True
        i = i + 1

def fatores(num):
    fator = []
    i = 2
    while True:
        if num % i == 0 and primo(i):
            fator.append(i)
            num /= i
        else: 
            i += 1
        if num == 1:
            break
    return fator
     
while True:
    num = int(input("Insira um numero entre 100 e 10000: "))
    if num > 100 and num < 10000:
        break

print(fatores(num))