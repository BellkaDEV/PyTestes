Pven = input("De o palpite do vencedor (time A ou B): ")
PA = int(input("De o palpite do placar do time A: "))
PB =int(input("De o palpite do placar do time B: "))

ven = input("Vencedor (time A ou B): ")
A = int(input("Placar do time A: "))
B =int(input("Placar do time B: "))

PT = 0
if Pven == ven:
    PT + 10

if PA == A:
    PT + 5
elif PB == B:
    PT + 5
elif PA == A and PB == B:
    PT + 10
    
