
import os.path
from pessoa.Endereco import Endereco
from pessoa.Paciente import Paciente
from menu import menu
from load_save import load_save

endereco_teste = Endereco("Rua de Wesley", "Roca do Povo", "Condominio")

paciente_teste = Paciente("matheus", "cpf", "M", "15/07/1923", "telefone", 1.75, 75.0, endereco_teste, 125)

menu.main_menu()

