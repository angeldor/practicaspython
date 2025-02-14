import matplotlib.pyplot as plt

tna = 0
aporte_mensual = 0
anos = 0
ajuste_anual = 0
porcentaje_aumento = 0

def calcular_interes_compuesto():
    #datos a solicitar
    while True:
        tna = float(input("Ingresa el TNA: "))
        if tna <= 0:
            print("El TNA no puede ser menor que cero")
        else:
            break
    while True:
        aporte_mensual = float(input("Ingresa el Aporte Mensual: "))
        if aporte_mensual <= 0:
            print("El Aporte Mensual no puede ser menor que cero")
        else:
            break
    while True:
        anos = float(input("Ingresa los años: "))
        if anos <= 0:
            print("Los años no pueden ser menores que cero")
        else:
            break
    #preguntar si los aportes aumentaran por año
    while True:
        ajuste_anual = input("Quieres que el aporte mensual aumente cada año?(s/n): ").strip().lower()
        if ajuste_anual == 's':
            porcentaje_aumento = float(input("Ingrese el porcentaje de aumento anual(%): ")) / 100
            break
        elif ajuste_anual == 'n':
            porcentaje_aumento = 0
            break
        else:
            print("Entrada no valida. Por favor ingresa 's' o 'n'.")

calcular_interes_compuesto()

print(tna)
print(aporte_mensual)
print(anos)
print(ajuste_anual)
print(porcentaje_aumento)