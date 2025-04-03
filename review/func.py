class Funcionario:
    def __init__(self, nome: str, idade: int, cpf:str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Departamento:
    def __init__(self, nome: str):
        self.nome = nome
        self.funcionarios = []

    def adiciona_funcionario(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)

    def lista_funcionarios(self):

        print(f"Departamento: {self.nome}")

        for funcionario in self.funcionarios:
            print(f"Funcionário: {funcionario.nome} \n Idade: {funcionario.idade} \n CPF: {funcionario.cpf}")

class Empresa:
    def __init__(self):
        
        self.marketing = Departamento("Marketing")
        self.marketing.adiciona_funcionario(Funcionario("Guilherme Soares",20,"52639099850"))
        self.marketing.adiciona_funcionario(Funcionario("Carlos Soares",20,"34639264150"))
        self.marketing.adiciona_funcionario(Funcionario("Ryan Rodrigues",22,"13489326481"))

if __name__ == "__main__":
    empresa = Empresa()
    print("\nExecutando a listagem de funcionários...\n")
    empresa.marketing.lista_funcionarios()