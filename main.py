from manejador import  manejador

def menu():
 print('opcion 1- Buscar identificador')
 print('Opcion 2- buscar palabra en titulos')

if __name__ == '__main__':
 manejalibros =  manejador()
 band = True
 while band == True:
  menu()
  op = input('ingrese opcion ')
  if op == "1":
   manejalibros.indenti()
  elif op == "2":
   manejalibros.comprobar()
  else:
   band = False
 print('opcion incorrecta')
 print('programa terminado')