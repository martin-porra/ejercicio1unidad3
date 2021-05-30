
class capitulo:
    __titulo = ''
    __cantidadpag = 0

    def __init__(self, titulo,cant):
        self.__titulo = titulo
        self.__cantidadpag = cant

    def titucap(self):
        return self.__titulo
    def cantpag(self):
        return  self.__cantidadpag