def registrar_inscripcion():
 
    print("Registro de Inscripción Universitaria")
    nombre = input("Ingrese el nombre del alumno: ")
    edad = input("Ingrese la edad del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (DD/MM/AAAA): ")
    título = True 
    matricula = float(input("Ingrese el monto de la matrícula: "))
    cuota = matricula + 1000
    arancel_mensual = 12000/4
    arancel = arancel_mensual - (arancel_mensual * 0.15)
    print("\Resumen de la Inscripción:")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Fecha de nacimiento:", fecha_nacimiento)
    print("Tiene título secundario:", título)
    print("Matrícula:", matricula)
    print("Cuota mensual:", cuota)
    print("Arancel mensual materia 'Python I':", arancel_mensual)
    print("El valor del arancel de la materia 'Python I' es 12000 y con un descuento es:", arancel )


registrar_inscripcion()