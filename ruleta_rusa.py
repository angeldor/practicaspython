#ruleta rusa de adivinanzas con 6 balas
import os
import random
numero = random.randint(1, 6)
print("Adivina el numero entre 1 y 6")

while True:
    intento = int(input("Ingrese un numero: "))
    if intento == numero:
        print("Adivinaste!")
        break
    elif intento < numero:
        print("Prueba con un numero mayor")
    else:
        print("Prueba con un numero menor")
    os.remove("vida.txt")
    os.system("cls")
    print("Has muerto")
    break