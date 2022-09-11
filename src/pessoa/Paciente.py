from src.pessoa.Pessoa import Pessoa
from src.pessoa.Endereco import Endereco

class Paciente(Pessoa):
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: str,
                 telefone: str, altura: float, peso: float, endereco: Endereco, 
                 nro_sus: str):

        super().__init__(nome, cpf, sexo, data_nascimento, endereco, telefone)
        self.altura = altura
        self.peso = peso
        self.nro_sus = nro_sus

    def __str__(self):
        saida = f"\n\nNome: {self.nome}\t\tCPF: {self.cpf}\t\tNúmero do SUS: {self.nro_sus}\n\
        Sexo: {self.sexo}\t\tData de Nascimento: {self.data_nascimento}\t\tTelefone: {self.telefone}\n\
        {self.endereco}\n\
        Altura: {self.altura}\t\tPeso: {self.peso}\n"
        return saida
