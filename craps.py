# -*- coding: utf-8 -*-
"""
@author: Fernando Franca and Francisco Costa

Objetivo do Código: Implementar uma versão simplificada do jogo Craps em Python
"""

import random

dados_desenho = {1:"""
 -------
|       |
|   *   |
|       |
 ------- 
""", 2:"""
 -------
| *     |
|       |
|     * |
 ------- 
""", 3:"""
 -------
| *     |
|   *   |
|     * |
 -------
 """, 4:"""
 -------
| *   * |
|       |
| *   * |
 -------
  """, 5:"""
 -------
| *   * |
|   *   |
| *   * |
 -------
  """, 6:"""
 -------
| *   * |
| *   * |
| *   * |
 -------"""}
 
titulo = """\n /$$$$$$$  /$$$$$$  /$$$$$$                               
| $$__  $$|_  $$_/ /$$__  $$                              
| $$  \ $$  | $$  | $$  \__/                              
| $$$$$$$   | $$  | $$ /$$$$                              
| $$__  $$  | $$  | $$|_  $$                              
| $$  \ $$  | $$  | $$  \ $$                              
| $$$$$$$/ /$$$$$$|  $$$$$$/                              
|_______/ |______/ \______/                               
 /$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
|_  $$_/| $$$ | $$ /$$__  $$| $$__  $$| $$_____/| $$__  $$
  | $$  | $$$$| $$| $$  \__/| $$  \ $$| $$      | $$  \ $$
  | $$  | $$ $$ $$|  $$$$$$ | $$$$$$$/| $$$$$   | $$$$$$$/
  | $$  | $$  $$$$ \____  $$| $$____/ | $$__/   | $$__  $$
  | $$  | $$\  $$$ /$$  \ $$| $$      | $$      | $$  \ $$
 /$$$$$$| $$ \  $$|  $$$$$$/| $$      | $$$$$$$$| $$  | $$
|______/|__/  \__/ \______/ |__/      |________/|__/  |__/
  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$         
 /$$__  $$| $$__  $$ /$$__  $$| $$__  $$ /$$__  $$        
| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$| $$  \__/        
| $$      | $$$$$$$/| $$$$$$$$| $$$$$$$/|  $$$$$$         
| $$      | $$__  $$| $$__  $$| $$____/  \____  $$        
| $$    $$| $$  \ $$| $$  | $$| $$       /$$  \ $$        
|  $$$$$$/| $$  | $$| $$  | $$| $$      |  $$$$$$/        
 \______/ |__/  |__/|__/  |__/|__/       \______/    
    \n"""


def dados():
    """
    Função com o objetivo de 'rolar' os dados.
	
	Args: None.

	Returns:
		dado1(int): Valor do dado1 gerado aleatoriamente.
		dado2(int): Valor do dado2 gerado aleatoriamente.
		soma(int): Valor da soma dos dados 1 e 2.
    """
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2

    return dado1, dado2, soma

def stats(dado1, dado2, soma):
    """
	Função com o objetivo de informar os valores dos dados graficamente.

	Args:
		dado1(int): Valor do dado1 gerado aleatoriamente.
		dado2(int): Valor do dado2 gerado aleatoriamente.
		soma(int): Valor da soma dos dados 1 e 2.

	Returns:
		(String) Informando quais são os valores dos dados graficamente.
	"""

    while True:
        if input("Aperte F para rodar dado? ").lower() == "f": break

    return(f"Dado 1: {dados_desenho[dado1]}\n Dado 2: {dados_desenho[dado2]}")

def field(vai_apostar, valor_da_aposta, soma):
    """
	Função que executa a aposta do tipo Field.

	Args:
		vai_apostar(bool): Booleano informando se o usuário vai apostar ou não.
		valor_da_aposta(float): Valor da quantidade de dinheiro que o usuário quer apostar.
		soma(int): Valor da soma dos dados 1 e 2.

	Returns:
		valor_da_aposta(int): Lucro ou prejuízo que o usuário teve.
	"""

    if vai_apostar:
        if soma in [5, 6, 7, 8]:
            return -valor_da_aposta
        elif soma in [3, 4, 9, 10, 11]:
            return valor_da_aposta
        elif soma == 2:
            return valor_da_aposta * 2
        elif soma == 12:
            return valor_da_aposta * 3
            
    return 0

