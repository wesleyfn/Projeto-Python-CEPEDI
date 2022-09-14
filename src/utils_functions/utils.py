from src.pessoa.Pessoa import Pessoa
from src.utils_functions import load_save
from src.pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente
from src.pessoa.Endereco import Endereco
from src.pessoa.Responsavel import Responsavel

def dict_to_obj(person, nome_objeto):

    if nome_objeto == "prontuario":
        aux_endereco = person['paciente']
        aux_endereco['endereco'] = Endereco(aux_endereco['endereco']['endereco'],
                                            aux_endereco['endereco']['bairro'],
                                            aux_endereco['endereco']['area'])

    else:
        person['endereco'] = Endereco(person['endereco']['endereco'],
                                      person['endereco']['bairro'])

    if nome_objeto == "especialista":
        person = Especialista(person['nome'],
                              person['cpf'],
                              person['sexo'],
                              person['data_nascimento'],
                              person['endereco'],
                              person['telefone'],
                              person['cro'],
                              person['especialidade'],
                              person['data_engresso'])
        return person
    elif nome_objeto == "paciente":
        person = Paciente(person['nome'],
                          person['cpf'],
                          person['sexo'],
                          person['data_nascimento'],
                          person['telefone'],
                          person['altura'],
                          person['peso'],
                          person['endereco'],
                          person['nro_sus'])
        return person

def opcao(tipo: str, string: str, n_opcoes: int=0):
    x = 0
    while True:
        try:
            match tipo:
                case 'i':
                    x = int(input(string))
                    if n_opcoes != 0:
                        while x > n_opcoes or x < 0:
                            x = int(input(string))
                case 'f':
                    x = float(input(string))
                case 's':
                    x = input(string)
                    while x.isspace() or x == '':
                        x = input(string)
        except ValueError:
            match tipo:
                case 'i':
                    print('\n > Digite um número inteiro!\n')
                case 'f':
                    print('\n > Digite um número flutuante!\n')
        else:
            return x

def gerar_filtro(onde_buscar: str) -> dict:
    filtro = {}
    match onde_buscar:
        case 'especialistas':  # Se a entrada for de números o filtro será o CPF
            nome_cpf = opcao('s', " > Digite o nome ou CPF do especialista: ")
            filtro = {"cpf": nome_cpf} if nome_cpf.isnumeric() else {"nome": nome_cpf}

        case 'pacientes' | 'prontuarios':  # Se a entrada for de números o filtro será o CPF
            nome_cpf = opcao('s', " > Digite o nome ou CPF do paciente: ")
            filtro = {"cpf": nome_cpf} if nome_cpf.isnumeric() else {"nome": nome_cpf}

        case outro:
            print(" > Não há onde buscar!\n")
            
    return filtro

def buscar_pessoas(tipo_pessoa) -> list:
    filtro = gerar_filtro(tipo_pessoa)
    pessoas = load_save.load_json(tipo_pessoa)
    encontros = []
    
    if not pessoas: # retorna []
        return encontros
    
    for pessoa in pessoas:
        encontrou = True
        for key, valor in filtro.items():
            if valor is None or pessoa[key] is None:
                continue

            elif key != 'paciente' and pessoa[key].isnumeric() and valor.isnumeric():
                if pessoa[key] != valor:
                    encontrou = False

            elif key == 'paciente':
                paciente = pessoa['paciente']
                if paciente['nome'] != valor['nome'] and paciente['cpf'] != valor['cpf']:
                    encontrou = False

            elif pessoa[key].lower() != valor.lower():
                encontrou = False
        if encontrou:
            encontros.append(pessoa)

    return encontros

def listar_encontrados(lista: Pessoa, tipo: str):
    match tipo:
        case "especialista":
            for i, pessoa in enumerate(lista, 1):
                print(f"   {i}. Nome: {pessoa['nome']}, CRO: {pessoa['cpf']}"
                      f"\n      Especialidade: {pessoa['especialidade']}\n")

        case "paciente":
            for i, pessoa in enumerate(lista, 1):
                print(f"   {i}. Nome: {pessoa['nome']}, CPF: {pessoa['cpf']}"
                      f"\n      Data de Nascimento: {pessoa['data_nascimento']}\n")

        case "prontuario":
            for i, pessoa in enumerate(lista, 1):
                paciente = pessoa['paciente']
                especialista = pessoa['especialista']

                print(f" {i}. Paciente: {paciente['nome']}, Número do SUS: {paciente['nro_sus']}\n"
                    f", Especialista: {especialista['nome']}, CRO: {especialista['cro']}\n"
                    f"Data do prontuário: {pessoa['data']}")