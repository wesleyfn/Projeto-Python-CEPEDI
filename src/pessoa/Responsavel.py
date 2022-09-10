import datetime
from Pessoa import Pessoa, Endereco

class Responsavel(Pessoa):
    def __init__(self, nome_init: str, cpf_init: str, sexo: str, data_nascimento: datetime, telefone: str, altura: float, peso: float, sexo_init: str, data_nascimento_init: datetime, endereco_init: Endereco, telefone_init: str, grau_parentesco: str):
        super().__init__(nome_init, cpf_init, sexo_init, data_nascimento_init, endereco_init, telefone_init)
        self.__grau_parentesco = grau_parentesco
    # fim __init__

    # metodos Getter abaixo

    @property # metodo getter para grau_parentesco
    def grau_parentesco(self) -> str:
        return self.__grau_parentesco
    # fim grau_parentesco

    # metodos Setter acima
    # # # # # # # # # # # # # # # # # # # # # # # # # #
    # metodos Setter abaixo

    @grau_parentesco.setter  # metodo setter para grau_parentesco
    def grau_parentesco(self, grau_parentesto: str) -> None:
        self.__grau_parentesco = grau_parentesto
    # fim grau_parentesco

    # metodos Setter acima

# fim class Responsavel
