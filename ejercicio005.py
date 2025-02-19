import math

area_circulo = 0
pi = math.pi

def hallar_area(radio):
    radio = float(input("Ingrese el radio del circulo: "))
    area_circulo = pi * radio ** 2
    print("El area del circulo es: ", area_circulo)

hallar_area(area_circulo)