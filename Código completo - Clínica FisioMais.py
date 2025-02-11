class Clinica:
    def __init__(self, nome_c="Fisiomais", endereco="Rua Paulo Cruz, 18", telefone="+55 (87)9971-8821", horario='Segunda a Sexta | 06:00 - 18:00'):
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



#########################



class Medico:
    def __init__(self, nome, idade, telefone, email, especialidade, registro, data_rgs):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.especialidade = especialidade
        self.registro = registro
        self.data_rgs = data_rgs

    def info_dispn(self):
        return f"Médico: {self.nome}\nEspecialidade: {self.especialidade}\nTelefone: {self.telefone}\nEmail: {self.email}\nRegistro: {self.registro}\nData de Registro: {self.data_rgs}"

class MedicoRepository:
    def __init__(self):
        self.medicos = []

    def adicionar_medico(self, medico):
        self.medicos.append(medico)

    def listar_medicos(self):
        for medico in self.medicos:
            print(medico.info_dispn())
            print("--------------------")

ramon = Medico("Ramon", 35, "11 99999-8888", "ramon@email.com", "Fisioterapeuta", "CRM 12345", "2020-01-01")
Dudu = Medico("Dudu", 40, "11 88888-7777", "Dudu@email.com", "Fisioterapeuta", "CRM 67890", "2018-06-01")

repositorio = MedicoRepository()

repositorio.adicionar_medico(ramon)
repositorio.adicionar_medico(Dudu)

repositorio.listar_medicos()



#########################



class Paciente:
    def __init__(self, cpf, nome, data_de_nascimento, peso, altura, sexo, plano_de_saude, rg, tipo_sanguineo, telefone, endereco, email, historico_hospitalar):
        self.cpf = cpf
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.plano_de_saude = plano_de_saude
        self.rg = rg
        self.tipo_sanguineo = tipo_sanguineo
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.historico_hospitalar = historico_hospitalar
    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Data de nascimento: {self.data_de_nascimento}\n"
            f"Peso: {self.peso} kg\n"
            f"Altura: {self.altura} m\n"
            f"Sexo: {self.sexo}\n"
            f"Plano de Saúde: {self.plano_de_saude}\n"
            f"RG: {self.rg}\n"
            f"Tipo Sanguíneo: {self.tipo_sanguineo}\n"
            f"Telefone: {self.telefone}\n"
            f"Endereço: {self.endereco}\n"
            f"E-mail: {self.email}\n"
            f"Histórico Hospitalar: {self.historico_hospitalar}"
        )




pacientes = []


paciente1 = Paciente(32165987465, "Roberto Siqueira", "13/09/1992", 65.32, 1.73, "Masculino",
"Unimed", "123456789", "O+", "987654321", "Rua A, 123",
"siqueirinha@email.com", "Nenhum histórico")
paciente2 = Paciente(98745879632, "Antonella Rossi", "26/07/1997", 62, 1.65, "Feminino",
"Bradesco Saúde", "987654321", "A-", "912345678", "Rua B, 456",
"antonita@email.com", "Alergia a penicilina")
paciente3 = Paciente(65987432145, "Maria das Graças Oliveira", "22/03/1956", 57, 1.58,
"Feminino", "Amil", "123321456", "O+", "912348765", "Rua C, 631",
"gracias@email.com", "Alergia a paracetamol")


pacientes.append(paciente1)
pacientes.append(paciente2)
pacientes.append(paciente3)




def buscar_paciente_por_codigo(cpf):
    for paciente in pacientes:
        if paciente.cpf == cpf:
            return paciente
    return None


print("== Sistema de busca de pacientes ==")


while True:  
    codigo_busca = int(input("[Código do paciente] : "))
    paciente_encontrado = buscar_paciente_por_codigo(codigo_busca)


    if paciente_encontrado:
        print(f"{paciente_encontrado}")
    else:
        print("Paciente não encontrado.")
   
    print("")
    print("Deseja inserir outro código? 1 - Sim | 2 - Não")
    tentar_novamente = int(input("[Opção]: "))
   
    if tentar_novamente != 1:
        break  



#########################
    


import random
from datetime import datetime

