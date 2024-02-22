""""
PROGRAMA 05
nombre: victor
matricula=1723110220
grupo=21
fecha:18-01-2024
descripcion=programa que sirve para crear una clase, agregar sus atributos y insertar datos 
"""

class alumnos:#creacion de la clase
  matricula=None#atributo matricula definida para la clase alumnos
  nombre=None#atributo nombre definido para la clase alumnos
  def __init__ (self, matricula, nombre):#definicion del constructor
    self.matricula=matricula#accediendo a la variable matricula de la clase alumnos
    self.nombre=nombre#accediendo a la variable nombre de la clase alumnos
    print("objetos Alumnos")#imprimiendo el mensaje objetos Alumnos
  def estudiar(self):#definicion del metodo estudiar
    print(f"{self.nombre} estudia")#imprimiendo el mensaje estudia
  def sumar (self, numero1, numero2):#definicion del metodo sumar
    suma=numero1+numero2#definicion de la variable suma y sumar los valores de numero1 y numero2
    print(f"la suma de {numero1} y {numero2} es {suma}")#imprimiendo el mensaje la suma de {numero1} y {numero2} es {suma}
dejah=alumnos(111,"dejah")#creacion del objeto de la clase alumno
dejah.estudiar()#invocacion del metodo estudiar del objeto de la clase alumno
dejah.sumar(10,5)#invocacion del metodo sumar del objeto de la clase alumno