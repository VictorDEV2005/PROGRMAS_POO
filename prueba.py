class Profesores:
  def __init__(self, nombre, materia):
      self.nombre = nombre
      self.materia = materia

  def calificar(self):
      print(f"El profesor {self.nombre} califica evaluaciones de la materia {self.materia}")

  def pasaAsistencia(self):
      print(f"El profesor {self.nombre} pasa asistencia")

profesor1 = Profesores("Profesor 1", "Materia 1")
profesor1.calificar()
profesor1.pasaAsistencia()