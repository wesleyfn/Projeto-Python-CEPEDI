from abc import ABC, abstractmethod
from src.pessoa.Endereco import Endereco

class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: str,
                 endereco: Endereco, telefone: str):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone

    @abstractmethod
    def __str__(self):
        pass
