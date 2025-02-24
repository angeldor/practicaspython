print("Bienvenido a la Tierra Media")
nombre= input("¿Cuál es tu nombre, viajero?")

print(f"¡Bienvenido, {nombre}! ¿Estás listo para comenzar tu aventura?")
print("¡Comencemos!")
print("Elige tu personaje:")
print("1. Humano")
print("2. Elfo")
print("3. Enano")
print("4. Hobbit")
print("5. Mago")
print("6. Orco")
print("7. Troll")

def get_number():
    # This function will keep asking the user to enter a number until a valid number is entered.
    while True:
        try:
            # Attempt to convert the user input to an integer.
            number = float(input("Por favor, elige tu personaje: "))
            return number  # If successful, return the number.
        except ValueError:
            # If a ValueError occurs (i.e., the input is not a valid integer), print an error message.
            print("Esa no es una opción válida. Por favor, intenta de nuevo.")