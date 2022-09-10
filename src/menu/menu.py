import datetime
from src.pessoa.Paciente import Paciente
from src.pessoa.Especialista import Especialista
from src.prontuario import Prontuario
from src.pessoa.Responsavel import Responsavel
from src.pessoa.Endereco import Endereco

def cadastro_pessoa():
    nome = input("Digite o nome: ")
    cpf = input("Digite o cpf: ")
    sexo = input("Digite o sexo [M] [F]: ")

    dia, mes, ano = input("Digite a data de nascimento Dia/Mes/Ano: ").split("/")
    data_nascimento = datetime.datetime.strptime(f"{dia} {mes} {ano}", "%d %m %Y")

    endereco = input("Digite o endereço: ")
    bairro = input("Digite o bairro: ")
    area = input("Digite a área [Comercial] [Residencial] [Rural]: ")
    endereco = Endereco(endereco, bairro, area)

    telefone = input("Digite o telefone: ")

    return nome, cpf, sexo, data_nascimento, endereco, telefone


def menu_cadastro():
    loop_condition = True
    opcao = -1

    while loop_condition:
        print("1-Cadastrar Especialista\n2-Cadastrar Paciente\n3-Cadastrar Prontuáio\n0-Voltar\n")
        opcao = int(input("Digite a opção: "))
        print("\n")

        match opcao:
            case 1:
                nome, cpf, sexo, data_nascimento, endereco, telefone = cadastro_pessoa()
                cro = int(input("Digite o CRO: "))

                dia, mes, ano = input("Digite a data de engresso Dia/Mes/Ano: ").split("/")
                data_engresso = datetime.datetime.strptime(f"{dia} {mes} {ano}", "%d %m %Y")

                especialidade = input("Digite a especialidade: ")
                especialista = Especialista(nome, cpf, sexo, data_nascimento, endereco, telefone, cro, especialidade,
                                            data_engresso)
            case 2:
                nome, cpf, sexo, data_nascimento, endereco, telefone = cadastro_pessoa()
                altura = float(input("Digite a altura: "))
                peso = float(input("Digite o peso: "))
                nro_sus = int(input("Digite o número do SUS: "))

                paciente = Paciente(nome, cpf, sexo, data_nascimento, telefone, altura, peso, endereco, nro_sus)

            case 3:
                pass
            case 0:
                return


def main_menu():
    loop_condition = True
    opcao = -1

    while loop_condition:
        print("1-Cadastros\n"
              "2-Buscar Especialista\n"
              "3-Buscar Paciente\n"
              "4-Buscar Prontuário\n"
              "5-Importar/Exportar Prontuário\n"
              "0-Sair\n")
        opcao = int(input("Digite a opção: "))
        print("")

        match opcao:
            case 1:
                menu_cadastro()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 0:
                return
