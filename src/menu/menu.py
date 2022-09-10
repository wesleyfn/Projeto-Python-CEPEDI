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
        print("\n")

        match op:
            case 1:
                nome, cpf, sexo, data_nascimento, endereco, telefone = cadastro_pessoa()
                cro = opcao('i', " > Digite o CRO: ")
                data_engresso = opcao('s', " > Digite a data de engresso dd/mm/aa: ")
                especialidade = opcao('s', " > Digite a especialidade: ")
                print("\n")
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

    for person in people:
        find = 1
        for key, value in filtro_busca.items():
            if value is None:
                continue

            if person[key].lower() != value.lower():
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
                nome = input("Digite o nome: ")
                nome = nome.lower() if nome else None

                cro = input("Digite o cro: ")
                cro = cro if cro else None

                cpf = input("Digite o cpf: ")
                cpf = cpf if cpf else None

                filtro_busca = {"_cro": cro, "_nome": nome}
                people = find_people("especialistas", filtro_busca)

                for person in people:
                    print(person['_nome'])

            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 0:
                return