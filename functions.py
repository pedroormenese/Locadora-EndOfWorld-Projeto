import os
import time
from classes import *

filme1 = Film('01', 'Titanic' 'Romance' '3h14min')
filme2 = Film('02,', 'Laranja Mecânica', 'Comédia', '2h16min')
filme3 = Film('03', 'Clube da Luta', 'Ação', '2h19')
filme4 = Film('04', 'Coringa', 'Drama', '2h2min')
filme5 = Film('05', 'The Batman', 'Ação', '2h56min')
filme6 = Film('06', 'Wicked', 'Musical', '2h40min')
filme7 = Film('07', 'Forrest Gump: O Contador de Histórias', 'Comédia', '2h22min')
filme8 = Film('08', 'Taxi Driver', 'Suspense', '1h54min')

lista_de_filmes = [filme1, filme2, filme3, filme4, filme5, filme6, filme7, filme8]

locadora = RentalStore("Locadora EndOfWorld", "Sorocaba")
for filme in lista_de_filmes:
    locadora.newItem(filme)
# ----------------------------------------------------------

def clean():
    time.sleep(2)
    os.system("cls")

# ----------------------------------------------------------

def rent(): #Função alugar filme
    while True:
        try:
            i = int(input("Você gostaria de ver a lista dos produtos disponíveis?\n\n--> "))
            match i:
                case 1: #Se sim
                    print("Mostrando produtos")
                    locadora.listFilms() #Arruma formatação depois

                case 2:
                    pass
                case _:
                    print("Selecione uma das opções disponíveis")
                    clean()
            
            
        except Exception:
            print("Selecione uma das opções disponíveis")
            clean()

# ----------------------------------------------------------

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
                    rent()
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
                    clean()
                    
        except Exception: #In case it doesn't work.
            print("Selecione uma das opções disponíveis")
            clean()
