class Endereco:
    # Construtor
    def __init__(self, endereco: str, bairro: str):
        self.endereco = endereco
        self.bairro = bairro
    
    def __str__(self) -> str:
        return f"""Endereço: {self.endereco}
        Bairro: {self.bairro}"""
