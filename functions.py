from classes import *
import os

locadora = Locadora("EndOfWorld", "Sorocaba")

locadora.cadastrarItem(Filme(1, "Meus 84m", "Terror Psicológico", "1h58min"))
locadora.cadastrarItem(Filme(2, "Fuja", "Terror", "1h30min"))
locadora.cadastrarItem(Filme(3, "Meu ano em Oxford", "Drama", "1h52min"))
locadora.cadastrarItem(Filme(4, "Até que as cores acabem", "Drama", "1h58min"))
locadora.cadastrarItem(Jogo(5, "007 Golden Eye", "Nintendo 64", "+12"))
locadora.cadastrarItem(Jogo(6, "Sonic Adventures 2", "Dreamcast", "+10"))
locadora.cadastrarItem(Jogo(7, "Super Mario Bros 3", "NES", "Livre"))
locadora.cadastrarItem(Jogo(8, "Alex Kidd in the Micacle World", "Master System", "Livre"))


# --------------------------------------------------- Cadastrar
def cadastro():
    os.system("cls")
    nome = input("Insira seu nome: ")
    cpf = int(input("Insira seu CPF (somente números): "))
    cliente = Cliente(nome, cpf)
    locadora.cadastrarCliente(cliente)
    return cliente

# --------------------------------------------------- Login

def login():
    os.system("cls")
    nome = input("Insira seu nome: ")
    cpf = int(input("Insira seu CPF (somente números): "))
    if not locadora.clientes:
        print("O usuário e/ou CPF não existem ou não foram encontrados. Certifique-se de que os dados estão corretos.")
        os.system("pause")
    else:
        for cliente in locadora.clientes:
            if nome == cliente.nome and cpf == cliente.cpf:
                print("Login efetuado com sucesso!")
                os.system("pause")
                return cliente
            else:
                print("O usuário e/ou CPF não existem ou não foram encontrados. Certifique-se de que os dados estão corretos.")
                os.system("pause")

# --------------------------------------------------- Menu Principal

def mainmenu(cliente: Cliente):
    while True:
        try:
            os.system("cls")
            opcoes = ["1. Locar item", "2. Devolver item", "3. Cadastrar item", "4. Ver itens alugados", "5. Sair"]
            print(locadora.nome)
            print("\n")
            print(f"Bem-vindo {cliente.nome}")
            for opcao in opcoes:
                print(opcao)
            i = int(input("\n--> "))
            match i:

                case 1:
                    os.system("cls")
                    locadora.listItens()
                    item_codigo = int(input("Digite o código do item que você deseja locar: "))
                    item_encontrado = False
                    for item in locadora.itens:
                        if item_codigo == item.code:
                            cliente.locarProduto(item)
                            item_encontrado = True
                            os.system("pause")
                            break
                    if not item_encontrado:
                        print("O produto não existe ou não foi encontrado")
                        os.system("pause")

                case 2:
                    item_devolver = False
                    cliente.listItems()
                    item_codigo = int(input("Digite o código do item que você gostaria de devolver: "))
                    for item in locadora.itens:
                       if item in cliente.itensLocados and item_codigo == item.code:
                           cliente.devolverProduto(item)
                           item_devolver = True
                           os.system("pause")
                    if not item_devolver:
                        print("O item não foi encontrado ou você não o alugou")
                        os.system("pause")

                case 3:
                    opcoes_cadastro = ["1. Filme", "2. Jogo"]
                    print("Cadastrando item")
                    for opcao in opcoes_cadastro:
                        print(opcao)
                    item_cadastro = int(input("Selecione o que você gostaria de cadastrar: "))
                    match item_cadastro:
                        case 1:
                            code = len(locadora.itens) + 1
                            nome_filme = input("Insira o nome do filme: ")
                            genero = input("Insira o gênero do filme: ")
                            duracao = input("Insira a duração do filme: ")
                            filme = Filme(code, nome_filme, genero, duracao)
                            locadora.cadastrarItem(filme)
                        case 2:
                            code = len(locadora.itens) + 1
                            nome_jogo = input("Insira o nome do jogo: ")
                            plataforma = input("Insira a plataforma do jogo: ")
                            class_idade = input("Insira a classificação de idade do jogo: ")
                            jogo = Jogo(code, nome_jogo, plataforma, class_idade)
                            locadora.cadastrarItem(jogo)
                case 4:
                    os.system("cls")
                    print("Itens alugados")
                    cliente.listItems()
                    os.system("pause")
                case 5:
                    break
        except Exception as e:
            print(f"Erro: {e}")

# ---------------------------------------------------Menu Inicial

def startmenu():
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
                    os.system("cls")
                    mainmenu(cliente)
                case 2:
                    cliente = login()
                    if cliente is not None:
                        mainmenu(cliente)
                case 3:
                    break
        except Exception as e:
            print(f"Erro: {e}")