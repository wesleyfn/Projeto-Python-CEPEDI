from src.pessoa.Especialista import Especialista
from src.pessoa.Paciente import Paciente
from src.pessoa.Endereco import Endereco

def dict_to_obj(person, nome_objeto):
    person['endereco'] = Endereco(person['endereco']['endereco'],
                                  person['endereco']['bairro'],
                                  person['endereco']['area'])

    if nome_objeto == "Especialista":
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
    elif nome_objeto == "Paciente":
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
