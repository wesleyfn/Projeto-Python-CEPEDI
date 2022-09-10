from ..pessoa import Especialista, Paciente, Responsavel

class Prontuario:
    def __init__(self, paciente: Paciente, especialista: Especialista = None, responsavel: Responsavel = None):
        self.__especialista = especialista
        self.__responsavel = responsavel
        self.__paciente = paciente
