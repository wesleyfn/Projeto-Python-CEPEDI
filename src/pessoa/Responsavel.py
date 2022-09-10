from copyreg import constructor
import datetime
from Pessoa import Pessoa
from Endereco import Endereco

class Responsavel(Pessoa):
    # Construtor
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: datetime, 
                 telefone: str, altura: float, peso: float, endereco: Endereco, grau_parentesco: str):

        # Construtor da classe herdade
        super().__init__(nome, cpf, sexo, data_nascimento, endereco, telefone)
        self.__grau_parentesco = grau_parentesco

    # Get
    @property
    def grau_parentesco(self) -> str:
        return self.__grau_parentesco

    # Set
    @grau_parentesco.setter 
    def grau_parentesco(self, grau_parentesto: str) -> None:
        self.__grau_parentesco = grau_parentesto
