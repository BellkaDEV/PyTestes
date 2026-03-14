"""import math

while True:
    PA = int(input("População A: "))
    PB = int(input("População B: "))
    TA = float(input("taxa de crescimento da cidade A: "))
    TB = float(input("taxa de crescimento da cidade B: "))
    if PA < PB and TA > TB:
        break

TA = TA/100
TB = TB/100

t = (math.log(PB/PA))/(math.log((TA+1)/(TB+1)))

print(round(t, 2))
"""
while True:
    PA = int(input("População A: "))
    PB = int(input("População B: "))
    TA = float(input("taxa de crescimento da cidade A: "))
    TB = float(input("taxa de crescimento da cidade B: "))
    if PA < PB and TA > TB:
        break
TA = TA/100
TB = TB/100
t = 0
while PA < PB:
    PA = int(PA*(1+TA))
    PB = int(PB*(1+TB))
    t += 1

print(f"tempo em anos para superar cidade B: {t}")
