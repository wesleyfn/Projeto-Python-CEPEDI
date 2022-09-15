from src.pessoa.Pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: str,
                 telefone: str, altura: float, peso: float, endereco: str, 
                 nro_sus: str):

        super().__init__(nome, cpf, sexo, data_nascimento, endereco, telefone)
        self.altura = altura
        self.peso = peso
        self.nro_sus = nro_sus

    def __str__(self):
        saida = f"\n     Nome: {self.nome:40}CPF: {self.cpf:21}Altura: {self.altura:.3}     Peso: {self.peso}\n"  
        saida += f"     Data de Nascimento: {self.data_nascimento:26}Telefone: {self.telefone:16}SUS: {self.nro_sus:12}Sexo: {self.sexo}\n"
        saida += f"     Endereço: {self.endereco:36}\n"
        return saida
