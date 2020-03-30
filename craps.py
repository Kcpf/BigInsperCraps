import random

def stats(dado1, dado2, soma):
    print(f"Dado 1: {dado1} e Dado 2: {dado2}")
    print(f"Soma: {soma}")
    return None

def dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2

    while True:
        if input("Aperte F para rodar dado? ") == "f": break

    return (dado1, dado2, dado1+dado2)

def passLineBet(soma):
    aposta = float(input("Quanto deseja apostar no Pass Line? "))
    
    if soma in [2, 3, 12]:
        aposta = -aposta
    elif soma in [4, 5, 6, 8, 9, 10]:
        print("Você foi para o Point!")
        return (True, soma, aposta)
    
    return (False, soma, aposta)

def field(soma):
    aposta = float(input("Quanto deseja apostar no Field? "))

    if soma in [5, 6, 7, 8]:
        return -aposta
    elif soma in [3, 4, 9, 10, 11]:
        return aposta
    elif soma == 2:
        return aposta * 2
    elif soma == 12:
        return aposta * 3       

def anyCraps(soma):
    aposta = float(input("Quanto deseja apostar no Any Craps? "))
    
    if soma in [2, 3, 12]:
        aposta *= 7
    else:
        aposta = -aposta
    return aposta

def twelve(soma):
    aposta = float(input("Quanto deseja apostar no Twelve? ")) 
    
    if soma == 12:
        aposta *= 30
    else:
        aposta = -aposta
    return aposta


def comeOut():
    nomesDasApostas = ['Pass Line Bet', 'Field', 'Any Craps', 'Twelve']
    tiposDeAposta = input("Em qual quer apostar (N para não apostar e sair do jogo)? Ex: PLB,F,AC,T   Digite: ").split(",")
    
    while tiposDeAposta[0] not in ["N", "PLB", "F", "AC", "T"]:
        tiposDeAposta = input("Em qual quer apostar (N para não apostar e sair do jogo)? Ex: PLB,F,AC,T    Digite: ").split(",")
    
    if "N" in tiposDeAposta:
        return ('f', [])
    

    (dado1, dado2, soma) = dados()

    dic = {"PLB": passLineBet, "F": field, "AC": anyCraps, "T": twelve}
    
    lucroOuPrejuizo = []
    lista = [False, soma, 0]

    for aposta in tiposDeAposta:
        
        if aposta == "PLB":
            lista = dic[aposta](soma) # Lista => [bol, soma, aposta]
        
            if lista[0] == False:
                lucroOuPrejuizo.append(lista[2])
            else:
                lucroOuPrejuizo.append(-lista[2])
        else:
            lucroOuPrejuizo.append(dic[aposta](soma))
    
    stats(dado1, dado2, soma)
    
    for e in range(len(lucroOuPrejuizo)):
        if lucroOuPrejuizo[e] > 0:
            print(f"Você ganhou {abs(lucroOuPrejuizo[e])} na aposta {tiposDeAposta[e]}")
        elif lucroOuPrejuizo[e] == 0:
            print(f"Você não ganhou nada na aposta {tiposDeAposta[e]}")
        else:
            print(f"Você perdeu {abs(lucroOuPrejuizo[e])} na aposta {tiposDeAposta[e]}")
    

    
    return (sum(lucroOuPrejuizo), lista)

    
    


def point(somaPoint, aposta, din):
    soma = 0
    while soma not in [7, somaPoint]:
        tiposDeAposta = input("Em qual quer apostar (N para não apostar e rolar os dados)? Ex: AC,T,P   Digite: ").split(",")
        
        while tiposDeAposta[0] not in ["N", "PLB", "F", "AC", "T"]:
            tiposDeAposta = input("Em qual quer apostar (N para não apostar e sair do jogo)? Ex: PLB,F,AC,T   Digite: ").split(",")
        
        (dado1, dado2, soma) = dados()

        if tiposDeAposta[0] != "N":
            dic = {"F": field, "AC": anyCraps, "T": twelve}
            
            lucroOuPrejuizo = []

            for aposta in tiposDeAposta:
                lucroOuPrejuizo.append(dic[aposta](soma))
            
            stats(dado1, dado2, soma)
            
            for e in range(len(lucroOuPrejuizo)):
                if lucroOuPrejuizo[e] > 0:
                    print(f"Você ganhou {abs(lucroOuPrejuizo[e])} na aposta {tiposDeAposta[e]}")
                elif lucroOuPrejuizo[e] == 0:
                    print(f"Você não ganhou nada na aposta {tiposDeAposta[e]}")
                else:
                    print(f"Você perdeu {abs(lucroOuPrejuizo[e])} na aposta {tiposDeAposta[e]}")   
        else:
            stats(dado1, dado2, soma)      
            
    if soma == somaPoint:
        print(f"Você ganhou o Point, recuperou seus {aposta} e voltou para o Come Out!")
        return din + float(aposta)
    else:
        print("Você perdeu o Point e voltou para o Come Out!")
        return din - float(aposta)




din = 100
passou = False

while True:
    (lucroOuPrejuizo, lista) = comeOut()
    if isinstance(lucroOuPrejuizo, str):
        break

    din += lucroOuPrejuizo
    print(f'Saldo atual:{din}')

    if lista[0]: 
        passou = True
        somaPoint = lista[1]
        aposta = lista[2]

    if passou:
        din = point(somaPoint, aposta, din)