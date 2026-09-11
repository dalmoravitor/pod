
class ContaBancaria:
    n_instancias = 0
    @classmethod
    def somar_instancia(cls):
        cls.n_instancias += 1


    def __init__(self, numero_conta, nome_titular, tipo_conta, saldo=0):
        ContaBancaria.somar_instancia()
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        print(f"Número de instâncias da classe ContaBancaria: {ContaBancaria.n_instancias}")


    

    #métodos: depositar, sacar
    
    def saldo(self):
        return self.saldo

    
    def set_saldo(self, valor):
        self.saldo += valor

    
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
    



