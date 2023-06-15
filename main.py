class Animal:
    def __init__(self, tipo, idade, cor, porte, particularidade):
        self.tipo = tipo
        self.idade = idade
        self.cor = cor
        self.porte = porte
        self.particularidade = particularidade

class Pessoa:
    def __init__(self, nome, contato, preferencia):
        self.nome = nome
        self.contato = contato
        self.preferencia = preferencia

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)

class SistemaAdocao:
    def __init__(self):
        self.animais_disponiveis = Queue()
        self.pessoas_interessadas = Queue()

    def cadastrar_animal(self, animal):
        self.animais_disponiveis.enqueue(animal)

    def cadastrar_pessoa(self, pessoa):
        self.pessoas_interessadas.enqueue(pessoa)

    def buscar_animais_por_caracteristicas(self, tipo=None, idade=None, cor=None, porte=None, particularidade=None):
        animais_encontrados = []
        queue_copy = Queue()

        while not self.animais_disponiveis.is_empty():
            animal = self.animais_disponiveis.dequeue()
            if (not tipo or animal.tipo == tipo) and \
               (not idade or animal.idade == idade) and \
               (not cor or animal.cor == cor) and \
               (not porte or animal.porte == porte) and \
               (not particularidade or animal.particularidade == particularidade):
                animais_encontrados.append(animal)
            queue_copy.enqueue(animal)

        while not queue_copy.is_empty():
            self.animais_disponiveis.enqueue(queue_copy.dequeue())

        return animais_encontrados

    def buscar_pessoas_por_preferencia(self, tipo):
        pessoas_encontradas = []
        queue_copy = Queue()

        while not self.pessoas_interessadas.is_empty():
            pessoa = self.pessoas_interessadas.dequeue()
            if pessoa.preferencia == tipo:
                pessoas_encontradas.append(pessoa)
            queue_copy.enqueue(pessoa)

        while not queue_copy.is_empty():
            self.pessoas_interessadas.enqueue(queue_copy.dequeue())

        return pessoas_encontradas

    def relatorio_cruzamento_especies(self):
        relatorio = []
        queue_copy = Queue()

        while not self.animais_disponiveis.is_empty():
            animal = self.animais_disponiveis.dequeue()
            pessoas_interessadas = self.buscar_pessoas_por_preferencia(animal.tipo)
            relatorio.append((animal, pessoas_interessadas))
            queue_copy.enqueue(animal)

        while not queue_copy.is_empty():
            self.animais_disponiveis.enqueue(queue_copy.dequeue())

        return relatorio

# Função para mostrar menu de opções
def mostrar_menu():
    print("\n-------- Menu --------")
    print("1. Cadastrar animal")
    print("2. Cadastrar pessoa interessada")
    print("3. Buscar animais por características")
    print("4. Buscar pessoas por preferência")
    print("5. Gerar relatório de cruzamento de espécies")
    print("0. Sair")

# Função para ler uma opção válida do usuário
def ler_opcao():
    while True:
        try:
            opcao = int(input("Digite a opção desejada: "))
            if 0 <= opcao <= 5:
                return opcao
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Opção inválida. Tente novamente.")

# Função para cadastrar um animal
def cadastrar_animal():
    tipo = input("Digite o tipo do animal (cachorro, gato, pássaro): ").lower()
    idade = input("Digite a idade do animal: ").lower()
    cor = input("Digite a cor do animal: ").lower()
    porte = input("Digite o porte do animal (pequeno, médio, grande): ").lower()
    particularidade = input("Digite a particularidade do animal: ").lower()
    animal = Animal(tipo, idade, cor, porte, particularidade)
    sistema_adocao.cadastrar_animal(animal)
    print("Animal cadastrado com sucesso!")

# Função para cadastrar uma pessoa interessada
def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ").lower()
    contato = input("Digite o contato da pessoa: ").lower()
    preferencia = input("Digite a preferência do animal: ").lower()
    pessoa = Pessoa(nome, contato, preferencia)
    sistema_adocao.cadastrar_pessoa(pessoa)
    print("Pessoa cadastrada com sucesso!")