class Agendamento:
    def __init__(self, horarios_disponiveis, fisioterapeutas_disponiveis):
        self.horarios_disponiveis = horarios_disponiveis
        self.fisioterapeutas_disponiveis = fisioterapeutas_disponiveis
        self.historico_consultas = []

    def gerar_codigo_acesso(self):
        while True:
            codigo = f"ACSS-{random.randint(1000, 9999)}"
            if not any(c['codigo_acesso'] == codigo for c in self.historico_consultas):
                return codigo

    def validar_horario(self, hora):
        try:
            datetime.strptime(hora, "%H:%M")
            return True
        except ValueError:
            return False

    def marcar_consulta(self, data, hora, paciente, medico, tipo_servico):
        if not self.validar_horario(hora):
            return f"Horário {hora} está em formato inválido."
        if hora not in self.horarios_disponiveis:
            return f"Horário {hora} não está disponível."
        if medico not in self.fisioterapeutas_disponiveis:
            return f"Médico {medico} não está disponível."
        
        codigo_acesso = self.gerar_codigo_acesso()
        consulta = {
            "codigo_acesso": codigo_acesso,
            "data": data,
            "hora": hora,
            "paciente": paciente,
            "medico": medico,
            "tipo_servico": tipo_servico
        }
        self.historico_consultas.append(consulta)
        self.horarios_disponiveis.remove(hora)
        return f"Consulta marcada com sucesso! Código de acesso: {codigo_acesso}"

    def notificar_consulta(self, codigo_acesso):
        consulta = next((c for c in self.historico_consultas if c["codigo_acesso"] == codigo_acesso), None)
        if consulta:
            return (f"Notificação: Consulta marcada para {consulta['data']} às {consulta['hora']} com o médico "
                    f"{consulta['medico']} para o paciente {consulta['paciente']}.")
        return "Código de acesso inválido."

# Inicializar sistema
horarios_disponiveis = ["09:00", "10:00", "11:00", "14:00"]
fisioterapeutas_disponiveis = ["Dr. João", "Dra. Maria"]

agenda = Agendamento(horarios_disponiveis, fisioterapeutas_disponiveis)

# Funções auxiliares
def solicitar_dados():
    data = input("Informe a data da consulta (DD-MM-AAAA): ")
    hora = input(f"Informe a hora da consulta (horários disponíveis: {horarios_disponiveis}): ")
    paciente = input("Informe o nome do paciente: ")
    medico = input(f"Informe o nome do médico (disponíveis: {fisioterapeutas_disponiveis}): ")
    tipo_servico = input("Informe o tipo de serviço (exemplo: Fisioterapia): ")
    return data, hora, paciente, medico, tipo_servico

def main():
    data, hora, paciente, medico, tipo_servico = solicitar_dados()
    resultado = agenda.marcar_consulta(data, hora, paciente, medico, tipo_servico)
    print(resultado)

    if "Código de acesso" in resultado:
        codigo = resultado.split(": ")[1].strip()
        notificacao = agenda.notificar_consulta(codigo)
        print(notificacao)
    else:
        print("Erro ao marcar a consulta.")

if __name__ == "__main__":
    main()



#########################
    


class Pagamento:
    def __init__(self, paciente, valor_pagar=90):
        self.paciente = paciente  
        self.valor_pagar = valor_pagar
        self.forma_pagamento = ""

    def escolher_pagamento(self):
        while True:
            try:
                escolha = int(input("Escolha sua forma de pagamento: 1- Dinheiro, 2- Crédito, 3- Débito, 4- Pix: "))
                if escolha == 1:
                    self.forma_pagamento = "Dinheiro"
                    break
                elif escolha == 2:
                    self.forma_pagamento = "Crédito"
                    break
                elif escolha == 3:
                    self.forma_pagamento = "Débito"
                    break
                elif escolha == 4:
                    self.forma_pagamento = "Pix"
                    break
                else:
                    print("Escolha inválida! Tente novamente.")
            except ValueError:
                print("Entrada inválida! Digite um número entre 1 e 4.")

    def gerar_fatura(self):
        fatura = f"Fatura detalhada: Valor total a pagar: R$ {self.valor_pagar:.2f}, Forma de pagamento: {self.forma_pagamento}"
        print(fatura)

    def gerar_recibo(self):
        recibo = (f"Aqui está o seu recibo: \n"
                  f"Recebemos de: {self.paciente['nome']} (Código: {self.paciente['codigo']})\n"
                  f"Importância de: R$ {self.valor_pagar:.2f}, Referente à consulta médica.\n"
                  f"Forma de pagamento: {self.forma_pagamento}\n"
                  f"RG (CPF): {self.paciente['rg']}\n")
        print(recibo)



paciente_encontrado = {
    "nome": "João Silva",
    "codigo": "123",
    "rg": "123.456.789-00"
}

if paciente_encontrado:
    pagamento = Pagamento(paciente_encontrado, 90)  
    pagamento.escolher_pagamento()  
    pagamento.gerar_fatura()      
    pagamento.gerar_recibo()
