from src.pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente

def list_all(people, nome_objeto):
    if nome_objeto == "Especialista":
        for i, person in enumerate(people, 1):
            print(f"{i}-Nome: {person['nome']}, CRO: {person['cpf']}, Especialidade: {person['especialidade']}")
        print("")

    elif nome_objeto == "Paciente":
        for i, person in enumerate(people, 1):
            print(f"{i}-Nome: {person['nome']}, CPF: {person['cpf']}, Número do SUS: {person['nro_sus']}")
        print("")
