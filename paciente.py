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
            f"Idade: {self.data_de_nascimento} anos\n"
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
