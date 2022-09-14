from src.pessoa.Pessoa import Pessoa
from src.pessoa.Endereco import Endereco

class Responsavel(Pessoa):
    # Construtor
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: str, 
                 telefone: str, endereco: Endereco, grau_parentesco: str):

        # Construtor da classe herdada (Pessoa)
        super().__init__(nome, cpf, sexo, data_nascimento, endereco, telefone)
        self.grau_parentesco = grau_parentesco

    def __str__(self):
        pass