# Função para buscar animais por características
def buscar_animais():
    tipo = input("Digite o tipo do animal (deixe em branco para qualquer tipo): ").lower()
    idade = input("Digite a idade do animal (deixe em branco para qualquer idade): ").lower()
    cor = input("Digite a cor do animal (deixe em branco para qualquer cor): ").lower()
    porte = input("Digite o porte do animal (deixe em branco para qualquer porte): ").lower()
    particularidade = input("Digite a particularidade do animal (deixe em branco para qualquer particularidade): ").lower()
    animais_encontrados = sistema_adocao.buscar_animais_por_caracteristicas(tipo, idade, cor, porte, particularidade)
    if animais_encontrados:
        print("Animais encontrados:")
        for animal in animais_encontrados:
            print("Tipo:", animal.tipo)
            print("Idade:", animal.idade)
            print("Cor:", animal.cor)
            print("Porte:", animal.porte)
            print("Particularidade:", animal.particularidade)
            print("----------------------")
    else:
        print("Nenhum animal encontrado com as características informadas.")

# Função para buscar pessoas por preferência
def buscar_pessoas():
    tipo = input("Digite o tipo de animal de preferência (deixe em branco para qualquer tipo): ").lower()
    pessoas_encontradas = sistema_adocao.buscar_pessoas_por_preferencia(tipo)
    if pessoas_encontradas:
        print("Pessoas encontradas:")
        for pessoa in pessoas_encontradas:
            print("Nome:", pessoa.nome)
            print("Contato:", pessoa.contato)
            print("----------------------")
    else:
        print("Nenhuma pessoa encontrada com a preferência informada.")

# Função para gerar relatório de cruzamento de espécies
def gerar_relatorio():
    relatorio = sistema_adocao.relatorio_cruzamento_especies()
    if relatorio:
        print("Relatório de cruzamento de espécies:")
        for animal, pessoas_interessadas in relatorio:
            print("Animal:")
            print("Tipo:", animal.tipo)
            print("Idade:", animal.idade)
            print("Cor:", animal.cor)
            print("Porte:", animal.porte)
            print("Particularidade:", animal.particularidade)
            print("Pessoas interessadas:")
            for pessoa in pessoas_interessadas:
                print("Nome:", pessoa.nome)
                print("Contato:", pessoa.contato)
                print("----------------------")
    else:
        print("Não há animais disponíveis ou pessoas interessadas para gerar o relatório.")

# Instanciar o sistema de adoção
sistema_adocao = SistemaAdocao()


animal1 = Animal("cachorro", "2 anos", "marrom", "médio", "cauda curta")
animal2 = Animal("gato", "1 ano", "branco", "Pequeno", "manchas pretas")
animal3 = Animal("cachorro", "3 anos", "preto", "grande", "orelhas grandes")
animal4 = Animal("gato", "2 anos", "cinza", "Médio", "rabo comprido")


person1 = Pessoa("joão", "joao@example.com", "cachorro")
person2 = Pessoa("maria", "maria@example.com", "gato")
person3 = Pessoa("pedro", "pedro@example.com", "cachorro")
person4 = Pessoa("ana", "ana@example.com", "gato")


sistema_adocao.cadastrar_animal(animal1)
sistema_adocao.cadastrar_animal(animal2)
sistema_adocao.cadastrar_animal(animal3)
sistema_adocao.cadastrar_animal(animal4)


sistema_adocao.cadastrar_pessoa(person1)
sistema_adocao.cadastrar_pessoa(person2)
sistema_adocao.cadastrar_pessoa(person3)
sistema_adocao.cadastrar_pessoa(person4)


# Loop principal
while True:
    mostrar_menu()
    opcao = ler_opcao()

    if opcao == 0:
        break
    elif opcao == 1:
        cadastrar_animal()
    elif opcao == 2:
        cadastrar_pessoa()
    elif opcao == 3:
        buscar_animais()
    elif opcao == 4:
        buscar_pessoas()
    elif opcao == 5:
        gerar_relatorio()
