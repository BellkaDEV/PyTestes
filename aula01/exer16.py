import random

def aleat(jafoi):
    while True:
        num = random.randint(0, len(estados_capitais)-1)
        if num % 2 == 0 and num not in jafoi:
            return num

estados_capitais = [
        "Acre", "Rio Branco", "Alagoas", "Maceió", "Amapá", "Macapá",
        "Amazonas", "Manaus", "Bahia", "Salvador", "Ceará", "Fortaleza",
        "Distrito Federal", "Brasília", "Espírito Santo", "Vitória",
        "Goiás", "Goiânia", "Maranhão", "São Luís", "Mato Grosso", "Cuiabá",
        "Mato Grosso do Sul", "Campo Grande", "Minas Gerais", "Belo Horizonte",
        "Pará", "Belém", "Paraíba", "João Pessoa", "Paraná", "Curitiba",
        "Pernambuco", "Recife", "Piauí", "Teresina", "Rio de Janeiro", "Rio de Janeiro",
        "Rio Grande do Norte", "Natal", "Rio Grande do Sul", "Porto Alegre",
        "Rondônia", "Porto Velho", "Roraima", "Boa Vista",
        "Santa Catarina", "Florianópolis", "São Paulo", "São Paulo",
        "Sergipe", "Aracaju", "Tocantins", "Palmas"
    ]

def jogar():
    resultados = []
    jafoi = []
    opc = "sim"
    t = 0
    a = 0
    while opc == "sim" or opc == "SIM":
        if len(jafoi) >= len(estados_capitais) // 2:
            break
        
        e = aleat(jafoi)
        jafoi.append(e)
        res = input(f"Qual a capital do/de {estados_capitais[e]}? ")
        if res == estados_capitais[e + 1]:
            t += 1
            a += 1
        else:
            t += 1
        
        opc = input("quer continuar a jogar? ")
        
        if t > 0:
            return [a, t, (a/t)*100]
        else:
            return 0

resultados = jogar()
print(f"Porcentagem de acertos foi de {resultados[2]}%")
print(f"{resultados[1]} questoes")
print(f"{resultados[0]} acertos")