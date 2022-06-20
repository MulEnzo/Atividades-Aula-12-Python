class Conta:

    def __init__(self, saldo=0):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo > 0:
            self._saldo = novo_saldo

    def verificar_saldo(self):
        return self._saldo

    def creditar(self, valor):
        if valor > 0:
            self._saldo += valor

    def debitar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor

    def atualizar(self, taxa):
        if taxa > 0:
            self._saldo += self._saldo * taxa


class ContaPoupanca(Conta):

    def __init__(self, saldo=0):
        super().__init__(saldo)

    def atualizar(self, taxa):
        if taxa > 0:
            # self.saldo += self.saldo * 3 * taxa
            super().creditar(self.saldo * 3 * taxa)

    def __repr__(self):
        return str(super().verificar_saldo())


class ContaCorrente(Conta):

    def __init__(self, saldo=0):
        super().__init__(saldo)

    def creditar(self, valor):
        super().creditar(valor)
        super().debitar(2.00)

    def atualizar(self, taxa):
        if taxa > 0:
            # self.saldo += self.saldo * 2 * taxa
            super().creditar(self.saldo * 2 * taxa)

    def __repr__(self):
        return str(super().verificar_saldo())


class ControladorAtualizacoes:
    def __init__(self, taxa=0.01):
        self.taxa = taxa
        self._saldo_total = 0

    @property
    def saldo_total(self):
        return self._saldo_total

    @saldo_total.setter
    def saldo_total(self, novo_valor):
        self._saldo_total = novo_valor

    def atualizar_conta(self, conta):
        try:
            print('\nSaldo Atual:', conta.saldo)
            conta.atualizar(self.taxa)
            self.saldo_total += conta.saldo
            print('\nNovo Saldo:', conta.saldo)
        except AttributeError as e:
            print(e)


if __name__ == '__main__':

    conta_corrente = ContaCorrente(saldo=10000)

    conta_poupanca = ContaPoupanca(saldo=2000)

    controlador = ControladorAtualizacoes(taxa=0.05)

    print('\nConta Corrente:', conta_corrente)
    print('Conta Poupança:', conta_poupanca)

    controlador.atualizar_conta(conta_corrente)

    controlador.atualizar_conta(conta_poupanca)

    controlador.atualizar_conta('OI')

    print('\n\nConta Corrente:', conta_corrente)
    print('Conta Poupança:', conta_poupanca)

    print('\n\nTotal saldo:', controlador.saldo_total)