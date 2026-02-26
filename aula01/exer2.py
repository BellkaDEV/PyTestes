# Desenvolver um programa em Python que calcule o salário semanal de um trabalhador. As entradas são: o número de horas trabalhadas
# na semana e o valor da hora. Até 40 h/semana não se acrescenta nenhum adicional. Acima de 40h e até 60h há um bônus de 50% para
# essas horas. Acima de 60h há um bônus de 100% para essas horas.

hrs = float(input("Horas trabalhadas: "))
valor = float(input("Salário por hora: "))
sal = hrs * valor
if hrs > 40 and hrs < 60:
    sal = sal * 1.5
elif hrs >= 60:
    sal = sal * 26
print(sal)
