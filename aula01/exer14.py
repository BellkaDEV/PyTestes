text = input("insira o texto: ")

text = text.upper()

vogais = ["A", "E", "I", "O", "U"]
n = 0
for char in text:
    if char in vogais:
        n += 1
print(n)