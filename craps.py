import random

def dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2

    while True:
        if input("Aperte F para rodar dado? ") == "f": break

    print(f"Dado 1: {dado1} e Dado 2: {dado2}")
    print(f"Soma: {soma}")
    
    return (dado1, dado2, dado1+dado2)

def passLineBet():
    aposta = float(input("Quanto deseja apostar no Pass Line? "))
    (dado1, dado2, soma) = dados()
    
    if soma in [7, 11]:
        print(f"Você ganhou {aposta}!")
    elif soma in [2, 3, 12]:
        aposta = -aposta
        print(f"Você perdeu! :(")
    else:
        print("Você foi para o Point!")
        return (aposta, soma, True)
    
    return (aposta, soma, False)

def point_função(aposta, somaPoint):
    (dado1, dado2, soma) = dados()

    while soma not in [7, somaPoint]:
        (dado1, dado2, soma) = dados()
    
    if soma == somaPoint:
        print("Você ganhou o Point e voltou para o Come Out!")
        return aposta
    
    else:
        print("Você perdeu o Point e voltou para o Come Out!")
        return 0


def field():
    aposta = float(input("Quanto deseja apostar no Field? "))

    if soma in [5, 6, 7, 8]:
        print(f"Você perdeu! :(")
        return -aposta
    elif soma in [3, 4, 9, 10, 11]:
        print(f"Você ganhou {aposta}!")
        return aposta
    elif soma == 2:
        print(f"Você ganhou {aposta*2}!")
        return aposta * 2
    elif soma == 12:
        print(f"Você ganhou {aposta*3}!")
        return aposta * 3
        

def anyCraps():
    aposta = float(input("Quanto deseja apostar no Pass Line? "))
    
    if soma in [2, 3, 12]:
        aposta*=7
        print(f"Você ganhou {aposta}!")
    else:
        aposta = -aposta
        print(f"Você perdeu! :(")
    return aposta

def twelve():
    aposta = float(input("Quanto deseja apostar no Pass Line? ")) 
    
    if soma == 12:
        aposta *= 30
        print(f"Você ganhou {aposta}!")
    else:
        aposta = -aposta
        print(f"Você perdeu! :(")
    return aposta

       
    
din = 100
point = False

while True:
    if not point:
        tipo_aposta = input("Em qual quer apostar?")
        if tipo_aposta == "P":
            (aposta, somaPoint, point) = passLineBet()
            if point == False:
                din += aposta
                print(f'Saldo atual: {din}')
                resp = input("Deseja parar? ")
                if resp == 's': break
            else:
                din -= aposta
                print(f'Saldo atual: {din}')
                print(f'Valor apostado: {aposta}')
    
    else:
        aposta_point = point_função(aposta, somaPoint)
        din += aposta_point
        print(f'Saldo atual: {din}')
        point = False
        resp = input("Deseja parar? ")
        if resp == 's': break
        




