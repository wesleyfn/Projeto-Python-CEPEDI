import datetime

from ..pessoa.Especialista import Especialista
from ..pessoa.Paciente import Paciente
from ..pessoa.Responsavel import Responsavel

class Prontuario:
    def __init__(self):
        self.__especialista = None
        self.__responsavel = None
        self.__paciente = None
        self.__patologia = None
        self.__procedimento = None
        self.__data = None
        self.__consulta = None

    @property
    def especialista(self) -> Especialista:
        return self.__especialista

    @property
    def responsavel(self) -> Responsavel:
        return self.__responsavel

    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @property
    def patologia(self) -> list:
        return self.__patologia

    @property
    def procedimento(self) -> list[dict]:
        return self.__procedimento

    @property
    def data(self) -> datetime:
        return self.__data

    @property
    def consulta(self) -> str:
        return self.__consulta

    @especialista.setter
    def especialista(self, especialista_setter) -> None:
        self.__especialista = especialista_setter

    @responsavel.setter
    def responsavel(self, responsavel_setter) -> None:
        self.__responsavel = responsavel_setter

    @paciente.setter
    def paciente(self, paciente_setter) -> None:
        self.__paciente = paciente_setter

    @patologia.setter
    def patologia(self, patologia_setter) -> None:
        self.__patologia = patologia_setter

    @procedimento.setter
    def procedimento(self, procedimento_setter) -> None:
        self.__procedimento = procedimento_setter

    @data.setter
    def data(self, data_setter) -> None:
        self.__data = data_setter

    @consulta.setter
    def consulta(self, consulta_setter) -> None:
        self.__consulta = consulta_setter

    def inicialize_prontuario(self):
        pass
