from abc import ABC, abstractmethod
from src.pessoa.Endereco import Endereco

class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: str,
                 endereco: Endereco, telefone: str):
        self._nome = nome
        self._cpf = cpf
        self._sexo = sexo
        self._data_nascimento = data_nascimento
        self._endereco = endereco
        self._telefone = telefone

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome_setter: str) -> None:
        self._nome = nome_setter

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, cpf_setter: str) -> None:
        self._cpf = cpf_setter

    @property
    def sexo(self) -> str:
        return self._sexo

    @sexo.setter
    def sexo(self, sexo_setter: str) -> None:
        self._sexo = sexo_setter

    @property
    def data_nascimento(self) -> str:
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento_setter: str) -> None:
        self._data_nascimento = data_nascimento_setter

    @property
    def endereco(self) -> Endereco:
        return self._endereco

    @endereco.setter
    def endereco(self, endereco_setter: Endereco) -> None:
        self._endereco = endereco_setter

    @property
    def telefone(self) -> str:
        return self._telefone

    @telefone.setter
    def telefone(self, telefone_setter: str) -> None:
        self._telefone = telefone_setter

    @abstractmethod
    def __str__(self):
        pass
