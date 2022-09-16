from src.pessoa.Pessoa import Pessoa

class Especialista(Pessoa):
    def __init__(self, nome: str, cpf: str, sexo: str, data_nascimento: str,
                 endereco: str, telefone: str, cro: str, especialidade: str,
                 data_engresso: str):

        super().__init__(nome, cpf, sexo, data_nascimento, endereco, telefone)
        self.cro = cro
        self.data_engresso = data_engresso
        self.especialidade = especialidade

    def __str__(self) -> str:
        saida = f"\n     Nome: {self.nome:40}CPF: {self.cpf:21}Data de Engresso: {self.data_engresso}\n"  
        saida += f"     Data de Nascimento: {self.data_nascimento:26}Telefone: {self.telefone:16}CRO: {self.cro}\n"
        saida += f"     Especialidade: {self.especialidade:31}Sexo: {self.sexo}\n     Endereço: {self.endereco}\n"
        return saida
