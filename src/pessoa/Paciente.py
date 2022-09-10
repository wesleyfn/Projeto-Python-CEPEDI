import datetime
from Pessoa import Pessoa, Endereco

class Paciente(Pessoa):
    def __init__(self, nome_init: str, cpf_init: str, sexo: str, data_nascimento: datetime, telefone: str,
                 altura: float, peso: float, sexo_init: str, data_nascimento_init: datetime, endereco_init: Endereco,
                 telefone_init: str, nro_sus: int = None):

        super().__init__(nome_init, cpf_init, sexo_init, data_nascimento_init, endereco_init, telefone_init)
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
        self.__altura = float(altura_setter)

    @peso.setter
    def peso(self, peso_setter: float) -> None:
        self.__peso = float(peso_setter)

    @nro_sus.setter
    def nro_sus(self, nro_sus_setter: int) -> None:
        self.__nro_sus = int(nro_sus_setter)
