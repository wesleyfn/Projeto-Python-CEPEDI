import json
import datetime
from src.pessoa.Pessoa import Pessoa
from src.pessoa.Endereco import Endereco
from src.pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente
from src.pessoa.Responsavel import Responsavel
import os


def load_pacientes():
    path = os.path.abspath("../data/pacientes.json")
    with open(path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def load_especialistas():
    path = os.path.abspath("../data/especialistas.json")
    with open(path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def load_prontuarios():
    path = os.path.abspath("../data/prontuarios.json")
    with open(path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def save_pessoa(pessoa) -> dict:
    new_pessoa = {"nome": pessoa.nome,
                  "cpf": pessoa.cpf,
                  "sexo": pessoa.sexo,
                  "data_nascimento": pessoa.data_nascimento,
                  "telefone": pessoa.telefone,
                  "endereco": {"endereco": pessoa.endereco.endereco,
                               "bairro": pessoa.endereco.bairro,
                               "area": pessoa.endereco.area}
                  }
    return new_pessoa

def save_paciente(paciente: Paciente) -> None:
    pacientes = load_pacientes()
    new_paciente = save_pessoa(paciente)
    new_paciente['altura'] = paciente.altura
    new_paciente['peso'] = paciente.peso
    new_paciente['nro_sus'] = paciente.nro_sus

    pacientes.append(new_paciente)

    path = os.path.abspath("../data/pacientes.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(pacientes, json_file, ensure_ascii=False, indent=True)

def save_especialista(especialista: Especialista):
    especialistas = load_especialistas()
    new_especialista = save_pessoa(especialista)
    new_especialista['cro'] = especialista.cro
    new_especialista['especialidade'] = especialista.especialidade

    especialistas.append(new_especialista)

    path = os.path.abspath("../data/especialistas.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(especialistas, json_file, ensure_ascii=False, indent=True)


def save_prontuario():
    pass
