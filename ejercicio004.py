conteo = 1
num_divisibles = []

while conteo <= 50:
    print(f"Tenemos el numero {conteo} y vamos a ver si es divisible por 7.")
    es_divisible = conteo % 7
    if es_divisible == 0:
        print(f"El numero {conteo} es divisible por 7.")
        num_divisibles.append(conteo)
    else:
        print(f"El numero {conteo} NO es divisible por 7.")
    conteo += 1

print(f"Los numeros divisibles por 7 son: {num_divisibles}")