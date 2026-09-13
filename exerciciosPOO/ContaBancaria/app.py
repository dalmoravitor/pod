# importando as classes
from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente
from ContaInvestimento import ContaInvestimento
from ContaPoupanca import ContaPoupanca

# criando instâncias das classes
c1 = ContaBancaria(nome_titular='Vitor',numero_conta=123456, tipo_conta='corrente', saldo=1000)
c2 = ContaInvestimento(numero_conta=123412, nome_titular='Jorge', perfil_investidor='conservador' , saldo=378)
c3 = ContaPoupanca(numero_conta=123123, nome_titular='Lisa',  saldo=787)
c4 = ContaCorrente(limite_saque=530, numero_conta=123256, nome_titular='Alex', saldo=1000)

# testando a c1:
print("\nDados da conta base (c1):")

print(c1.nome_titular, c1.numero_conta, c1.tipo_conta, c1.saldo)

#testando a c2
print("\nDados da conta investimento (c2):")
print(f"Nome do titular: {c2.nome_titular}")
print(f"Perfil do investidor: {c2.perfil_investimento}")

c2.perfil_investimento = "arriscado"
print(f"Perfil do investidor após a troca: {c2.perfil_investimento}")


#testando a c3
print("\nDados da conta pouppança (c2):")

print(f"Taxa de juros anual da conta poupança: {c3.taxa_juros_anual}")