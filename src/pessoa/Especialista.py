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
        saida = f"""\t\tNome: {self.nome}\t\tCPF: {self.cpf}
        Sexo: {self.sexo}\t\tData de Nascimento: {self.data_nascimento}\t\tTelefone: {self.telefone}
        {self.endereco}
        CRO: {self.cro}\t\tEspecialidade: {self.especialidade}\t\tData de Engresso: {self.data_engresso}"""
        return saida
