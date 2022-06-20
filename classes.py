class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def salario(self):
        return self._salario

    def get_bonificacao(self):
        print('Bonificação Funcionário ....')
        return self._salario * 0.10


class Autenticavel:
    def __init__(self, senha):
        self.senha = senha

    def autenticar(self, senha):
        if self.senha == senha:
            print('Acesso OK!')
            return True
        else:
            print('Acesso negado!')
            return False


class Gerente(Funcionario, Autenticavel):

    def __init__(self, nome, cpf, salario, senha, qtd_funcionarios=0):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    @property
    def qtd_funcionarios(self):
        return self._qtd_funcionarios

    def get_bonificacao(self):
        print('Bonificação Gerente ....')
        return self.salario * 0.15

    def __repr__(self):
        return self.nome + ' - ' + self.cpf


class Cliente(Autenticavel):
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha


class SistemaInterno:
    def login(self, objeto):
        try:
            ok = objeto.autenticar(objeto.senha)
            print('Autenticação?', ok)
            return ok
        except AttributeError:
            print('{} não é autenticável' .format(objeto.__class__.__name__))