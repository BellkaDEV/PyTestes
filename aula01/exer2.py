hrs = float(input("Horas trabalhadas: "))
valor = float(input("Salário por hora: "))
sal = hrs * valor
if hrs > 40 and hrs < 60:
    sal = (hrs * valor) + (hrs - 40)* valor * 1.5
elif hrs > 60:
    sal = (hrs * valor) + (hrs - 60)* valor * 2
else:
    sal = hrs * valor
print(sal)
