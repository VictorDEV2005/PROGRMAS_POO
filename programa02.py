"""
PROGRAMA 02
nombre: victor
matricula=1723110220
grupo=21
fecha:18-01-2024
descripcion:programa para crea una clase y agregar atributos apartir del constructor
"""
class A:#creacion de la clase A
  matricula=None#definicion de variable matricula
  nombre=None#definicion de variable nombre
  def __init__ (self):#creacion de la funcion init
    print("Constructor de la clase A")#imprimimos el mensaje
objetoA=A()#creamos una instancia de la clase A
print(objetoA.nombre)#imprimimos la variable nombre
print(objetoA.matricula)#imprimimos la variable matricula
