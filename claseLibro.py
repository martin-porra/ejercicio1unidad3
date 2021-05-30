from claseHoja import  capitulo
class libro:
    __idlibro = 0
    __titulo = ''
    __autor = ''
    __editorial = ''
    __isbn = 0
    __cantcapitulos = 0

    def __init__(self,id,titulo,autor,editorial,isbn,cant):
        self.__idlibro = id
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__isbn = isbn
        self.__cantcapitulos = cant
        self.__capitulos = []
    def cap(self,x):
        self.__capitulos.append(x)

    def ide(self):
     return self.__idlibro

    def titulo(self):
        return  self.__titulo

    def caps(self):
     suma = 0
     for x in range(0,len(self.__capitulos)):
      print(self.__capitulos[x].titucap())
      suma =  int(self.__capitulos[x].cantpag()) + suma
     print('cantidad de paginas del libro es: ' + str(suma))

    def tituautor(self):
     print(self.__titulo)
     print(self.__autor)

    def capitu(self):
     return self.__capitulos