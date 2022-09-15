from src.utils_functions.utils import *
from src.prontuario.Prontuario import Prontuario


def iniciando():
    limpar_console()
    print(" Sistema Iniciado!")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    enter_continua()


def menu_busca():
    op = ""
    while True:
        limpar_console()
        barra(" Buscar")
        print(" 1. Especialista\n"
              " 2. Paciente\n"
              " 3. Prontuario\n"
              " 0. Voltar")
        barra()
        op = opcao('i', " > Escolha a opção: ")
        match op:
            case 1:
                encontrar_listando("especialista")
            case 2:
                encontrar_listando("paciente")
            case 3:
                encontrar_listando("prontuario")  # Não está funcionando
            case 0:
                return


def menu_cadastro(ignore_print=-1):
    while True:
        limpar_console()
        barra(" Cadastrar")
        op = 0
        if ignore_print == -1:
            print(" 1. Especialista\n"
                  " 2. Paciente\n"
                  " 3. Prontuário\n"
                  " 0. Voltar")
            barra()
            op = opcao('i', " > Escolha a opção: ", 3)
        else:
            op = ignore_print

        match op:
            case 1:
                nome, cpf, sexo, data_nascimento, endereco, telefone = cadastro_pessoa()
                cro = opcao('s', " > Digite o CRO: ")
                data_engresso = opcao('s', " > Digite a data de engresso [dd/mm/aa]: ")
                especialidade = opcao('s', " > Digite a especialidade: ")
                especialista = Especialista(nome, cpf, sexo, data_nascimento, endereco,
                                            telefone, cro, especialidade, data_engresso)

                load_save.save_especialista(especialista)
            case 2:
                nome, cpf, sexo, data_nascimento, endereco, telefone = cadastro_pessoa()
                altura = opcao('f', " > Digite a altura: ")
                peso = opcao('f', " > Digite o peso: ")
                nro_sus = opcao('s', " > Digite o número do SUS: ")
                paciente = Paciente(nome, cpf, sexo, data_nascimento,
                                    telefone, altura, peso, endereco, nro_sus)

                load_save.save_paciente(paciente)
            case 3:
                prontuario = cadastro_prontuario()
                if prontuario:
                    load_save.save_prontuario(prontuario)
            case 0:
                return
        ignore_print = 0


def cadastro_pessoa() -> tuple:
    nome = opcao('s', " > Digite o nome: ")
    cpf = opcao('s', " > Digite o CPF (apenas números): ")
    sexo = opcao('s', " > Digite o sexo [M/F]: ")
    data_nascimento = opcao('s', " > Digite a data de nascimento (dd/mm/aa): ")
    endereco = opcao('s', " > Digite o endereço: ")
    bairro = opcao('s', " > Digite o bairro: ")
    endereco = Endereco(endereco, bairro)
    telefone = opcao('s', " > Digite o telefone: ")

    return nome, cpf, sexo, data_nascimento, endereco, telefone

def cadastro_prontuario():
    op = ""
    paciente_encontrado, especialista_encontrado = {}, {}

    # Paciente
    limpar_console()
    barra(" Cadastro de Prontuario", 20)
    pacientes = buscar_pessoas("pacientes")
    if pacientes:
        listar_encontrados(pacientes, "paciente")
        op = opcao('i', f" > Escolha o paciente: ", len(pacientes))
        paciente_encontrado = pacientes[op - 1]
    else:
        op = opcao('s', "\n > Paciente não encontrado, cadastrar novo paciente? [s/n]: ")
        if op == 's':
            menu_cadastro(2)
            paciente_encontrado = load_save.load_json("pacientes")[-1]
        else:
            return None

    responsavel = opcao('s', f" > Digite o nome do responsável: ")

    # Especialista
    especialistas = buscar_pessoas("especialistas")
    if especialistas:
        listar_encontrados(especialistas, "especialista")
        op = opcao('i', f" > Escolha o especialista: ", len(especialistas))
        especialista_encontrado = especialistas[op - 1]
    else:
        op = opcao('s', "\n > Especialista não encontrado, cadastrar novo especialista? [s/n]: ")
        if op == 's':
            menu_cadastro(1)
            especialista_encontrado = load_save.load_json("especialistas")[-1]
        else:
            return None

    data = opcao('s', " > Digite a data (dd/mm/aa): ")

    prontuario = Prontuario(paciente_encontrado['nome'], data,
                            especialista_encontrado['nome'])
    while True:
        prontuario.mostrar_consultas()
        op = opcao('i', " > Escolha o tipo de consulta (0 p/sair): ", 4)
        prontuario.add_consulta(op)
        if 0 <= op < 5:
            break

    while True:
        prontuario.mostrar_patologias_L()
        op = opcao('i', " > Selecione as patologias (0 p/sair): ", 28)
        prontuario.add_patologia(op)
        if op == 0:
            break

    procedimento = opcao("s", f"Digite o procedimento adotado: ")
    prontuario.add_procedimento(procedimento)

    return prontuario


def encontrar_listando(tipo_pessoa, return_busca=False) -> Paciente | None:
    people = buscar_pessoas(f"{tipo_pessoa}s")

    if not people:
        print(f"\n > {tipo_pessoa} não encontrado!\n")
        return None
    else:
        if len(people) == 1:
            print(f" > {len(people)} {tipo_pessoa} foi encontrado:\n")
        else:
            print(f" > {len(people)} {tipo_pessoa}s foram encontrados:\n")

        listar_encontrados(people, tipo_pessoa)

        op = opcao('i', f" > Escolha o {tipo_pessoa}: ", len(people))
        person = dict_to_obj(people[op - 1], tipo_pessoa)

        if return_busca:
            return person
        print(person)


def main_menu():
    while True:
        limpar_console()
        barra(" Menu Principal")
        print(" 1. Cadastrar\n"
              " 2. Buscar\n"
              " 0. Sair")
        barra()
        op = opcao('i', " > Escolha a opção: ", 4)

        match op:
            case 1:
                menu_cadastro()
            case 2:
                menu_busca()
            case 0:
                return
