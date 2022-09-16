from src.pessoa.Pessoa import Pessoa
from src.prontuario.Prontuario import Prontuario
from src.utils_functions import load_save
from src.pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente

def limpar_console():
    print("\n" * 100)

def enter_continua():
    input(" > Enter para continuar...")

def barra(title="", n=15):
    if title:
        print(f" {title}")
    print("-=" * n, end="-\n")

def dicionario_objeto(person, nome_objeto):
    if nome_objeto == "prontuario":
        procedimento = person['procedimento']
        patologias = person['patologias']
        consulta = person['tipo_consulta']

        person = Prontuario(person['nome_paciente'],
                            person['data'],
                            person['nome_especialista'],
                            person['nome_responsavel'],
                            person['cpf'])
        person.add_procedimento(procedimento)
        person.add_lista_patologias(patologias)
        person.add_consulta(consulta)

        return person

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

def opcao(tipo: str, string: str, n_opcoes: int = 0):
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
    if onde_buscar != "prontuarios":
        nome_cpf = opcao('s', f" > Digite o nome ou CPF do {onde_buscar[:-1:]}: ")
        filtro = {"cpf": nome_cpf} if nome_cpf.isnumeric() else {"nome": nome_cpf}
    else:
        nome_paciente = opcao('s', f" > Digite o nome do paciente: ")
        filtro = {"nome_paciente": nome_paciente}

    return filtro

def buscar_pessoas(tipo_pessoa) -> list:
    filtro = gerar_filtro(tipo_pessoa)
    pessoas = load_save.carregar_json(tipo_pessoa)
    encontros = []

    if not pessoas:  # retorna []
        return encontros

    for pessoa in pessoas:
        encontrou = True
        for key, valor in filtro.items():
            if valor is None or pessoa[key] is None:
                continue

            elif pessoa[key].isnumeric() and valor.isnumeric():
                if pessoa[key] != valor:
                    encontrou = False
            
            elif valor.lower() not in pessoa[key].lower():
                encontrou = False
        if encontrou:
            encontros.append(pessoa)

    return encontros

def listar_encontrados(lista: Pessoa | list, tipo: str):
    match tipo:
        case "especialista":
            barra("Especialistas")
            print("")
            for i, pessoa in enumerate(lista, 1):
                print(f"   {i}. Nome: {pessoa['nome']}, CRO: {pessoa['cpf']}"
                      f"\n      Especialidade: {pessoa['especialidade']}\n")

        case "paciente":
            barra("Pacientes")
            print("")
            for i, pessoa in enumerate(lista, 1):
                print(f"   {i}. Nome: {pessoa['nome']}, CPF: {pessoa['cpf']}"
                      f"\n      Data de Nascimento: {pessoa['data_nascimento']}\n")

        case "prontuario":
            for i, pessoa in enumerate(lista, 1):
                nome_paciente = pessoa['nome_paciente']
                nome_especialista = pessoa['nome_especialista']
                data = pessoa['data']
                tipo_consulta = pessoa['tipo_consulta']
                procedimento = pessoa['procedimento']

                print(f"   {i}. Paciente: {nome_paciente}, Data: {data}\n"
                      f"      Tipo de consulta: {tipo_consulta}\n"
                      f"      Procedimento: {procedimento}\n"
                      f"      Especialista: {nome_especialista}")
    barra()

def mostrar_prontuario(prontuario: Prontuario):
    pessoas = load_save.carregar_json("pacientes")
    encontrada = None
    for pessoa in pessoas:
        if pessoa["cpf"] == prontuario.cpf:
            encontrada = pessoa
    
    print(f"\n     Paciente: {encontrada['nome']:40} CPF: {encontrada['cpf']:21} SUS: {encontrada['nro_sus']}\n"
            f"     Altura: {encontrada['altura']:.3}     Peso: {encontrada['peso']}     Sexo: {encontrada['sexo']:10}"  
            f"Telefone: {encontrada['telefone']:15}\n     Responsável: {prontuario.nome_responsavel}\n"
            f"     Endereço: {encontrada['endereco']}\n"
            f"     Tipo de consulta: {prontuario.tipo_consulta:20} Procedimento: {prontuario.procedimento}\n"
            f"     Patologias: {prontuario.mostrar_patologias_S()}\n"
            f"     Especialista: {prontuario.nome_especialista:40} Data da consulta: {prontuario.data}\n")
    
    
    
