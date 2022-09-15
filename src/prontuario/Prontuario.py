class Prontuario:
    def __init__(self, nome_paciente: str, data: str, nome_especialista: str, nome_responsavel: str):
        self.nome_paciente = nome_paciente
        self.nome_responsavel = nome_responsavel
        self.nome_especialista = nome_especialista
        self.data = data

        self.patologias = []
        self.tipo_consulta = None
        self.procedimento = None

    def mostrar_consultas(self):
        for i, consulta in enumerate(self.__lista_consultas(), 1):
            print(f"   {i}. {consulta}")
        return

    def add_consulta(self, escolhida: int | str):
        if isinstance(escolhida, str):
            self.tipo_consulta = escolhida
        else:
            self.tipo_consulta = self.__lista_consultas(escolhida)

    def mostrar_patologias_L(self):
        x = [' '] * 29
        for i, patologia in enumerate(self.__lista_patologias(), 1):
            for j in self.patologias:
                if j == patologia:
                    x[i - 1] = 'X'

            if i < 10:
                print(f"  {i}. [{x[i - 1]}] {patologia:35}", end="")
            else:
                print(f" {i}. [{x[i - 1]}] {patologia:35}", end="")
            if i % 2 == 0:
                print("")
        return

    def add_patologia(self, escolhida: int):
        self.patologias.append(self.__lista_patologias(escolhida))
        self.patologias = list(set(self.patologias))

    def add_lista_patologias(self, lista_patologias: list):
        self.patologias = lista_patologias

    def __lista_patologias(self, escolhida: int = None) -> list:
        lista = [
            "Alcoolismo (Usa bebida alcóolica)", "Alergia", "Anemia", "Asma", "Cicatrização ruim",
            "Cirurgia realizada", "Desmaios", "Distúrbios Psicológicos", "Endocardite Bacteriana",
            "Epilepsia", "Febre Reumática", "Gravidez", "Hepatite", "Herpes/Afta", "HIV (AIDS)",
            "Internação Hopitalar", "Pressão arterial Baixa ou Alta", "PNE (Necessidades Especiais)",
            "Problema Cardíaco (Coração)", "Problema Hepático (Fígado)", "Problema Homonal",
            "Problema Renal (Rim)", "Sífilis", "Tabagismo (Fuma)", "Tatuagem", "Tuberculose", "Tumor",
            "Outras drogas"
        ]
        if escolhida is not None:
            return lista[escolhida - 1]
        return lista

    def __lista_consultas(self, escolhida: int = None) -> str | list[str]:
        lista = ["Urgencia", "Tratamento", "Revisão", "Primeira Consulta"]
        if escolhida is not None:
            return lista[escolhida - 1]
        return lista

    def add_procedimento(self, procedimento: str):
        self.procedimento = procedimento

    def __str__(self):
        return "Teste"
