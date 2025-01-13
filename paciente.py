class Paciente:
    def __init__(self, codigo, nome, idade, peso, altura, sexo, plano_de_saude, rg, tipo_sanguineo, telefone, endereco, email, assunto, historico_hospitalar):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.plano_de_saude = plano_de_saude
        self.rg = rg
        self.tipo_sanguineo = tipo_sanguineo
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.assunto = assunto
        self.historico_hospitalar = historico_hospitalar

    def __str__(self):
        return (f"{self.nome}\n"
                f"Idade: {self.idade} anos\n"
                f"Peso: {self.peso} kg\n"
                f"Altura: {self.altura} m\n"
                f"Sexo: {self.sexo}\n"
                f"Plano de Saúde: {self.plano_de_saude}\n"
                f"RG: {self.rg}\n"
                f"Tipo Sanguíneo: {self.tipo_sanguineo}\n"
                f"Telefone: {self.telefone}\n"
                f"Endereço: {self.endereco}\n"
                f"E-mail: {self.email}\n"
                f"Assunto: {self.assunto}\n"
                f"Histórico Hospitalar: {self.historico_hospitalar}\n")


pacientes = []

paciente1 = Paciente(123, "João Silva", 30, 80, 1.75, "Masculino", "Unimed", "123456789", "O+", "987654321", "Rua A, 123", "joao@email.com", "Consulta", "Nenhum histórico")
paciente2 = Paciente(231, "Maria Oliveira", 25, 60, 1.65, "Feminino", "Bradesco Saúde", "987654321", "A-", "912345678", "Rua B, 456", "maria@email.com", "Exame", "Alergia a penicilina")

pacientes.append(paciente1)
pacientes.append(paciente2)

def buscar_paciente_por_codigo(codigo):
    for paciente in pacientes:
        if paciente.codigo == codigo:
            return paciente
    return None

codigo_busca = int(input("[Código do paciente] : "))
paciente_encontrado = buscar_paciente_por_codigo(codigo_busca)

if paciente_encontrado:
    print(f"Paciente encontrado: {paciente_encontrado}")
else:
    print("Paciente não encontrado.")