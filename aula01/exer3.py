Pven = input("De o palpite do vencedor (time A ou B): ")
PA = int(input("De o palpite do placar do time A: "))
PB =int(input("De o palpite do placar do time B: "))


A = int(input("Placar do time A: "))
B =int(input("Placar do time B: "))

ven = None

if A > B:
    ven = "A"
elif A < B:
    ven = "B"

PT = 0
if Pven.upper() == ven: 
    PT = PT + 10

if PA == A:
    PT = PT + 5
elif PB == B:
    PT = PT + 5
elif PA == A and PB == B:
    PT + 10

print(f"Pontos: {PT}")