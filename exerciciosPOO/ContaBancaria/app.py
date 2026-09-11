from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente
from ContaInvestimento import ContaInvestimento
from ContaPoupanca import ContaPoupanca

c1 = ContaBancaria(123456, 'Vitor', 'corrente', 1000)
c2 = ContaInvestimento(123412, 'Jorge', 'investimento', 378)
c3 = ContaPoupanca(123123, 'Lisa', 'poupanca', 787)

c1.depositar(248.32)
print(c1.saldo)

c4 = ContaCorrente(limite_saque=530, numero_conta=123256, nome_titular='Alex', saldo=1000)
c4.depositar(800)
print(c4.saldo)

print(c4.sacar(5344))

