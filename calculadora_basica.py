# calculadora basica

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: division por cero"
    return a / b

def menu():
    print("Calculadora basica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    
def main():
    while True:
        menu()
        opcion = input("Ingrese una opcion: ")
        if opcion == "5":
            break
        if opcion in ["1", "2", "3", "4"]:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            if opcion == "1":
                print("Resultado: ", suma(a, b))
            elif opcion == "2":
                print("Resultado: ", resta(a, b))
            elif opcion == "3":
                print("Resultado: ", multiplicacion(a, b))
            elif opcion == "4":
                print("Resultado: ", division(a, b))
        else:
            print("Opcion invalida")
        
        
if __name__ == "__main__":
    main()