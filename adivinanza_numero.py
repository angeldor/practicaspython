#adivinanza
import random
numero = random.randint(1, 100)
print("Adivina el numero entre 1 y 100")
while True:
    intento = int(input("Ingrese un numero: "))
    if intento == numero:
        print("Adivinaste!")
        break
    elif intento < numero:
        print("Prueba con un numero mayor")
    else:
        print("Prueba con un numero menor")

# The code above is a simple number guessing game. The computer generates a random number between 1 and 100, and the user has to guess it. The user can keep guessing until they get it right. The game will give hints if the guess is too high or too low. The game will end when the user guesses the correct number.
# The game uses a while loop to keep the game running until the user guesses the correct number. Inside the loop, the user is prompted to enter a number, and the program checks if the number is equal to the random number. If the number is correct, the game ends. If the number is too high or too low, the game gives a hint and continues.
# The random number is generated using the randint function from the random module. The randint function takes two arguments, the start and end of the range, and returns a random integer within that range.

# The code above is a simple number guessing game. The computer generates a random number between 1 and 100, and the user has to guess it. The user can keep guessing until they get it right. The game will give hints if the guess is too high or too low. The game will end when the user guesses the correct number.
# The game uses a while loop to keep the game running until the user guesses the correct number. Inside the loop, the user is prompted to enter a number, and the program checks if the number is equal to the random number. If the number is correct, the game ends. If the number is too high or too low, the game gives a hint and continues.