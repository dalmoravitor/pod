from ContaBancaria import ContaBancaria
from Erros import ErroQuantidade

class ContaCorrente(ContaBancaria):
    def __init__(self, limite_saque, numero_conta, nome_titular, saldo=0 ):
        self.limite_saque = limite_saque
        super().__init__(numero_conta, nome_titular, "corrente", saldo)

    
    def sacar(self, valor):
        if valor > self.limite_saque:
            return f"Saque não realizado: valor acima do limite de {self.limite_saque}"
        elif valor <= 0:
            return f"O valor de saque deve ser positivo"
        else:
            return f"saque de {valor} realizado"
        
        

    