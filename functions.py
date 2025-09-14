from classes import *
from main import locadora
import os
code = len(locadora.itens) + 1

# --------------------------------------------------- Cadastrar
def cadastro():
    nome = input("Insira seu nome: ")
    cpf = int(input("Insira seu CPF (somente números): "))
    cliente = Cliente(nome, cpf)
    locadora.cadastrarCliente(cliente)
    return cliente

# --------------------------------------------------- Login

def login():
    nome = input("Insira seu nome: ")
    cpf = int(input("Insira seu CPF (somente números): "))
    for cliente in locadora.clientes:
        if nome == cliente.nome and cpf == cliente.cpf:
            print("Login efetuado com sucesso!")
            return cliente
        else:
            print("O usuário e/ou CPF não existem ou não foram encontrados. Certifique-se de que os dados estão corretos.")

# --------------------------------------------------- Menu Principal

def main_menu(cliente: Cliente):
    while True:
        try:
            os.system("cls")
            opcoes = ["1. Locar item", "2. Devolver item", "3. Cadastrar item", "4. Ver itens alugados", "5. Sair"]
            print(locadora.nome)
            for opcao in opcoes:
                print(opcao)
            i = int(input("\n--> "))
            match i:

                case 1:
                    locadora.listItens()
                    item_codigo = int(input("Digite o código do item que você deseja locar: "))
                    for item in locadora.itens:
                        if item_codigo == item.code:
                            cliente.locarProduto(item)

                case 2:
                    cliente.listItems()
                    item_codigo = int(input("Digite o código do item que você gostaria de devolver: "))
                    for item in locadora.itens:
                       if item_codigo == item.code:
                           cliente.devolverProduto(item) 

                case 3:
                    opcoes_cadastro = ["1. Filme", "2. Jogo"]
                    print("Cadastrando item")
                    for opcao in opcoes_cadastro:
                        print(opcao)
                    item_cadastro = int(input("Selecione o que você gostaria de cadastrar: "))
                    match item_cadastro:
                        case 1:
                            nome_filme = input("Insira o nome do filme: ")
                            genero = input("Insira o gênero do filme: ")
                            duracao = input("Insira a duração do filme: ")
                            filme = Filme(code, nome_filme, genero, duracao)
                            locadora.cadastrarItem(filme)
                        case 2:
                            nome_jogo = input("Insira o nome do jogo: ")
                            plataforma = input("Insira a plataforma do jogo: ")
                            class_idade = input("Insira a classificação de idade do jogo: ")
                            jogo = Jogo(code, nome_jogo, plataforma, class_idade)
                            locadora.cadastrarItem(jogo)
                case 4:
                    print("Itens alugados")
                    cliente.listItems()
                case 5:
                    break
        except Exception:
            pass

# ---------------------------------------------------Menu Inicial

def start_menu():
    while True:
        try:
            os.system("cls")
            opcoes = ["1. Cadastrar novo usuário", "2. Entrar com uma conta já existente", "3. Sair"]
            print("Bem-Vindo à locadora EndOfWorld!")
            for opcao in opcoes:
                print(opcao)
            i = int(input("--> "))

            match i:
                case 1:
                    cliente = cadastro()
                    main_menu(cliente)
                case 2:
                    cliente = login()
                    main_menu(cliente)
                case 3:
                    break
        except Exception:
            pass