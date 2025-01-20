class Clinica:
    def _init_(self, nome_c="Fisiomais", endereco="Rua Paulo Cruz, 18", telefone="+55 (87)9971-8821", horario='Segunda a Sexta | 06:00 - 18:00'):
        self.nome_c = nome_c
        self.endereco = endereco
        self.telefone = telefone
        self.horario = horario
    def info_g(self):
                print(f'''
    ====================== Informações sobre a Fisiomais ======================
     Nome da Clínica - {self.nome_c}                                         
     Endereço - {self.endereco}                                              
     Telefone - {self.telefone}                                              
     Horário de Funcionamento - {self.horario}                               
    ===========================================================================
''')