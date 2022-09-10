class Endereco:
    # Construtor
    def __init__(self, endereco:str, bairro:str, area:str):
        self.__endereco = endereco
        self.__bairro = bairro
        self.__area = area
    
    def __str__(self) -> str:
        pass

    # Gets
    @property
    def endereco(self) -> str:
        return self.__endereco

    @property
    def bairro(self) -> str:
        return self.__bairro
    
    @property
    def area(self) -> str:
        return self.__area
    
    # Sets
    @endereco.setter
    def endereco(self, endereco_setter: str) -> None:
        self.__endereco = endereco_setter
    
    @bairro.setter
    def bairro(self, bairro_setter: str) -> None:
        self.__bairro = bairro_setter
    
    @area.setter
    def area(self, area_setter: str) -> None:
        self.__endereco = area_setter
    
