import random

def guessing_game():
    print("=== Number Guessing Game ===")
    
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number (1-100): "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You guessed in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()
