from src.utils_functions.utils import *
from src.prontuario.Prontuario import Prontuario

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

def menu_busca(nome_objeto, return_busca=False):
    filtro_busca = filtros(nome_objeto)
    people = find_people(f"{nome_objeto.lower()}s", filtro_busca)

    if not people:
        print(f" > {nome_objeto} não encontrado!\n")
        return None
    else:
        if len(people) == 1:
            print(f" > {len(people)} {nome_objeto.lower()} foi encontrado:\n")
        else:
            print(f" > {len(people)} {nome_objeto.lower()}s foram encontrados:\n")
        list_all(people, nome_objeto)

        op = opcao('i', f" > Escolha o {nome_objeto.lower()}: ")
        person = dict_to_obj(people[op - 1], nome_objeto)

        if return_busca:
            return person
        print(f"{person}\n")

def menu_cadastro():
    loop_condition = True

    while loop_condition:
        print(" 1. Cadastrar Especialista\n 2. Cadastrar Paciente\n 3. Cadastrar Prontuário\n 0. Voltar")
        op = opcao('i', " > Opção:")
        print("")

        match op:
            case 1:
                nome, cpf, sexo, data_nascimento, endereco, telefone = cadastro_pessoa()
                cro = opcao('s', " > Digite o CRO: ")
                data_engresso = opcao('s', " > Digite a data de engresso [dd/mm/aa]: ")
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
                prontuario = Prontuario()
                prontuario.inicializar_prontuario()

                load_save.save_prontuario(prontuario)
            case 0:
                return

def main_menu():
    loop_condition = True
    while loop_condition:
        print(" 1. Cadastros\n"
              " 2. Buscar Especialista\n"
              " 3. Buscar Paciente\n"
              " 4. Buscar Prontuário\n"
              " 0. Sair")
        op = opcao('i', " > Digite a opção: ")
        print("")

        match op:
            case 1:
                menu_cadastro()
            case 2:
                menu_busca("Especialista")
            case 3:
                menu_busca("Paciente")
            case 4:
                menu_busca("Prontuario")
            case 0:
                return
