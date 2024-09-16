def evaluar_desempeño():
  nota1 = float(input("Ingrese la nota del primer parcial (0-10): "))
  while nota1 < 0 or nota1 > 10:
      nota1 = float(input("Nota inválida. Ingrese la nota del primer parcial (0-10): "))

  nota2 = float(input("Ingrese la nota del segundo parcial(0-10): "))
  while nota2 < 0 or nota2 > 10:
      nota2 = float(input("Nota inválida. Ingrese la nota del segundo parcial (0-10): "))
  promedio = (nota1 + nota2) / 2
  if nota2 >= 7:
      print("El alumno aprobó el segundo parcial.")
  else:
      print("El alumno desaprobó el segundo parcial.")
  if nota2 > nota1:
      print("El alumno mejoró su desempeño.")
  elif nota2 < nota1:
      print("El alumno empeoró su desempeño.")
  else:
      print("El alumno mantuvo su nota.")
  if promedio >= 7:
      print("El alumno promocionó la materia.")
  elif promedio >= 4:
      print("El alumno debe rendir final.")
  else:
      print("El alumno debe recursar.")
evaluar_desempeño()