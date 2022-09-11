import json
from src.pessoa.Paciente import Paciente
from src.pessoa.Especialista import Especialista
from src.pessoa.Endereco import Endereco
from src.load_save import load_save

def opcao(tipo: str, string: str):
    x = 0
    while True:
        try:
            match tipo:
                case 'i':
                    x = int(input(string))
                case 'f':
                    x = float(input(string))
                case 's':
                    x = input(string)
        except:
            match tipo:
                case 'i':
                    print('\n > Digite um número inteiro!\n')
                case 'f':
                    print('\n > Digite um número flutuante!\n')
        else:
            return x

def filtros(index_of_category: int) -> dict:
    nome = input("Digite o nome: ")
    nome = nome.lower() if nome else None

    cpf = input("Digite o cpf: ")
    cpf = cpf if cpf else None

    filtro_busca = {"nome": nome, "cpf": cpf}

    match index_of_category:
        case 1: # case especilista
            cro = input("Digite o cro: ")
            cro = cro if cro else None
            filtro_busca["cro"] = cro

        case 2: # case paciente
            nro_sus = input("Digite o número do SUS: ")
            nro_sus = nro_sus if nro_sus else None
            filtro_busca["nro_sus"] = nro_sus

        case 3: # case prontuário
            pass

    print("")
    return filtro_busca

def cadastro_pessoa():
    nome = opcao('s', " > Digite o nome: ")
    cpf = opcao('s', " > Digite o CPF: ")
    sexo = opcao('s', " > Digite o sexo [M/F]: ")
    data_nascimento = opcao('s', " > Digite a data de nascimento [dd/mm/aa]: ")
    endereco = opcao('s', " > Digite o endereço: ")
    bairro = opcao('s', " > Digite o bairro: ")
    area = opcao('s', " > Digite a área [Comercial, Residencial, Rural...]: ")
    endereco = Endereco(endereco, bairro, area)
    telefone = opcao('s', " > Digite o telefone: ")

    return nome, cpf, sexo, data_nascimento, endereco, telefone

def menu_cadastro():
    loop_condition = True

    while loop_condition:
        print(" 1. Cadastrar Especialista\n 2. Cadastrar Paciente\n 3. Cadastrar Prontuáio\n 0. Voltar")
        op = opcao('i', " > Opção:")
        print("")

        match op:
            case 1:
                nome, cpf, sexo, data_nascimento, endereco, telefone = cadastro_pessoa()
                cro = opcao('i', " > Digite o CRO: ")
                data_engresso = opcao('s', " > Digite a data de engresso dd/mm/aa: ")
                especialidade = opcao('s', " > Digite a especialidade: ")
                print("")
                especialista = Especialista(nome, cpf, sexo, data_nascimento, endereco, telefone, cro, especialidade,
                                            data_engresso)

                load_save.save_especialista(especialista)
            case 2:
                nome, cpf, sexo, data_nascimento, endereco, telefone = cadastro_pessoa()
                altura = opcao('f', " > Digite a altura: ")
                peso = opcao('f', " > Digite o peso: ")
                nro_sus = opcao('i', " > Digite o número do SUS: ")
                print("\n")
                paciente = Paciente(nome, cpf, sexo, data_nascimento, telefone, altura, peso, endereco, nro_sus)

                load_save.save_paciente(paciente)
            case 3:

                pass
            case 0:
                return

def find_people(nome_arquivo_json, filtro_busca):
    people = load_save.load_json(nome_arquivo_json)
    matchs = []

    if not people:
        return []

    for person in people:
        find = 1
        for key, value in filtro_busca.items():
            if value is None:
                continue

            if not value.isnumeric() and person[key].lower() != value.lower():
                find = 0
                break

        if find:
            matchs.append(person)

    return matchs

def main_menu():
    loop_condition = True
    while loop_condition:
        print(" 1. Cadastros\n"
              " 2. Buscar Especialista\n"
              " 3. Buscar Paciente\n"
              " 4. Buscar Prontuário\n"
              " 5. Importar/Exportar Prontuário\n"
              " 0. Sair")
        op = opcao('i', " > Digite a opção: ")
        print("")

        match op:
            case 1:
                menu_cadastro()

            case 2:
                filtro_busca = filtros(int(1)) # diz ao metodo filtros que será o case 1
                people = find_people("especialistas", filtro_busca)

                if not people:
                    print("Especialista nao encontrado.")
                else:
                    print(f"{len(people)} pessoas foram encontradas:\n")
                    for i, person in enumerate(people, 1):
                        person = Especialista(person['nome'],
                                              person['cpf'],
                                              person['sexo'],
                                              person['data_nascimento'],
                                              person['endereco'],
                                              person['telefone'],
                                              person['cro'],
                                              person['especialidade'],
                                              person['data_engresso'])
                        print(f"{i}-{person}")
                    print("")
                    # Dar opção de  Selecionar Especialista por Indice e printar o especialista
                    if len(people) > 1:
                        escolha = opcao('i', "Digite o indice qual dos especialistas acima você está procurando: ")
                        print(f"{people[escolha-1]}\n")
                    else:
                        print(f"{people}\n")

            case 3:
                filtro_busca = filtros(int(2)) # diz ao metodo filtros que será o case 2
                people = find_people("pacientes", filtro_busca)

                if not people:
                    print("Paciente nao encontrado.")
                else:
                    print(f"{len(people)} pessoas foram encontradas:\n")
                    for i, person in enumerate(people, 1):
                        person = Paciente(person['nome'],
                                              person['cpf'],
                                              person['sexo'],
                                              person['data_nascimento'],
                                              person['telefone'],
                                              person['altura'],
                                              person['peso'],
                                              person['endereco'],
                                              person['nro_sus'])
                        print(f"{i}-{person}")
                    print("")
                    # Dar opção de  Selecionar Especialista por Indice e printar o especialista
                    if len(people) > 1:
                        escolha = opcao('i', "Digite o indice qual dos pacientes acima você está procurando: ")
                        print(f"{people[escolha - 1]}\n")
                    else:
                        print(f"{people}\n")

            case 4:
                # Este case é dependente da classe Prontuário !!!
                pass
            case 5:
                # Provavelmente não será implementado a tempo, então é melhor deixar quieto !!!
                pass
            case 0:
                return