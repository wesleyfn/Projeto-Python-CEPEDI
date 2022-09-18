import json, os
from src.prontuario.prontuario import Prontuario

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

def salvar_pessoa(pessoa, nome_objeto) -> None:
    pessoas = carregar_json(nome_objeto)
    
    if pessoas is None:
        pessoas = []
    
    dict_pessoa = pessoa.__dict__
    pessoas.append(dict_pessoa)

    path = os.path.abspath(f"../data/{nome_objeto}.json")
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(pessoas, json_file, ensure_ascii=False, indent=3)

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


