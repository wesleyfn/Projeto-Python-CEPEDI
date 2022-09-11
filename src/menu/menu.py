from src.pessoa.Paciente import Paciente
from src.pessoa.Especialista import Especialista
from src.pessoa.Endereco import Endereco
from src.load_save import load_save

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
        finally:
            return x

def filtros(onde_buscar: int) -> dict:
    nome = opcao('s', " > Digite o nome: ")
    cpf = opcao('s', " > Digite o CPF: ")

    filtro_busca = {"nome": nome, "cpf": cpf}

    match onde_buscar:
        case 1:  # case especilista
            cro = opcao('s', " > Digite o CRO: ")
            filtro_busca["cro"] = cro

        case 2:  # case paciente
            nro_sus = opcao('s', " > Digite o número do SUS: ")
            filtro_busca["nro_sus"] = nro_sus

        case 3:  # case prontuário
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
                cro = opcao('s', " > Digite o CRO: ")
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
                nro_sus = opcao('s', " > Digite o número do SUS: ")
                print("\n")
                paciente = Paciente(nome, cpf, sexo, data_nascimento, telefone, altura, peso, endereco, nro_sus)

                load_save.save_paciente(paciente)
            case 3:

                pass
            case 0:
                return

def find_people(nome_json, filtro_busca):
    peoples = load_save.load_json(nome_json)
    matchs = []

    if not peoples:
        return []

    for person in peoples:
        find = False
        print("fffffffffffffffff")
        for key, value in filtro_busca.items():
            if value is None or person[key] == None:
                print(f"{key} AAAAAAAAAAAAAAAAAAAAAAAAAA")
                continue

            if person[key].isnumeric() and value.isnumeric():
                print(f"{key} iiiiiiiiiiiiiii")
                if person[key] == value:
                    print(f"{key} oooooooooooooooooo")
                    find = True
                    break
            elif person[key].lower() == value.lower():
                print(f"{key} uuuuuuuuuuuuuu")
                find = True
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
                filtro_busca = filtros(1)  # diz ao metodo filtros que será o case 1
                people = find_people("especialistas", filtro_busca)

                if not people:
                    print(" > Especialista não encontrado!\n")
                else:
                    print(f" > {len(people)} especialistas encontradas:\n")
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
                        op = opcao('i', " > Escolha o especialista procurado: ")
                        print(f"{people[op - 1]}\n")
                    else:
                        print(f"{people}\n")

            case 3:
                filtro_busca = filtros(2)  # diz ao metodo filtros que será o case 2
                people = find_people("pacientes", filtro_busca)

                if not people:
                    print(" > Paciente não encontrado!\n")
                else:
                    print(f" > {len(people)} pessoas foram encontradas:\n")
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
                    # Dar opção de  Selecionar Paciente por Indice e printar o paciente
                    if len(people) > 1:
                        op = opcao('i', " > Escolha o especialista procurado: ")
                        print(f"{people[op - 1]}\n")
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
