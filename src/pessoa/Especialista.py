from src.pessoa.Pessoa import Pessoa
from src.pessoa.Endereco import Endereco

class Especialista(Pessoa):
    # Construtor
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: str,
                 endereco: Endereco, telefone: str, cro: str, especialidade: str,
                 data_engresso: str):

        # Construtor da classe herdada (Pessoa)
        super().__init__(nome, cpf, sexo, data_nascimento, endereco, telefone)
        self.cro = cro
        self.data_engresso = data_engresso
        self.especialidade = especialidade

    def __str__(self) -> str:
        return f"Nome: {self.nome}, CRO: {self.cro}, Especialidade: {self.especialidade}"
    
    # Gets
   