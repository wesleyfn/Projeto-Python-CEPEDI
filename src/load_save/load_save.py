import os, json
from src.pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente
from src.prontuario.Prontuario import Prontuario

def load_json(name_json):
    path = os.path.abspath(f"../data/{name_json}.json")
    try:
        with open(path, 'r', encoding='utf-8') as json_file:
            if json_file:
                return json.load(json_file)
    except json.decoder.JSONDecodeError:
        return None
    except FileNotFoundError:
        with open(path, 'w', encoding='utf-8') as json_file:
            return None

def save_paciente(paciente: Paciente) -> None:
    pacientes = load_json("pacientes") if not None else []
    print(pacientes)
    dict_paciente = paciente.__dict__
    dict_paciente['endereco'] = paciente.endereco.__dict__
    pacientes.append(dict_paciente)

    path = os.path.abspath("../data/pacientes.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(pacientes, json_file, ensure_ascii=False, indent=True)

def save_especialista(especialista: Especialista):
    especialistas = load_json("especialistas") if not None else []
    dict_especialista = especialista.__dict__
    dict_especialista['endereco'] = especialista.endereco.__dict__
    especialistas.append(dict_especialista)

    path = os.path.abspath("../data/especialistas.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(especialistas, json_file, ensure_ascii=False, indent=True)

def save_prontuario(prontuario: Prontuario):
    prontuarios = load_json("prontuarios") if not None else []
    dict_prontuario = prontuario.__dict__
    dict_prontuario['especialista'] = prontuario.especialista.__dict__
    prontuarios.append(dict_prontuario)

    path = os.path.abspath("../data/prontuarios.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(prontuarios, json_file, ensure_ascii=False, indent=True)