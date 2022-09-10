from ..pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente
from ..pessoa.Responsavel import Responsavel

class Prontuario:
    def __init__(self):
        self.especialista = None
        self.responsavel = None
        self.paciente = None
        self.patologia = None
        self.procedimento = None
        self.data = None
        self.consulta = None

    def inicialize_prontuario(self):
        pass
