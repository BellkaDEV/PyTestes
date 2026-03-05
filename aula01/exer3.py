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
    PT += 10

if PA == A:
    PT =+ 5
    
if PB == B:
    PT += 5

print(f"Pontos: {PT}")