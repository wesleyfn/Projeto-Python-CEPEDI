import datetime
from src.pessoa.Pessoa import Pessoa
from src.pessoa.Endereco import Endereco

class Paciente(Pessoa):
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: str,
                 telefone: str, altura: float, peso: float, endereco: Endereco, 
                 nro_sus: int = None):

        super().__init__(nome, cpf, sexo, data_nascimento, endereco, telefone)
        self._altura = altura
        self._peso = peso
        self._nro_sus = nro_sus

    @property
    def imc(self) -> float:
        return self._peso / (self.__altura ** 2)

    @property
    def altura(self) -> float:
        return self._altura

    @property
    def peso(self) -> float:
        return self._peso
    
    @property
    def nro_sus(self) -> int:
        return self._nro_sus

    @altura.setter
    def altura(self, altura_setter: float) -> None:
        self._altura = altura_setter

    @peso.setter
    def peso(self, peso_setter: float) -> None:
        self._peso = peso_setter

    @nro_sus.setter
    def nro_sus(self, nro_sus_setter: int) -> None:
        self._nro_sus = nro_sus_setter

    def __str__(self):
        pass