def any_craps(vai_apostar, valor_da_aposta, soma):
    """
	Função que executa a aposta do tipo Any Craps.

	Args:
		vai_apostar(bool): Booleano informando se o usuário vai apostar ou não.
		valor_da_aposta(float): Valor da quantidade de dinheiro que o usuário quer apostar.
		soma(int): Valor da soma dos dados 1 e 2.

	Returns:
		valor_da_aposta(int): Lucro ou prejuízo que o usuário teve.
	"""

    if vai_apostar:
        if soma in [2, 3, 12]:
            return valor_da_aposta * 7
        else:
            return -valor_da_aposta
            
    return valor_da_aposta

def twelve(vai_apostar, valor_da_aposta, soma):
    """
	Função que executa a aposta do tipo Twelve.

	Args:
		vai_apostar(bool): Booleano informando se o usuário vai apostar ou não.
		valor_da_aposta(float): Valor da quantidade de dinheiro que o usuário quer apostar.
		soma(int): Valor da soma dos dados 1 e 2.

	Returns:
		valor_da_aposta(int): Lucro ou prejuízo que o usuário teve.
	"""

    if vai_apostar:
        if soma == 12:
            return valor_da_aposta * 30
        else:
            return -valor_da_aposta
        
    return valor_da_aposta

def pass_line_bet(vai_apostar, valor_da_aposta, soma):
    """
	Função que executa a aposta do tipo Pass Line Bet.

	Args:
		vai_apostar(bool): Booleano informando se o usuário vai apostar ou não.
		valor_da_aposta(float): Valor da quantidade de dinheiro que o usuário quer apostar.
		soma(int): Valor da soma dos dados 1 e 2.

	Returns:
		valor_da_aposta(int): Lucro ou prejuízo que o usuário teve.
		bool: informando se o usuário foi para o Point ou não.
		soma(int): Soma dos dados que será usada para o Point
	"""

    if soma in [2, 3, 12]:
        return (-valor_da_aposta, False, soma)
    elif soma in [4, 5, 6, 8, 9, 10]:
        return (-valor_da_aposta, True, soma)
    
    return (valor_da_aposta, False, soma)

def come_out(dinheiro):
    """
	Função que executa a rodada do Come Out
	
	Args: 
		dinheiro(float): Saldo atual que o usuário possui. 

	Returns:
		dinheiro(float): Saldo que o usuário possui depois do Come Out.
		vai_para_o_point(bool): Informa se o usuário vai para o Point ou não.
		soma(int): Soma dos dados que será usada no Point.
		dic["PLB"](float): Valor da aposta do Pass Line Bet
		 
	"""

    print('Você está na fase de Come Out')
    vai_para_o_point = False
    aposta_total = 0
    todas_apostas = {"F": field, "AC": any_craps, "T": twelve, "PLB": pass_line_bet}
    lucro_total = 0
    dic = {}
    quantia_apostada_em_cada_aposta = []
    nomes_das_apostas = {"PLB":"Pass Line Bet", "F":"Field", "AC":"Any Craps", "T":"Twelve"}

    tipos_de_aposta = input("Em qual quer apostar (N para não apostar e sair do jogo)? Ex: PLB,F,AC,T   Digite: ").split(",")
    
    while tipos_de_aposta[0] not in ["N", "PLB", "F", "AC", "T"]:
        tipos_de_aposta = input("Em qual quer apostar (N para não apostar e sair do jogo)? Ex: PLB,F,AC,T    Digite: ").split(",")
    

    if "PLB" in tipos_de_aposta:
        tipos_de_aposta.remove("PLB")
        tipos_de_aposta.append("PLB")

    (dado1, dado2, soma) = dados()


    for tipos in tipos_de_aposta:
        while True:
            teste_aposta = int(input(f'Quanto quer apostar no {nomes_das_apostas[tipos]}?    Digite: '))
            aposta_total+=teste_aposta

            if aposta_total <= dinheiro and aposta_total >= 0:
                quantia_apostada_em_cada_aposta.append(teste_aposta)
                break
            else:
                print('Aposta Invalida')
                aposta_total-=teste_aposta

    print(stats(dado1, dado2, soma))

    for num in range(len(tipos_de_aposta)):
        dic[tipos_de_aposta[num]] = quantia_apostada_em_cada_aposta[num]

    for tipos in tipos_de_aposta:
        if tipos == "PLB":
            lucro, vai_para_o_point, soma = pass_line_bet(True, dic[tipos], soma)
        else:
            lucro = todas_apostas[tipos](True, dic[tipos], soma)

        lucro_total += lucro
        
        if lucro > 0:
            print(f'Você ganhou {lucro} no {nomes_das_apostas[tipos]}')
        
        elif lucro < 0 and vai_para_o_point == True:
            print("Você foi para o Point!")

        elif lucro < 0:
            print(f'Você perdeu {-lucro} no {nomes_das_apostas[tipos]}')
        
    
    dinheiro+=lucro_total

    return dinheiro, vai_para_o_point, soma, dic["PLB"] if vai_para_o_point else 0

