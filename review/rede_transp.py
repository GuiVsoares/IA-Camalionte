class Estacao:
    def __init__(self, nome: str, capacidade: int):
        self.nome = nome
        self.capacidade = capacidade


class Cidade:
    def __init__(self, nome: str):
        self.nome = nome
        self.estacoes = []

    def adiciona_estacao(self, estacao: Estacao):
        self.estacoes.append(estacao)

    def lista_estacoes(self):
        print(f"\nCidade: {self.nome}")
        for estacao in self.estacoes:
            print(f"Estação: {estacao.nome} - Capacidade: {estacao.capacidade} passageiros")


class RedeTransporte:
    def __init__(self):
        self.cidades = []

    def adiciona_cidade(self, cidade: Cidade):
        self.cidades.append(cidade)

    def exibe_estacoes_cidade(self, nome_cidade: str):
        for cidade in self.cidades:
            if cidade.nome == nome_cidade:
                cidade.lista_estacoes()
                return
        print(f"Cidade '{nome_cidade}' não encontrada.")


# Criando a rede de transporte e adicionando cidades
rede = RedeTransporte()

sp = Cidade("São Paulo")
sp.adiciona_estacao(Estacao("Estação Luz", 5000))
sp.adiciona_estacao(Estacao("Estação Sé", 8000))

rj = Cidade("Rio de Janeiro")
rj.adiciona_estacao(Estacao("Central do Brasil", 7000))

rede.adiciona_cidade(sp)
rede.adiciona_cidade(rj)

# Exibindo as estações de uma cidade
rede.exibe_estacoes_cidade("São Paulo")
rede.exibe_estacoes_cidade("Rio de Janeiro")
