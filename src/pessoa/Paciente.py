import datetime
from Pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome_init: str, cpf_init: str, sexo: str, data_nascimento: datetime, telefone: str, altura: float, peso: float, nro_sus=None):
        super.__init__(nome_init, cpf_init, sexo, data_nascimento, telefone)
        self.__altura = float(altura)
        self.__peso = float(peso)
        self.__nro_sus = int(nro_sus) if not None else None
    # fim __init__

    # metodos Getter abaixo

    @property # metodo getter para imc
    def imc(self) -> float:
        return (self.__peso / (self.__altura**2))
    # fim imc

    @property # metodo getter para altura
    def altura(self) -> float:
        return self.__altura
    # fim altura

    @property # metodo getter para peso
    def peso(self) -> float:
        return self.__peso
    # fim peso

    @property # metodo getter para nro_sus
    def nro_sus(self) -> int:
        return self.__nro_sus
    # fim nro_sus

    # metodos Setter acima
    # # # # # # # # # # # # # # # # # # # # # # # # # #
    # metodos Setter abaixo

    @altura.setter # metodo setter para altura
    def altura(self, altura_setter: float) -> None:
        self.__altura = float(altura_setter)
    # fim altura

    @peso.setter # metodo setter para peso
    def peso(self, peso_setter: float) -> None:
        self.__peso = float(peso_setter)
    # fim peso

    @nro_sus.setter # metodo setter para nro_sus
    def nro_sus(self, nro_sus_setter: int) -> None:
        self.__nro_sus = int(nro_sus_setter)
    # fim nro_sus

    # metodos Setter acima

# fim class Paciente