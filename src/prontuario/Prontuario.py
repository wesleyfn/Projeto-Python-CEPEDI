from src.pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente
from src.pessoa.Responsavel import Responsavel
from src.utils_functions import load_save
from src.utils_functions import menu
from src.utils_functions import utils

def insere_itens(lista, nome_item) -> list:
    while True:
        novo_item = input(f"Novo {nome_item} ou digite 0 para sair: ")
        if novo_item == '0':
            break
        else:
            lista.append(novo_item)
    return lista

def imprime_tipo_consulta() -> list:
    consultas = ["Urgencia", "Tratamento", "Revisão", "Primeira Consulta"]
    return consultas

def patologias() -> list:
    lista_patologias = ["Alcoolismo_(Usa bebida alcóolica)", "Alergia", "Anemia", "Asma", "Cicatrização ruim",
                        "Cirurgia realizada", "Desmaios", "Distúrbios Psicológicos", "Endocardite Bacteriana",
                        "Epilepsia", "Febre Reumática", "Gravidez", "Hepatite", "Herpes/Afta",
                        "HIV_(AIDS)", "Internação Hopitalar", "Pressão arterial Baixa ou Alta",
                        "PNE_(Necessidades Especiais)", "Problema Cardíaco_(Coração)",
                        "Problema Hepático_(Fígado)", "Problema Homonal", "Problema Renal_(Rim)",
                        "Sífilis", "Tabagismo_(Fuma)", "Tatuagem", "Tuberculose", "Tumor", "Outras drogas"]
    return lista_patologias

def busca_pessoas_prontuario(nome_objeto):
    while True:
        person = menu.menu_busca(f"{nome_objeto}", return_busca=True)
        if person is None:
            op = utils.opcao("s", f'Deseja cadastrar {nome_objeto} [S/N]? ')
            menu.menu_cadastro() if (op == 'S' or op == 's') else None
        else:
            return person

def print_pathologies() -> None:
    contador_linhas = int(0)
    for doenca in patologias():
        print(f"| {doenca}", end="")
        contador_linhas += 1
        if contador_linhas % 2 == 0:
            print(" |")

class Prontuario:
    def __init__(self):
        self.especialista = None
        self.responsavel = None
        self.paciente = None
        self.patologia = []
        self.procedimento = []
        self.data = None
        self.consulta = None

    def inicializar_prontuario(self) -> None:
        self.data = input(" > Digite a data do procedimento [dd/mm/aa]: ")
        self.paciente = busca_pessoas_prontuario('Paciente')
        self.consulta = input(f" > Qual o tipo de consulta ({imprime_tipo_consulta()}):\n > ")
        self.especialista = busca_pessoas_prontuario('Especialista')

        print(f"\n")
        print(f" > Quais patologias o paciente possui?\n")
        print_pathologies()
        self.patologia = insere_itens(self.patologia, 'patologia')

        print(f" > Quais procedimentos foram realizados no paciente {self.paciente.nome}?\n")
        self.procedimento = insere_itens(self.procedimento, 'procedimento')
