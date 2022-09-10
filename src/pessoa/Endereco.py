class Endereco:
    # Construtor
    def __init__(self, endereco: str, bairro: str, area: str):
        self._endereco = endereco
        self._bairro = bairro
        self._area = area
    
    def __str__(self) -> str:
        pass

    # Gets
    @property
    def endereco(self) -> str:
        return self._endereco

    @property
    def bairro(self) -> str:
        return self._bairro
    
    @property
    def area(self) -> str:
        return self._area
    
    # Sets
    @endereco.setter
    def endereco(self, endereco_setter: str) -> None:
        self._endereco = endereco_setter
    
    @bairro.setter
    def bairro(self, bairro_setter: str) -> None:
        self._bairro = bairro_setter
    
    @area.setter
    def area(self, area_setter: str) -> None:
        self._endereco = area_setter
    
