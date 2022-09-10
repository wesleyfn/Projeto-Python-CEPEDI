import datetime
from pessoa.Endereco import Endereco
from pessoa.Paciente import Paciente
from menu import menu

data = datetime.datetime.strptime("10 09 2022", "%d %m %Y")
endereco_teste = Endereco("Rua de Wesley", "Roca do Povo", "Condominio")

paciente_teste = Paciente("matheus", "cpf", "M", data, "telefone", 1.75, 75.0, endereco_teste, 125)

menu.main_menu()
