import Empresa

class Empresa(Empresa.Empresa):
    def __init__(self, compradores, administrador):
        self.compradores = compradores
        self.administrador = administrador