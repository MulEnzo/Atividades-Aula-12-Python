class Pessoa:
    def __init__(self, nome, email, telefone, idade, sexo=None):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.idade = idade
        self.sexo = sexo


class Aluno(Pessoa):
    def __init__(self, nome, email, telefone, idade, matricula, notas, sexo=None):
        super().__init__(nome, email, telefone, idade, sexo)
        self.matricula = matricula
        self.notas = notas


class Professor(Pessoa):
    def __init__(self, nome, email, telefone, idade, salario, disciplinas=None, sexo=None):
        super().__init__(nome, email, telefone, idade, sexo)
        self.salario = salario
        self.disciplinas = disciplinas


class Secretario(Pessoa):
    def __init__(self, nome, email, telefone, idade, salario, sexo=None):
        super().__init__(nome, email, telefone, idade, sexo)
        self.salario = salario