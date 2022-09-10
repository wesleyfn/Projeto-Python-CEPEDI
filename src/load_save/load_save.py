import os
import json
import datetime
from src.pessoa.Pessoa import Pessoa
from src.pessoa.Endereco import Endereco
from src.pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente
from src.pessoa.Responsavel import Responsavel

from src.prontuario.Prontuario import Prontuario


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


def create_dict_pessoa(pessoa) -> dict:
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


def create_dict_paciente(dict_pessoa, paciente) -> dict:
    dict_pessoa['altura'] = paciente.altura
    dict_pessoa['peso'] = paciente.peso
    dict_pessoa['nro_sus'] = paciente.nro_sus

    return dict_pessoa


def create_dict_especialista(dict_pessoa, especialista) -> dict:
    dict_pessoa['cro'] = especialista.cro
    dict_pessoa['especialidade'] = especialista.especialidade

    return dict_pessoa


def save_paciente(paciente: Paciente) -> None:
    pacientes = load_pacientes()
    new_paciente = create_dict_pessoa(paciente)
    new_paciente = create_dict_paciente(new_paciente, paciente)

    pacientes.append(new_paciente)

    path = os.path.abspath("../data/pacientes.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(pacientes, json_file, ensure_ascii=False, indent=True)


def save_especialista(especialista: Especialista):
    especialistas = load_especialistas()
    new_especialista = create_dict_pessoa(especialista)
    new_especialista = create_dict_especialista(new_especialista, especialista)

    especialistas.append(new_especialista)

    path = os.path.abspath("../data/especialistas.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(especialistas, json_file, ensure_ascii=False, indent=True)


def save_prontuario(prontuario: Prontuario):
    prontuarios = load_prontuarios()

    dict_especialista = create_dict_pessoa(prontuario.especialista)
    dict_especialista = create_dict_especialista(dict_especialista, prontuario.especialista)

    dict_paciente = create_dict_pessoa(prontuario.paciente)
    dict_paciente = create_dict_paciente(dict_especialista, prontuario.paciente)

    dict_responsavel = create_dict_pessoa(prontuario.responsavel)
    dict_responsavel["grau_parentesco"] = prontuario.responsavel.grau_parentesco

    new_prontuario = {"paciente": dict_paciente,
                      "responsavel": dict_responsavel,
                      "data": prontuario.data,
                      "consulta": prontuario.consulta,
                      "patologia": prontuario.patologia,
                      "procedimento": prontuario.procedimento,
                      "especialista": dict_especialista
                      }

    prontuarios.append(new_prontuario)

    path = os.path.abspath("../data/prontuarios.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(prontuarios, json_file, ensure_ascii=False, indent=True)
