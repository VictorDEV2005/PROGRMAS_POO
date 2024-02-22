"""
Programa: eva01.py
Alumno:
Matricula:
Fecha:
"""
class profesores():
  id = None
  nombre = ""
  materias = []
  def __init__(self, id, nombre):
    self.id = id
    self.nombre = nombre
    print("ClaseProfesor")
    
  def califica(self):
    print("El profesor {} califica evaluaciones de la materia {}".format(self.nombre, self.materias[0]))
  def pasaAsistencia(self):
    print(f"El profesor {self.nombre} pasa asistencia")


profesor1 = profesores("111","Profesor 1")
profesor1.materias.append("Materia 1")
profesor1.materias.append("Materia 2")
profesor1.califica()
profesor1.pasaAsistencia()