import datetime
from abc import ABC, abstractmethod
from Endereco import Endereco

class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: datetime,
                 endereco: Endereco, telefone: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__sexo = sexo
        self.__data_nascimento = data_nascimento
        self.__endereco = endereco
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
def data_nascimento(self, data_nascimento_setter: datetime) -> None:
    self.__data_nascimento = data_nascimento_setter

@property
def endereco(self) -> Endereco:
    return self.__endereco

@endereco.setter
def endereco(self, endereco_setter: Endereco) -> None:
    self.__endereco = endereco_setter

@property
def telefone(self) -> str:
    return self.__telefone

@telefone.setter
def telefone(self, telefone_setter: str) -> None:
    self.__telefone = telefone_setter

@abstractmethod
def __str__(self):
    pass
