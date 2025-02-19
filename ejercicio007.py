def get_number():
    # This function will keep asking the user to enter a number until a valid number is entered.
    while True:
        try:
            # Attempt to convert the user input to an integer.
            number = float(input("Please enter a number: "))
            return number  # If successful, return the number.
        except ValueError:
            # If a ValueError occurs (i.e., the input is not a valid integer), print an error message.
            print("That's not a valid number. Please try again.")

if __name__ == "__main__":
    # If this script is run directly, call the get_number function and print the result.
    number = get_number()
    print(f"You entered the number: {number}")