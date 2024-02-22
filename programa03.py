"""
PROGRAMA 03
nombre: victor
matricula=1723110220
grupo=21
fecha:18-01-2024
descripcion:contienela creacion de la clase alumnos y sus atributos
"""
class Alumnos:#creacion de la clase Alumnos
  matricula=None#definicion de variable matricula
  nombre=None#definicion de variable nombre
  def __init__ (self, matricula, nombre):#definicion de la funcion init
    self.matricula=matricula#asignamos el valor de la variable matricula
    self.nombre=nombre#asignamos el valor de la variable nombre

objetoAlumnos=Alumnos(nombre="victor",matricula=1723110220)#creacion de la instancia y asignacion de valores
print(objetoAlumnos.matricula, objetoAlumnos.nombre)#imprimimos la variable matricula y nombre