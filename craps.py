import random

"""
*************************Regras**********************************
Para escolher um tipo de aposta, utilize as seguintes abreviações:
Para apostar no Pass Line, digite PLB;
Para apostar no Field, digite F;
Para apostar no Any Craps, digite AC;
Para apostar no Twelve, digite T;
Obs: É possivel apostar em até 4 tipos de apostas diferentes, dependendo da fase do jogo
Para fazer mais de uma aposta, utilize o formato TIPO_DE_APOSTA_1,TIPO_DE_APOSTA_2,TIPO_DE_APOSTA_3
"""

def dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2

    while True:
        if input("Aperte F para rodar dado? ") == "f": break

    print(f"Dado 1: {dado1} e Dado 2: {dado2}")
    print(f"Soma: {soma}")

    return (dado1, dado2, dado1+dado2)

def passLineBet(soma):
    aposta = float(input("Quanto deseja apostar no Pass Line? "))
    
    if soma in [7, 11]:
        print(f"Você ganhou {aposta}!")
    elif soma in [2, 3, 12]:
        aposta = -aposta
        print(f"Você perdeu! :(")
    else:
        print("Você foi para o Point!")
        return (True, soma, aposta)
    
    return (False, soma, aposta)

def field(soma):
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

def anyCraps(soma):
    aposta = float(input("Quanto deseja apostar no Any Craps? "))
    
    if soma in [2, 3, 12]:
        aposta *= 7
        print(f"Você ganhou {aposta}!")
    else:
        aposta = -aposta
        print(f"Você perdeu! :(")
    return aposta

def twelve(soma):
    aposta = float(input("Quanto deseja apostar no Twelve? ")) 
    
    if soma == 12:
        aposta *= 30
        print(f"Você ganhou {aposta}!")
    else:
        aposta = -aposta
        print(f"Você perdeu! :(")
    return aposta


def comeOut():
    tiposDeAposta = input("Em qual quer apostar (N para não apostar e sair do jogo)? Ex: PLB,F,AC,T").split(",")
    
    while tiposDeAposta[0] not in ["N", "PLB", "F", "AC", "T"]:
        tiposDeAposta = input("Em qual quer apostar (N para não apostar e sair do jogo)? Ex: PLB,F,AC,T").split(",")
    
    if "N" in tiposDeAposta:
        return ('f', [])
    

    (dado1, dado2, soma) = dados()

    dic = {"PLB": passLineBet, "F": field, "AC": anyCraps, "T": twelve}
    
    lucroOuPrejuizo = 0
    lista = [False, soma, 0]

    for aposta in tiposDeAposta:
        
        if aposta == "PLB":
            lista = dic[aposta](soma) # Lista => [bol, soma, aposta]
        
            if lista[0] == False:
                valor += lista[2]
        else:
            valor = dic[aposta](soma)

        lucroOuPrejuizo += valor

    
    return (lucroOuPrejuizo, lista)

    
    


def point(somaPoint, aposta, din):
    soma = 0
    while soma not in [7, somaPoint]:
        tiposDeAposta = input("Em qual quer apostar (N para não apostar e rolar os dados)? Ex: AC,T,P   Digite: ").split(",")
        
        while tiposDeAposta[0] not in ["N", "PLB", "F", "AC", "T"]:
            tiposDeAposta = input("Em qual quer apostar (N para não apostar e sair do jogo)? Ex: PLB,F,AC,T   Digite: ").split(",")
        
        (dado1, dado2, soma) = dados()

        dic = {"F": field, "AC": anyCraps, "T": twelve}
        
        lucroOuPrejuizo = 0

        for aposta in tiposDeAposta:
            valor = dic[aposta](soma)

            lucroOuPrejuizo += valor
        
        din += lucroOuPrejuizo
        
            
    if soma == somaPoint:
        print("Você ganhou o Point e voltou para o Come Out!")
        return din + aposta
    else:
        print("Você perdeu o Point e voltou para o Come Out!")
        return din - aposta



    


din = 100
passou = False

while True:
    (lucroOuPrejuizo, lista) = comeOut()
    if isinstance(lucroOuPrejuizo, str):
        break

    din += lucroOuPrejuizo

    if lista[0]: 
        passou = True
        somaPoint = lista[1]
        aposta = lista[2]

    if passou:
        din = point(somaPoint, aposta, din)