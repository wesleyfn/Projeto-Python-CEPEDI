import datetime
from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome_init: str, cpf_init: str, sexo: str, data_nascimento: datetime, telefone: str) -> None:
        self.__nome = nome_init
        self.__cpf = cpf_init
        self.__sexo = sexo
        self.__data_nascimento = data_nascimento
        self.__telefone = telefone

@property
def nome(self) -> str:
    return self.__nome

@nome.setter
def nome(self, nome_setter: str) -> None:
    self.__nome = nome_setter

@property
def cpf(self) -> str:
    return self.__cpf

@cpf.setter
def cpf(self, cpf_setter: str) -> None:
    self.__cpf = cpf_setter

@property
def sexo(self) -> str:
    return self.__sexo

@sexo.setter
def sexo(self, sexo_setter: str) -> None:
    self.__sexo = sexo_setter

@property
def data_nascimento(self) -> datetime:
    return self.__data_nascimento

@data_nascimento.setter
def data_nascimento(self, data_nascimento_setter) -> None:
    self.__data_nascimento = data_nascimento_setter


