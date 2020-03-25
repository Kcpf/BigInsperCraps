import random

def dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2


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
                
            else:
                din -= aposta
                print(f'Saldo atual: {din}')
                print(f'Valor apostado: {aposta}')
    
    break
        




