import json, os
from src.pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente
from src.prontuario.Prontuario import Prontuario

def carregar_json(name_json):
    path = os.path.abspath(f"../data/{name_json}.json")
    try:
        with open(path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    except json.decoder.JSONDecodeError:
        return None
    except FileNotFoundError:
        with open(path, 'w', encoding='utf-8') as json_file:
            return None

def salvar_paciente(paciente: Paciente) -> None:
    pacientes = carregar_json("pacientes")
    
    if pacientes is None:
        pacientes = []
    
    dict_paciente = paciente.__dict__
    pacientes.append(dict_paciente)

    path = os.path.abspath("../data/pacientes.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(pacientes, json_file, ensure_ascii=False, indent=3)

def salvar_especialista(especialista: Especialista):
    especialistas = carregar_json("especialistas")
    
    if especialistas is None:
        especialistas = []
        
    dict_especialista = especialista.__dict__
    especialistas.append(dict_especialista)

    path = os.path.abspath("../data/especialistas.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(especialistas, json_file, ensure_ascii=False, indent=3)

def salvar_prontuario(prontuario: Prontuario):
    prontuarios = carregar_json("prontuarios")
        
    if prontuarios is None:
        prontuarios = []
    
    dict_prontuario = prontuario.__dict__
    prontuarios.append(dict_prontuario)
    
    path = os.path.abspath("../data/prontuarios.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(prontuarios, json_file, ensure_ascii=False, indent=3)

def atualizar_registro(nome_objeto, lista_atualizada):
    path = os.path.abspath(f"../data/{nome_objeto}.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(lista_atualizada, json_file, ensure_ascii=False, indent=3)


