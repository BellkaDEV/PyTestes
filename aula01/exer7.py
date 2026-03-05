num = input("insira o numero: ")
s = 0
for i in range(0, len(num), 1):
    s += int(num[i]) 
print(s)