def point(dinheiro, soma_dados_point, dinheiro_apostado):
    """
	Função que executa as rodadas do Point
	
	Args: 
		dinheiro(float): Saldo atual que o usuário possui.
		soma_dados_point(int): Soma dos dados usado para sair do Point.
		dinheiro_apostado(float): Dinheiro apostado no Point. 

	Returns:
		dinheiro(float): Saldo que o usuário possui depois do Come Out.
		bool: Informando se o usuário está no Point.
		 
	"""

    soma = 0
    aposta_total = 0
    todas_apostas = {"F": field, "AC": any_craps, "T": twelve}
    lucro_total = 0
    dic = {}
    quantia_apostada_em_cada_aposta = []
    nomes_das_apostas = {"F":"Field", "AC":"Any Craps", "T":"Twelve"}
    
    while soma not in [7, soma_dados_point]:
        print('Você está na fase de Point')
        
        tipos_de_aposta = input("Em qual quer apostar (N para não apostar)? Ex: F,AC,T   Digite: ").split(",")
    
        while tipos_de_aposta[0] not in ["N", "PLB", "F", "AC", "T"]:
            tipos_de_aposta = input("Em qual quer apostar (N para não apostar)? Ex: F,AC,T    Digite: ").split(",")
        

        (dado1, dado2, soma) = dados()

        if tipos_de_aposta[0] != "N":
            for tipos in tipos_de_aposta:
                while True:
                    teste_aposta = int(input(f'Quanto quer apostar no {nomes_das_apostas[tipos]}?    Digite: '))
                    aposta_total+=teste_aposta

                    if aposta_total <= dinheiro and aposta_total >= 0:
                        quantia_apostada_em_cada_aposta.append(teste_aposta)
                        break
                    else:
                        print('Aposta Inválida!')
                        aposta_total-=teste_aposta

            print(stats(dado1, dado2, soma))

            for num in range(len(tipos_de_aposta)):
                dic[tipos_de_aposta[num]] = quantia_apostada_em_cada_aposta[num]

            for tipos in tipos_de_aposta:

                lucro = todas_apostas[tipos](True, dic[tipos], soma)

                lucro_total += lucro
                
                if lucro > 0:
                    print(f'Você ganhou {lucro} no {nomes_das_apostas[tipos]}')

                elif lucro < 0:
                    print(f'Você perdeu {-lucro} no {nomes_das_apostas[tipos]}')
                
            
            dinheiro+=lucro_total

        else:
            print(stats(dado1, dado2, soma))
            print("Você não apostou e so rolou os dados")
        
        print(f'Seu saldo atual é de {dinheiro} fichas')

    if soma == soma_dados_point:
        print(f"Você ganhou o Point, recuperou suas {dinheiro_apostado} fichas apostadas e voltou para o Come Out!")
        return dinheiro + dinheiro_apostado, False
    else:
        print("Você perdeu o Point e voltou para o Come Out!")
        return dinheiro, False

def main():
    """
	Função principal que roda o jogo.
	
	Args: None.

	Returns: None.
		 
	"""
    
    quer_jogar = True
    esta_no_point = False
    dinheiro = 1000
    dinheiro_apostado = 0

    print(titulo)

    vamos_jogar = input("""Bem vindo ao Big Insper Craps!\nVamos jogar?\nDigite 'S' para jogar e 'N' para sair    Digite: """)

    if vamos_jogar == 'N':
        quer_jogar = False
    
    else:
        print('Você irá iniciar com 1000 fichas')


    while quer_jogar:
        if dinheiro <= 0 and dinheiro_apostado <= 0:
            print('Que pena! Suas fichas acabaram')
            break

        elif not esta_no_point:
            dinheiro, esta_no_point, soma_dados_point, dinheiro_apostado = come_out(dinheiro)

            if dinheiro_apostado == 0:
                print(f'Seu saldo atual é de {dinheiro} fichas')
            else: 
                print(f'Seu saldo atual é de {dinheiro} fichas e você possui {dinheiro_apostado} fichas apostadas')

        elif esta_no_point:
            dinheiro, esta_no_point = point(dinheiro, soma_dados_point, dinheiro_apostado)


        vamos_jogar = input("""Quer continuar jogando?\nDigite 'S' para continuar e 'N' para sair    Digite: """)

        if vamos_jogar == 'N':
            quer_jogar = False
            
    print('Obrigado por jogar! Até a próxima')
    
    return None


main()
