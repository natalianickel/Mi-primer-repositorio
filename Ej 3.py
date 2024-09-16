def asignacion_aula(dia):
  
    if dia % 2 == 0:
        return "A-300"
    else:
        return "A-315"

def calcular_descuento(turno, num_materias, cuota):
    
    if turno.lower() == "tarde" and num_materias > 3:
        descuento = cuota * 0.25
    else:
        descuento = cuota * 0.05
    return descuento

def calcular_estacionamiento(medio_transporte):
    if medio_transporte.lower() in ["auto", "moto"]:
        return 300
    elif medio_transporte.lower() == "bicicleta":
        return 50
    else:
        return 0

dia = int(input("Ingrese el número del día (1-6): "))
aula = asignacion_aula(dia)
print("El aula asignada para el día", dia, "es:", aula)

turno = input("Ingrese el turno (Mañana/Tarde): ")
num_materias = int(input("Ingrese el número de materias: "))
cuota_base = float(input("Ingrese el valor de la cuota base: $"))
descuento = calcular_descuento(turno, num_materias, cuota_base)
cuota_final = cuota_base - descuento
print("El descuento es de: $", descuento)
print("La cuota final es de: $", cuota_final)

medio_transporte = input("Ingrese el medio de transporte (auto, moto, bicicleta): ")
costo_estacionamiento = calcular_estacionamiento(medio_transporte)
print("El costo del estacionamiento es de: $", costo_estacionamiento)