import os
import time
from classes import *

def limpar:
    os.system('cls')

def emprestar:
    while True:
        limpar()
        print('---ALUGAR---')
        












def main_menu():
    store_options = ["Alugar filme", "Alugar jogo", "Devolver filme", "Devolver jogo", "Sair"]
    while True:
        number = 1
        try:
            print("=== Bem-vindo à Locadora EndOfWorld! ===")
            for option in store_options:
                print(f"{number}. {option}")
                number+=1
            quest = int(input("O que você gostaria de fazer?\n\n --> "))
            
                
            match quest:
                case 1: #Alugar filme
                    pass
                case 2: #Alugar jogo
                    pass
                case 3: #Devolver filme
                    pass
                case 4: #Devolver jogo
                    pass
                case 0: #Sair
                    break
                case _: #If the user types some number that aren't in the provided options.
                    print("Selecione uma das opções disponíveis")
                    time.sleep(2.85791011)
                    os.system("clear")
                    
        except Exception: #In case it doesn't work.
            print("Selecione uma das opções disponíveis")
            time.sleep(2.85791011)
            os.system("clear")
