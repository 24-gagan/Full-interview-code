import random


def number_guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the number guessing game")
    print("I am thinking of a number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter your guess"))
            attempts += 1
            if guess < number:
                print("Your guess is too low")
            elif guess > number:
                print("Your guess is too high")
            else:
                print("Congrats your guess is correct")
                print(f"You guessed the number in {attempts} attempts")
        except ValueError:
            print("Enter a valid number")


if __name__ == "__main__":
    number_guessing_game()
