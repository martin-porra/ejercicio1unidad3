import csv
from claseLibro import  libro
from  claseHoja import  capitulo
class manejador:
    __libros = []

    def __init__(self):
      archivo = open('libros.csv')
      reader = csv.reader(archivo, delimiter=(','))
      for fila in reader:
        lib = libro(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
        cant = fila[5]
        for fila1 in reader:
         a = capitulo(fila1[0],fila1[1])
         lib.cap(a)
         cant = int(cant) -1
         if cant == 0:
            break

        self.__libros.append(lib)
      archivo.close()



    def capos(self,c):
     for x in range(0,len(self.__libros)):
      self.__libros[x].caps(c)

    def indenti(self):
     print('ingrese indentificador del libro')
     id = input()
     for x in range(0,len(self.__libros)):
         if self.__libros[x].ide() == id:
          print(self.__libros[x].titulo())
          self.__libros[x].caps()
     else:
      print('identificador no encontrador')
     print('')

    def comprobar(self):
     titu = input('escribir palabra a buscar en titulos ')
     for x in range(0,len(self.__libros)):
         if titu in self.__libros[x].titulo():
             self.__libros[x].tituautor()
         else:
          list = self.__libros[x].capitu()
          for i in range(0,len(list)):
               if titu in list[i].titucap():
                   self.__libros[x].tituautor()
     print('')



