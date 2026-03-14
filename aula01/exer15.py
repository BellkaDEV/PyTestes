import string

minusculas = string.ascii_lowercase
maiusculas = string.ascii_uppercase

msg = None
desl = 0

def pos(c):
    if c.isupper():
        for i in range(len(maiusculas)):
            if maiusculas[i] == c:
                return i 
    if c.islower():
        for i in range(len(minusculas)):
            if minusculas[i] == c:
                return i 


def cifra(msg, s):
    for i in range(len(msg)):
        if msg[i].isupper():
            msg[i] = maiusculas[pos(msg[i])+s]
        if msg[i].islower():
            msg[i] = minusculas[pos(msg[i])+s]


msg = input("insira a mensagem: ")
s = int(input("insira o deslocamento: "))
msg = list(msg)
cifra(msg, s)
boua = "".join(msg)
print(boua)