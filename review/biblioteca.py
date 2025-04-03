class Livro:
    def __init__(self, titulo: str, autor: str, ano: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano


class Biblioteca:
    def __init__(self, nome: str):
        self.nome = nome
        self.livros = []

    def adiciona_livro(self, livro: Livro):
        self.livros.append(livro)

    def lista_livros(self):
        print(f"\nBiblioteca: {self.nome}")
        if not self.livros:
            print("Nenhum livro disponível.")
        for livro in self.livros:
            print(f"{livro.titulo} - {livro.autor} ({livro.ano})")


class SistemaBibliotecas:
    def __init__(self):
        self.bibliotecas = []

    def adiciona_biblioteca(self, biblioteca: Biblioteca):
        self.bibliotecas.append(biblioteca)

    def busca_livro(self, nome_biblioteca: str, titulo: str):
        for biblioteca in self.bibliotecas:
            if biblioteca.nome == nome_biblioteca:
                for livro in biblioteca.livros:
                    if livro.titulo.lower() == titulo.lower():
                        print(f"\nLivro encontrado em '{biblioteca.nome}': {livro.titulo} - {livro.autor} ({livro.ano})")
                        return
                print(f"\nO livro '{titulo}' não foi encontrado na biblioteca '{biblioteca.nome}'.")
                return
        print(f"\nBiblioteca '{nome_biblioteca}' não encontrada.")


# Criando o sistema e adicionando bibliotecas
sistema = SistemaBibliotecas()

biblio_central = Biblioteca("Biblioteca Central")
biblio_central.adiciona_livro(Livro("Dom Quixote", "Miguel de Cervantes", 1605))
biblio_central.adiciona_livro(Livro("1984", "George Orwell", 1949))

biblio_norte = Biblioteca("Biblioteca Norte")
biblio_norte.adiciona_livro(Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954))

sistema.adiciona_biblioteca(biblio_central)
sistema.adiciona_biblioteca(biblio_norte)

# Exibindo os livros disponíveis em cada biblioteca
biblio_central.lista_livros()
biblio_norte.lista_livros()

# Buscando um livro específico
sistema.busca_livro("Biblioteca Central", "1984")
sistema.busca_livro("Biblioteca Norte", "Dom Quixote")
sistema.busca_livro("Biblioteca Sul", "O Senhor dos Anéis")
