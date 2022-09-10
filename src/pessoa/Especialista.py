from src.pessoa.Pessoa import Pessoa
from src.pessoa.Endereco import Endereco

class Especialista(Pessoa):
    # Construtor
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: str,
                 endereco: Endereco, telefone: str, cro: int, especialidade: str,
                 data_engresso: str):

        # Construtor da classe herdada (Pessoa)
        super().__init__(nome, cpf, sexo, data_nascimento, endereco, telefone)
        self._cro = cro
        self._data_engresso = data_engresso
        self._especialidade = especialidade

    def __str__(self) -> str:
        pass
    
    # Gets
    @property
    def cro(self) -> int:
        return self._cro

    @property
    def data_engresso(self) -> str:
        return self._data_engresso

    @property
    def especialidade(self) -> str:
        return self._especialidade

    # Sets
    @cro.setter
    def cro(self, cro_setter: str):
        self._cro = cro_setter

    @data_engresso.setter
    def data_engresso(self, data_engresso_setter: str):
        self._data_engresso = data_engresso_setter

    @especialidade.setter
    def especialidade(self, especialidade_setter: str):
        self._especialidade = especialidade_setter


