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
    if PA > PB and TA < TB:
        break

t = 1
while PA > PB:
    PA = int(PA*TA)
    PB = int(PB*TB)
    t += 1

print(t)
