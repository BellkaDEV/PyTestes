for i in range(28):
    if i == 0:
        a = 0
        b = 1
        c = 0
        print(f"{i+1}º Numero da sequencia de fibo: {a}")
        print(f"{i+2}º Numero da sequencia de fibo: {b}")
    c = a + b
    a = b
    b = c
    print(f"{i+3}º Numero da sequencia de fibo: {c}")