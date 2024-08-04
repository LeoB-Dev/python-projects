import random
try:
    random_number = random.randint(1, 10)       
    print(f"Guess the number between 1 and 10! \n\nEnter a whole number:", end="")

    while True:
        user_number = int(input())
        if user_number > 0 and user_number <= 10:
            if user_number == random_number:
                print(f"You guessed right! The number was {random_number}.")
                break
            else: 
                print(f"\nYou guessed wrong! Try again.\n\nEnter a whole number:", end="")
        else: 
            print("Invalid input. Try again.\n\nEnter a whole number:", end="")
except ValueError: 
    print("Invalid input. Try again.\n\nEnter a whole number:", end="")
except KeyboardInterrupt:
    print("\n\nProgram terminated by the user.")


# Problem with this code is that when I enter a character instead of an integer
# the program ends says "Enter a whole number:%", instead of the expected 
# "Enter a whole number: