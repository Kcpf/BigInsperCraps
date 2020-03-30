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


def come_out(dinheiro):

    print('Voce esta na fase de Come Out')

    dinheiro_apostado = 0
    dinheiro_local = dinheiro
    teste_aposta = 0
    aposta_total = 0
    valida_aposta = False
    lucro = 0
    vai_para_o_point = False
    todas_apostas = {"F": field, "AC": any_craps, "T": twelve}
    lucro_total = 0
    dic = {}
    quantia_apostada_em_cada_aposta = []
    nomes_das_apostas = {"PLB":"Pass Line Bet", "F":"Field", "AC":"Any Craps", "T":"Twelve"}
    tipos_de_aposta = input("Em qual quer apostar (N para não apostar e sair do jogo)? Ex: PLB,F,AC,T   Digite: ").split(",")
    
    while tipos_de_aposta[0] not in ["N", "PLB", "F", "AC", "T"]:
        tipos_de_aposta = input("Em qual quer apostar (N para não apostar e sair do jogo)? Ex: PLB,F,AC,T    Digite: ").split(",")
    
    tipos_de_aposta.sort()

    (dado1, dado2, soma) = dados()


    for tipos in tipos_de_aposta:
        valida_aposta = False
        while valida_aposta == False:
            teste_aposta = int(input(f'Quanto quer apostar no {nomes_das_apostas[tipos]}?    Digite: '))
            aposta_total+=teste_aposta
            if aposta_total <= dinheiro_local and aposta_total >= 0:
                quantia_apostada_em_cada_aposta.append(teste_aposta)
                valida_aposta = True 
            else:
                print('aposta invalida')
                aposta_total-=teste_aposta

    print(stats(dado1, dado2, soma))

    for num in range(len(tipos_de_aposta)):
        dic[tipos_de_aposta[num]] = quantia_apostada_em_cada_aposta[num]

    print(quantia_apostada_em_cada_aposta,tipos_de_aposta,dic)

    for tipos in todas_apostas:

        if tipos in tipos_de_aposta:
            lucro = todas_apostas[tipos](True, dic[tipos], soma)

        else:
            lucro = todas_apostas[tipos](False, 0, soma)
        
        if lucro > 0:
            lucro_total+=lucro
            print(f'Voce ganhou {lucro} no {nomes_das_apostas[tipos]}')

        elif lucro < 0:
            lucro_total+=lucro
            print(f'Voce perdeu {-lucro} no {nomes_das_apostas[tipos]}')

    if "PLB" in tipos_de_aposta:
        lucro, vai_para_o_point, soma = pass_line_bet(True, dic["PLB"], soma)
        if lucro > 0:
            print(f'Voce ganhou {lucro} no {nomes_das_apostas["PLB"]}')
            lucro_total+=lucro
        elif lucro < 0 and vai_para_o_point == False:
            print(f'Voce perdeu {-lucro} no {nomes_das_apostas["PLB"]}')
            lucro_total+=lucro
        elif lucro < 0 and vai_para_o_point == True:
            print("Você foi para o Point!")
            dinheiro_apostado = dic["PLB"]
            lucro_total+=lucro


    dinheiro_local+=lucro_total

    return dinheiro_local, vai_para_o_point, soma, dinheiro_apostado
    
    


def point(dinheiro, soma_dados_point, dinheiro_apostado):
    print('Voce esta na fase de Point')
    soma = 0
    dinheiro_local = dinheiro
    teste_aposta = 0
    aposta_total = 0
    valida_aposta = False
    valida_tipo_aposta = False
    lucro = 0
    todas_apostas = {"F": field, "AC": any_craps, "T": twelve}
    lucro_total = 0
    dic = {}
    quantia_apostada_em_cada_aposta = []
    nomes_das_apostas = {"F":"Field", "AC":"Any Craps", "T":"Twelve"}
    siglas_apostas = ["N", "F", "AC", "T"]
    
    while soma not in [7, soma_dados_point]:
        
        teste_aposta = 0
        aposta_total = 0
        valida_aposta = False
        valida_tipo_aposta = False
        lucro = 0
        lucro_total = 0
        dic = {}
        quantia_apostada_em_cada_aposta = []
            
    
        tipos_de_aposta = input("Em qual quer apostar (N para não apostar e sair do jogo)? Ex: F,AC,T   Digite: ").split(",")

        while valida_tipo_aposta == False:
            for nums in range(len(tipos_de_aposta)):
                if tipos_de_aposta[nums] not in ["N", "F", "AC", "T"]:
                    tipos_de_aposta = input("Em qual quer apostar (N para não apostar e sair do jogo)? Ex: F,AC,T    Digite: ").split(",")
            else:
                valida_tipo_aposta = True
        
        tipos_de_aposta.sort()

        (dado1, dado2, soma) = dados()


        for tipos in tipos_de_aposta:
            valida_aposta = False
            while valida_aposta == False:
                teste_aposta = int(input(f'Quanto quer apostar no {nomes_das_apostas[tipos]}?    Digite: '))
                aposta_total+=teste_aposta
                if aposta_total <= dinheiro_local and aposta_total >= 0:
                    quantia_apostada_em_cada_aposta.append(teste_aposta)
                    valida_aposta = True 
                else:
                    print('aposta invalida')
                    aposta_total-=teste_aposta

        print(stats(dado1, dado2, soma))

        for num in range(len(tipos_de_aposta)):
            dic[tipos_de_aposta[num]] = quantia_apostada_em_cada_aposta[num]

        for tipos in todas_apostas:

            if tipos in tipos_de_aposta:
                lucro = todas_apostas[tipos](True, dic[tipos], soma)

            else:
                lucro = todas_apostas[tipos](False, 0, soma)
            
            if lucro > 0:
                lucro_total+=lucro
                print(f'Voce ganhou {lucro} no {nomes_das_apostas[tipos]}')

            elif lucro < 0:
                lucro_total+=lucro
                print(f'Voce perdeu {-lucro} no {nomes_das_apostas[tipos]}')

            dinheiro_local+=lucro_total


    if soma == soma_dados_point:
        print(f"Você ganhou o Point, recuperou suas {dinheiro_apostado} fichas apostadas e voltou para o Come Out!")
        return dinheiro_local + dinheiro_apostado, False
    else:
        print("Você perdeu o Point e voltou para o Come Out!")
        return dinheiro_local, False




def main():
    quer_jogar = True
    esta_no_point = False
    dinheiro = 1000
    dinheiro_apostado = 0
    soma_dados_point = 0

    vamos_jogar = input("""Bem vindo ao Big Insper Craps!
Vamos jogar?
digite 'S' para jogar e 'N' para sair    Digite: """)

    if vamos_jogar == 'N':
        quer_jogar = False
    
    else:
        print('Voce ira iniciar com 1000 fichas')


    while quer_jogar:
        if dinheiro <= 0 and dinheiro_apostado <= 0:
            print('Que pena! Suas fichas acabaram')
            break
        elif not esta_no_point:
            dinheiro_local, vai_para_o_point, soma, dinheiro_apostado = come_out(dinheiro)
            dinheiro = dinheiro_local
            esta_no_point = vai_para_o_point
            soma_dados_point = soma
            if dinheiro_apostado == 0:
                print(f'Seu saldo atual é de {dinheiro} fichas')
            else: 
                print(f'Seu saldo atual é de {dinheiro} fichas e voce possui {dinheiro_apostado} fichas apostadas')

        elif esta_no_point:
            dinheiro_local, esta_no_point = point(dinheiro, soma_dados_point, dinheiro_apostado)
            dinheiro = dinheiro_local
            print(f'Seu saldo atual é de {dinheiro} fichas')


        vamos_jogar = input("""Quer continuar jogando?
digite 'S' para continuar e 'N' para sair    Digite: """)

        if vamos_jogar == 'N':
            quer_jogar = False
            

    
    
    return('Obrigado por jogar! Até a próxima')