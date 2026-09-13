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
        self.taxa_juros = 0.01 if perfil_investidor == "conservador" else 0.05
        
    #metodos de investimento
    

    @property
    def perfil_investimento(self):
        return self.perfil_investidor

    @perfil_investimento.setter
    def perfil_investimento(self, perfil_investidor):
        if perfil_investidor not in ["conservador", "arriscado"]:
            print("Perfil de investidor inválido. Escolha entre 'conservador' ou 'arriscado'.")
        else:
            self.perfil_investidor = perfil_investidor
            if perfil_investidor == "conservador":
                self.taxa_juros = 0.01  # 1% ao mês
            else:
                self.taxa_juros = 0.05  # 5% ao mês