#entrada de un valor y calculara si es multiplo de 3 o de 5


print("Bienvenido a la calculadora de multiplos!")
numero = float(input("Ingresa un numero por favor: "))

es_multiplo_5 = numero % 5
es_multiplo_3 = numero % 3

if es_multiplo_5 == 0:
    print("El número es multiplo de 5.")
else:
    print("El número no es multiplo de 5.")

if es_multiplo_3 == 0:
    print("El número es multiplo de 3.")
else:
    print("El número no es multiplo de 3.")