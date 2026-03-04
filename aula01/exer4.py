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

num = 21

while True:
    if primo(num):
        print(num)
    if num == 500:
        break
    num = num + 1


            


