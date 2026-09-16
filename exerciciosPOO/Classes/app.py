from Pessoa import Pessoa

#instanciar uma pessoa

print(Pessoa.numero_instancias) #acho que vai retornar 0

p1 = Pessoa(nome="Luane", idade=100, cpf=12345678910, tem_carro=False)

print(Pessoa.numero_instancias) # retorna 1

p2 = Pessoa(nome="Vitor", idade=99, cpf=93187427642, tem_carro=False)


print(Pessoa.numero_instancias) #retorna 2



verifica_se_dirige = p1.dirige()
print(verifica_se_dirige)

print(p1.info())

print(Pessoa.numero_instancias) # retorna x

print(Pessoa.soma(5, 3))
