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

num = int(input("Insira um numero inteiro natural: "))

if primo(num):
    print("Numero primo!")
else:
    print("Nao primo")

            


