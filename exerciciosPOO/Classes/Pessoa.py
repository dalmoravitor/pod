
class Pessoa:
    """Aqui você explica o que a classe faz ou os métodos dels"""

    numero_instancias = 0

    @classmethod
    def soma_instancias(cls):
        cls.numero_instancias +=1

    def __init__(self, nome, idade, cpf, tem_carro):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.tem_carro = tem_carro
        Pessoa.soma_instancias()
        
    def dirige(self):
        if self.idade >= 18 and self.tem_carro == True:
            return True
        else:
            return False

    def info(self):
        return f"Nome {self.nome}, idade: {self.idade}, cpf: {self.cpf}, tem carro: {self.tem_carro}"

    @classmethod
    def mostra_numero_de_instancias(cls):
        cls.numero_instancias

    @staticmethod
    def FRASE_MOTIVACIONAL():
        print('ABRACADABRA!')

    @staticmethod
    def soma(a, b):
        return a+b