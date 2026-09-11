from ContaBancaria import ContaBancaria

class ContaInvestimento(ContaBancaria):
    taxa_juros = 0

    
    '''
    Baixo risco: selic rendendo 1%a.m "conservador"
    Alto risco: derivativo x podendo render algo entre 5%a.m "arriscado"
    '''
    def __init__(self, numero_conta, nome_titular, saldo=0, perfil_investidor="conservador"):
        super().__init__(numero_conta, nome_titular, saldo)
        self.perfil_investidor = perfil_investidor
        self.perfil_investimento()
        
    #metodos de investimento
    def perfil_investimento(self):
        if self.perfil_investidor == "conservador":
            self.taxa_juros = 0.01
        else:
            self.taxa_juros = 0.05