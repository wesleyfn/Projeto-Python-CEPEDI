from src.utils_functions import load_save
from src.pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente
from src.pessoa.Endereco import Endereco
from src.pessoa.Responsavel import Responsavel

def list_all(people, nome_objeto):
    if nome_objeto == "Especialista":
        for i, person in enumerate(people, 1):
            print(f"{i}-Nome: {person['nome']}, CRO: {person['cpf']}, Especialidade: {person['especialidade']}")
        print("")

    elif nome_objeto == "Paciente":
        for i, person in enumerate(people, 1):
            print(f"{i}-Nome: {person['nome']}, CPF: {person['cpf']}, Número do SUS: {person['nro_sus']}")
        print("")

    elif nome_objeto == "Prontuario":
        for i, person in enumerate(people, 1):
            paciente = person['paciente']
            especialista = person['especialista']

            print(f"{i}-Paciente: {paciente['nome']}, Número do SUS: {paciente['paciente']['nro_sus']}\n"
                  f", Especialista: {especialista['nome']}, CRO: {especialista['cro']}\n"
                  f"Data do prontuário: {person['data']}")

def dict_to_obj(person, nome_objeto):
    person['endereco'] = Endereco(person['endereco']['endereco'],
                                  person['endereco']['bairro'],
                                  person['endereco']['area'])

    if nome_objeto == "Especialista":
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
    elif nome_objeto == "Paciente":
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

def opcao(tipo: str, string: str):
    x = None

    while True:
        try:
            match tipo:
                case 'i':
                    x = int(input(string))
                case 'f':
                    x = float(input(string))
                case 's':
                    x = input(string)
                    if x.isspace() or x == '':
                        x = None

        except ValueError:
            match tipo:
                case 'i':
                    print('\n > Digite um número inteiro!\n')
                case 'f':
                    print('\n > Digite um número flutuante!\n')
        else:
            return x

def filtros(onde_buscar: int) -> dict:
    nome = opcao('s', f" > Digite o nome do paciente: ")
    cpf = opcao('s', f" > Digite o CPF do paciente: ")

    if onde_buscar != 'Prontuario':
        filtro_busca = {"nome": nome, "cpf": cpf}
    else:
        filtro_busca = {'paciente': {"nome": nome, "cpf": cpf}}

    match onde_buscar:
        case 'Especialista':  # case especilista
            cro = opcao('s', f" > Digite o CRO do especialista: ")
            filtro_busca["cro"] = cro

        case 'Paciente':  # case paciente
            nro_sus = opcao('s', f" > Digite o número do SUS do paciente: ")
            filtro_busca["nro_sus"] = nro_sus

        case 'Prontuario':  # case prontuário
            filtro_busca['data'] = opcao("s", f"> Digite a data do prontuário: ")
    print("")
    return filtro_busca

def find_people(nome_json, filtro_busca):
    peoples = load_save.load_json(nome_json)
    matchs = []

    if not peoples:
        return []

    for person in peoples:
        find = True

        for key, value in filtro_busca.items():
            if value is None or person[key] is None:
                continue

            elif key != 'paciente' and person[key].isnumeric() and value.isnumeric():
                if person[key] != value:
                    find = False

            elif key == 'paciente':
                paciente = person['paciente']
                if paciente['nome'] != value['nome'] or paciente['cpf'] != value['cpf']:
                    find = False

            elif person[key].lower() != value.lower():
                find = False

        if find:
            matchs.append(person)

    return matchs
