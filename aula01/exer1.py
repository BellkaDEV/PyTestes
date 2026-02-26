import array


def media(N, L):
    aprov = True
    if L == 'A':
        mediaR = sum(N)/3
        print(f"Média A: {mediaR}") 
    elif L == 'P':
        mediaR = (N[0]*5 + N[1]*3 + N[2]*2)/8
        print(f"Média P: {mediaR}") 
    else:
        print(f"Você escolheu o tipo de média {L}, que não é válido...")
        aprov = False
    if aprov != False:
        if mediaR > 6.0:
            print("Aprovado")
        elif mediaR == 6.0 or mediaR < 6.0:
            print("Recuperação")
        else:
            print("Reprovado")
    else:
        print("Insira um tipo de média válido.")

a = float(input("Digite a primeira nota (0 a 10): "))
b = float(input("Digite a segunda nota (0 a 10): "))
c = float(input("Digite a terceira nota (0 a 10): "))

N = [a, b, c]
L = input("Agora digite o tipo de média A (aritimetica) ou P (Ponderada: ")

media(N, L)