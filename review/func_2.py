class Funcionario:
    def __init__(self, nome: str, idade: int, cpf: str):
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
        if not self.funcionarios:
            print(f"O departamento {self.nome} não tem funcionários cadastrados.")
            return
        
        print(f"\nDepartamento: {self.nome}\n")
        for funcionario in self.funcionarios:
            print(f"Funcionário: {funcionario.nome} \nIdade: {funcionario.idade} \nCPF: {funcionario.cpf}")

class Empresa:
    def __init__(self):
        self.departamentos = {}

    def adiciona_departamento(self, departamento: Departamento):
        self.departamentos[departamento.nome.lower()] = departamento  # 🔹 Armazena o nome do departamento em minúsculas

    def listar_funcionarios_por_departamento(self, nome_departamento: str):
        departamento = self.departamentos.get(nome_departamento.lower())  # 🔹 Busca sem diferenciar maiúsculas/minúsculas
        if departamento:
            departamento.lista_funcionarios()
        else:
            print(f"\nDepartamento '{nome_departamento}' não encontrado.")

# Criando a empresa e adicionando departamentos
empresa = Empresa()

marketing = Departamento("Marketing")
marketing.adiciona_funcionario(Funcionario("Guilherme Soares", 20, "52639099850"))
marketing.adiciona_funcionario(Funcionario("Carlos Soares", 20, "34639264150"))

ti = Departamento("TI")
ti.adiciona_funcionario(Funcionario("Ana Oliveira", 25, "12345678900"))
ti.adiciona_funcionario(Funcionario("Bruno Souza", 30, "98765432100"))

rh = Departamento("RH")
rh.adiciona_funcionario(Funcionario("Alice Mendes", 32, "12345678900"))
rh.adiciona_funcionario(Funcionario("João Martins", 28, "98765432100"))

backoffice = Departamento("Backoffice")
backoffice.adiciona_funcionario(Funcionario("Ricardo Silva", 40, "11122233344"))
backoffice.adiciona_funcionario(Funcionario("Marina Souza", 37, "55566677788"))

dev = Departamento("Dev")
dev.adiciona_funcionario(Funcionario("Gabriel Almeida", 25, "11223344556"))
dev.adiciona_funcionario(Funcionario("Fernanda Costa", 29, "22334455667"))

cs = Departamento("CS")
cs.adiciona_funcionario(Funcionario("Carla Ramos", 27, "33445566778"))
cs.adiciona_funcionario(Funcionario("Bruno Lima", 30, "44556677889"))

dp = Departamento("DP")
dp.adiciona_funcionario(Funcionario("Pedro Santos", 35, "55667788990"))
dp.adiciona_funcionario(Funcionario("Juliana Ferreira", 31, "66778899001"))

financeiro = Departamento("Financeiro")
financeiro.adiciona_funcionario(Funcionario("Marta Oliveira", 45, "77889900112"))
financeiro.adiciona_funcionario(Funcionario("Carlos Henrique", 50, "88990011223"))

suporte = Departamento("Suporte")
suporte.adiciona_funcionario(Funcionario("Diego Nascimento", 26, "99001122334"))
suporte.adiciona_funcionario(Funcionario("Larissa Moraes", 24, "00112233445"))

# Adicionando os departamentos na empresa
empresa.adiciona_departamento(marketing)
empresa.adiciona_departamento(ti)
empresa.adiciona_departamento(rh)
empresa.adiciona_departamento(backoffice)
empresa.adiciona_departamento(dev)
empresa.adiciona_departamento(cs)
empresa.adiciona_departamento(dp)
empresa.adiciona_departamento(financeiro)
empresa.adiciona_departamento(suporte)

# 🔹 Input do usuário para escolher um departamento
departamento_desejado = input("\nDigite o nome do departamento para listar os funcionários: ")
empresa.listar_funcionarios_por_departamento(departamento_desejado)
