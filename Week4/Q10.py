import random

# Generate a random number between 1 and 20
Hidden = random.randint(1,20)


for guess_count in range(1,6):
    try:
        guess = int(input("Guess a number between 1 to 20: "))
        
        if guess < Hidden :
            print("The correct number is higher.")
        elif guess > Hidden:
            print("The correct number is lower.")
        else:
            print(f"Congratulations! You guessed the correct number ({Hidden}) in {guess_count} guesses.")
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")
else:
    print(f"Sorry, you've run out of guesses. The hidden number was {Hidden}.")
