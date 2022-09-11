from src.utils_functions.utils import *

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
                    print(f" > {len(people)} especialistas encontrados:\n")
                    list_all(people, "Especialista")

                    if len(people) > 1:
                        op = opcao('i', " > Escolha o especialista: ")
                        person = dict_to_obj(people[op - 1], "Especialista")
                        print(f"{person}\n")

            case 3:
                filtro_busca = filtros(2)  # diz ao metodo filtros que será o case 2
                people = find_people("pacientes", filtro_busca)

                if not people:
                    print(" > Paciente não encontrado!\n")
                else:
                    print(f" > {len(people)} pessoas foram encontradas:\n")
                    list_all(people, "Paciente")

                    if len(people) > 1:
                        op = opcao('i', " > Escolha o paciente: ")
                        person = dict_to_obj(people[op - 1], "Paciente")
                        print(f"{person}\n")

            case 4:
                # Este case é dependente da classe Prontuário !!!
                pass
            case 5:
                # Provavelmente não será implementado a tempo, então é melhor deixar quieto !!!
                pass
            case 0:
                return
