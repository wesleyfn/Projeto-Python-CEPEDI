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
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}"
