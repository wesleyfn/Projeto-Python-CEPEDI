import datetime
from Pessoa import Pessoa
from Endereco import Endereco

class Paciente(Pessoa):
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: datetime, 
                 telefone: str, altura: float, peso: float, endereco: Endereco, 
                 nro_sus: int = None):

        super().__init__(nome, cpf, sexo, data_nascimento, endereco, telefone)
        self.__altura = altura
        self.__peso = peso
        self.__nro_sus = nro_sus

    @property
    def imc(self) -> float:
        return self.__peso / (self.__altura ** 2)

    @property
    def altura(self) -> float:
        return self.__altura

    @property
    def peso(self) -> float:
        return self.__peso

    @property
    def nro_sus(self) -> int:
        return self.__nro_sus

    @altura.setter
    def altura(self, altura_setter: float) -> None:
        self.__altura = altura_setter

    @peso.setter
    def peso(self, peso_setter: float) -> None:
        self.__peso = peso_setter

    @nro_sus.setter
    def nro_sus(self, nro_sus_setter: int) -> None:
        self.__nro_sus = nro_sus_setter
