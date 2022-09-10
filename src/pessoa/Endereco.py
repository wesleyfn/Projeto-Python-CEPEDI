class Endereco:
    # Construtor
    def __init__(self, endereco: str, bairro: str, area: str):
        self.endereco = endereco
        self.bairro = bairro
        self.area = area
    
    def __str__(self) -> str:
        pass