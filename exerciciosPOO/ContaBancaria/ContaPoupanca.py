from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    taxa_juros_anual = 0.085
    def __init__(self, numero_conta, nome_titular, saldo):
        super().__init__(numero_conta, nome_titular, "poupanca", saldo)


    # método: aplicação de juros
    def aplicar_rendimento(self):
        if self.saldo > 0:
            self.saldo += self.saldo * self.taxa_juros_anual
        