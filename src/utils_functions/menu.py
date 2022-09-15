from src.utils_functions.utils import *
from src.prontuario.Prontuario import Prontuario

def iniciando():
    limpar_console()
    barra("Sistema Iniciado!")
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
        limpar_console()
        match op:
            case 1:
                encontrar_listando("especialista")
            case 2:
                encontrar_listando("paciente")
            case 3:
                encontrar_listando("prontuario")
            case 0:
                return


def menu_cadastro(ignore_print=-1):
    while True:
        op = 0
        if ignore_print == -1:
            limpar_console()
            barra(" Cadastrar")
            print(" 1. Especialista\n"
                  " 2. Paciente\n"
                  " 3. Prontuário\n"
                  " 0. Voltar")
            barra()
            op = opcao('i', " > Escolha a opção: ", 3)
            limpar_console()
        else:
            op = ignore_print

        match op:
            case 1:
                nome, cpf, sexo, data_nascimento, endereco, telefone = cadastro_pessoa()
                cro = opcao('s', " > Digite o CRO: ")
                data_engresso = opcao('s', " > Digite a data de engresso (dd/mm/aa): ")
                especialidade = opcao('s', " > Digite a especialidade: ")
                especialista = Especialista(nome, cpf, sexo, data_nascimento, endereco,
                                            telefone, cro, especialidade, data_engresso)

                load_save.salvar_especialista(especialista)
            case 2:
                nome, cpf, sexo, data_nascimento, endereco, telefone = cadastro_pessoa()
                altura = opcao('f', " > Digite a altura: ")
                peso = opcao('f', " > Digite o peso: ")
                nro_sus = opcao('s', " > Digite o número do SUS: ")
                paciente = Paciente(nome, cpf, sexo, data_nascimento,
                                    telefone, altura, peso, endereco, nro_sus)

                load_save.salvar_paciente(paciente)
            case 3:
                prontuario = cadastro_prontuario()
                if prontuario:
                    load_save.salvar_prontuario(prontuario)
            case 0:
                return
        ignore_print = 0


def cadastro_pessoa() -> tuple:
    barra("Cadastrando...")
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
    resposta_s = ['s','sim', 'yes']

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
        if op.lower() in resposta_s: 
            menu_cadastro(2)
            paciente_encontrado = load_save.carregar_json("pacientes")[-1]
        else:
            return None

    responsavel = opcao('s', f"\n > Digite o nome do responsável: ")
    print("")

    # Especialista
    especialistas = buscar_pessoas("especialistas")
    if especialistas:
        listar_encontrados(especialistas, "especialista")
        op = opcao('i', f" > Escolha o especialista: ", len(especialistas))
        especialista_encontrado = especialistas[op - 1]
    else:
        op = opcao('s', "\n > Especialista não encontrado, cadastrar novo especialista? [s/n]: ")
        if op.lower() in resposta_s: 
            menu_cadastro(1)
            especialista_encontrado = load_save.carregar_json("especialistas")[-1]
        else:
            return None

    data = opcao('s', "\n > Digite a data da consulta (dd/mm/aa): ")
    print("")

    prontuario = Prontuario(paciente_encontrado['nome'], data,
                            especialista_encontrado['nome'],
                            responsavel)
    while True:
        prontuario.mostrar_consultas()
        op = opcao('i', " > Escolha o tipo de consulta (0 p/sair): ", 4)
        prontuario.add_consulta(op)
        if 0 <= op < 5:
            break

    while True:
        limpar_console()
        prontuario.mostrar_patologias_L()
        op = opcao('i', " > Selecione as patologias (0 p/sair): ", 28)
        prontuario.add_patologia(op)
        if op == 0:
            break

    procedimento = opcao("s", f"\n > Digite o procedimento adotado: ")
    prontuario.add_procedimento(procedimento)

    return prontuario


def encontrar_listando(tipo_pessoa, return_busca=False) -> Paciente | None:
    resposta_s = ['s', 'sim', 'yes', 'y']

    pessoas = buscar_pessoas(f"{tipo_pessoa}s")
    if not pessoas:
        print(f"\n > {tipo_pessoa} não encontrado!\n")
        enter_continua()
        return None
    else:
        if len(pessoas) == 1:
            print(f" > {len(pessoas)} {tipo_pessoa} foi encontrado:\n")
        else:
            print(f" > {len(pessoas)} {tipo_pessoa}s foram encontrados:\n")

        listar_encontrados(pessoas, tipo_pessoa)

        op = opcao('i', f" > Escolha o {tipo_pessoa}: ", len(pessoas))
        pessoa_selecionado = pessoas[op - 1]
        pessoa = dict_to_obj(pessoas[op - 1], tipo_pessoa)

        if return_busca:
            return pessoa
        print(pessoa)

        op = opcao('i', f" > Escolha o 1 para deletar, 0 para sair: ")
        if op == 1:
            for i, pessoa_atual in enumerate(pessoas):
                if pessoa_atual == pessoa_selecionado:
                    del pessoas[i]

                    load_save.atualizar_registro(tipo_pessoa + "s", pessoas)
        elif op == 2:
            for i, pessoa_atual in enumerate(pessoas):
                if pessoa_atual == pessoa_selecionado:
                    for chave, valor in pessoa_selecionado.items():
                        print(f"{chave.capitalize()}: {valor}")
                        op = opcao('s', f" > Deseja atualizar esse campo [s/n]?: ")

                        if op in resposta_s:
                            novo_valor = None

                            if isinstance(valor, float):
                                novo_valor = opcao("i", f"Digite o novo {chave}: ")
                            elif isinstance(valor, str):
                                novo_valor = opcao("s", f"Digite o novo {chave}: ")

                            pessoa_selecionado[chave] = novo_valor
                pessoas[i] = pessoa_selecionado
                load_save.atualizar_registro(tipo_pessoa + "s", pessoas)

        enter_continua()

def menu_principal():
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
