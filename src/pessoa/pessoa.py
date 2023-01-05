from abc import ABC, abstractmethod

class Pessoa(ABC):
    # Construtor
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: str,
                 endereco: str, telefone: str):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone

    @abstractmethod
    def __str__(self):
        pass
