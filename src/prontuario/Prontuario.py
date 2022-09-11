from src.pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente
from src.pessoa.Responsavel import Responsavel


def insere_itens(lista) -> list:
    while True:
        novo_item = input(" Nova item ou digite 0 para sair: ")
        if novo_item.isnumeric():
            break

        lista.append(novo_item)
        print(f"\n")
        return lista


def imprime_tipo_consulta() -> list:
    consultas = ["Urgencia", "Tratamento", "Revisão", "Primeira Consulta"]
    return consultas


class Prontuario:
    def __init__(self):
        self.especialista = None
        self.responsavel = None
        self.paciente = None
        self.patologia = None
        self.procedimento = None
        self.data = None
        self.consulta = None

    def inicializar_prontuario(self, especialista: Especialista, paciente: Paciente, responsavel: Responsavel =
                               None) -> None:
        self.especialista = especialista
        self.paciente = paciente
        self.responsavel = responsavel if responsavel else None
        self.patologia = []
        self.procedimento = []
        self.data = input(" > Digite a data do procedimento: ")
        self.consulta = input(f" > Qual o tipo de consulta ({imprime_tipo_consulta()}):\n > ")

        print(f"\n")
        self.print_pathologies()
        print(f" > Das patologias acima, quais o paciente possui?\n")
        self.patologia = insere_itens(self.patologia)

        print(f" > Quais procedimentos serão realizados no paciente {self.paciente.nome}?\n")
        self.procedimento = insere_itens(self.patologia)

    def patologias(self) -> list:
        lista_doencas = ["Alcoolismo_(Usa bebida alcóolica)", "Alergia", "Anemia", "Asma", "Cicatrização ruim",
                         "Cirurgia realizada", "Desmaios", "Distúrbios Psicológicos", "Endocardite Bacteriana",
                         "Epilepsia", "Febre Reumática", "Gravidez", "Hepatite", "Herpes/Afta",
                         "HIV_(AIDS)", "Internação Hopitalar", "Pressão arterial Baixa ou Alta",
                         "PNE_(Necessidades Especiais)", "Problema Cardíaco_(Coração)",
                         "Problema Hepático_(Fígado)", "Problema Homonal", "Problema Renal_(Rim)",
                         "Sífilis", "Tabagismo_(Fuma)", "Tatuagem", "Tuberculose", "Tumor", "Outras drogas"]
        return lista_doencas

    def print_pathologies(self) -> None:
        contador_linhas = int(0)
        for doenca in self.patologias():
            print(f"\t{doenca}\t")
            contador_linhas += 1
            if contador_linhas % 2 == 0:
                print(f"\n")
