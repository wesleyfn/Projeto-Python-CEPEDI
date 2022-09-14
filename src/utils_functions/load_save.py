import json, os
from src.pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente
from src.prontuario.Prontuario import Prontuario

def load_json(name_json):
    path = os.path.abspath(f"../data/{name_json}.json")
    try:
        with open(path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except json.decoder.JSONDecodeError:
        return None
    except FileNotFoundError:
        with open(path, 'w', encoding='utf-8') as json_file:
            return None

def save_paciente(paciente: Paciente) -> None:
    pacientes = load_json("pacientes")
    
    if pacientes is None:
        pacientes = []
    
    dict_paciente = paciente.__dict__
    dict_paciente['endereco'] = paciente.endereco.__dict__
    pacientes.append(dict_paciente)

    path = os.path.abspath("../data/pacientes.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(pacientes, json_file, ensure_ascii=False, indent=3)

def save_especialista(especialista: Especialista):
    especialistas = load_json("especialistas")
    
    if especialistas is None:
        especialistas = []
        
    dict_especialista = especialista.__dict__
    dict_especialista['endereco'] = especialista.endereco.__dict__
    especialistas.append(dict_especialista)

    path = os.path.abspath("../data/especialistas.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(especialistas, json_file, ensure_ascii=False, indent=3)

def save_prontuario(prontuario: Prontuario):
    prontuarios = load_json("prontuarios")
        
    if prontuarios is None:
        prontuarios = []
    
    dict_prontuario = prontuario.__dict__
    prontuarios.append(dict_prontuario)
    
    path = os.path.abspath("../data/prontuarios.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(prontuarios, json_file, ensure_ascii=False, indent=3)
        
"""     paciente_temp = prontuario.paciente.__dict__
    paciente_temp['endereco'] = prontuario.paciente.endereco.__dict__
    dict_prontuario['paciente'] = paciente_temp

    if isinstance(prontuario.responsavel, Responsavel):
        responsavel_temp = prontuario.responsavel.__dict__
        responsavel_temp['endereco'] = prontuario.responsavel.endereco.__dict__
        dict_prontuario['responsavel'] = paciente_temp

    especialista_temp = prontuario.especialista.__dict__
    especialista_temp['endereco'] = prontuario.especialista.endereco.__dict__
    dict_prontuario['especialista'] = especialista_temp

    prontuarios.append(dict_prontuario) """


