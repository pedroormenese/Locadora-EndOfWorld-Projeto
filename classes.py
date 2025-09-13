num = 1

class Cliente:
    pass

class Item:
    pass

#----------------------------------------------------

class Locadora:
    def __init__(self, nome, cidade):
        self.nome = nome
        self.cidade = cidade
        self.clientes = []
        self.itens = []

    def listClientes(self):
        for cliente in self.clientes:
            print(f"{cliente}\n")

    def listItens(self):
        for item in self.itens:
            if isinstance(item, Filme):
                print(f"{item}\n")

        for item in self.itens:
            if isinstance(item, Jogo):
                print(f"{item}\n")

    def cadastrarCliente(self, cliente: Cliente):
        cliente = Cliente(cliente)
        self.itens.append(cliente)

    def cadastrarItem(self, item: Item):
        item = Item(item)
        self.itens.append(item)

# ---------------------------------------------------

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.itensLocados = []

    def listItems(self):
        for item in self.alugados:
            if isinstance(item, Filme):
                print("\n")
                print(f"Código: {item.code}\nNome: {item.nome}\nGênero: {item.genero}\nDuração: {item.duracao}\n")
            elif isinstance(item, Jogo):
                print("\n")
                print(f"Código: {item.code}\nNome: {item.nome}\nPlataforma: {item.plataforma}\nFaixa Etária: {item.class_idade}\n")

    def locarProduto(self, item: Item):
        if item.status == True:
            self.itensLocados.append(item)
            self.item.locar()
            if isinstance(item, Filme):
                print("Seu filme foi locado com sucesso. Aproveite a pipoca!")
            elif isinstance(item, Jogo):
                print("Seu jogo foi locado com sucesso. Aproveite a gameplay!")
        else:
            print("Você não pode alocar este item porque ele já está locado.")

    def devolverProduto(self, item: Item):
        if item.status == True:
            print("Você não pode devolver esse produto porque ele não está locado.")
        else:
            self.item.devolver()
            print("O item foi devolvido com sucesso. Obrigado pela preferência!")
        
# ---------------------------------------------------

class Item:
    def __init__(self, code, nome):
        self.nome = nome
        self.code = code
        self.status = True #Se o Status for True = Disponível. Se o Status for False = Indisponível

    def locar(self):
        self.status = False

    def devolver(self):
        self.status = True


# ---------------------------------------------------
# ----------------------------------- Subclasses

class Filme(Item):
    def __init__(self, code, nome, genero, duracao):
        super().__init__(code, nome)
        self.nome = nome
        self.code = code
        self.genero = genero
        self.duracao = duracao


class Jogo(Item):
    def __init__(self, code, nome, plataforma, class_idade):
        super().__init__(code, nome)
        self.code = code
        self.nome = nome
        self.plataforma = plataforma
        self.class_idade = class_idade
