
class ContaBancaria:
    n_instancias = 0

    @classmethod
    def somar_instancia(cls):
        cls.n_instancias += 1

    def __init__(self, numero_conta, nome_titular, tipo_conta, saldo=0):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        ContaBancaria.somar_instancia()

        print(f"Número de instâncias da classe ContaBancaria: {ContaBancaria.n_instancias}")

    #métodos: depositar, sacar
    def depositar(self, valor):
        if valor < 0:
            return "Erro: não é possível depositar valores negativos à conta."
        elif valor == 0:
            return "Erro: não é possível fazer um depósito de R$0,00 à conta."
        else:
            self.saldo += valor

    def sacar(self, valor):
        if valor < self.saldo and valor > 0: 
            self.saldo -= valor
        else:
            return "Erro: saque acima do saldo disponível"

    #getters e setters (usando decoradores @property)
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def numero_conta(self):
        return self._numero_conta
    
    @numero_conta.setter
    def numero_conta(self, numero):
        self._numero_conta = numero

    @property
    def tipo_conta(self):
        return self._tipo_conta

    @tipo_conta.setter
    def tipo_conta(self, account_type):
        if account_type == "poupanca" or account_type == "investimento" or account_type == "corrente":
            self._tipo_conta = account_type
        else:
            return "erro, forneça um tipo de conta válido"
        
    @property
    def nome_titular(self):
        return self._nome_titular

    @nome_titular.setter
    def nome_titular(self, nome_titular):
        self._nome_titular = nome_titular

