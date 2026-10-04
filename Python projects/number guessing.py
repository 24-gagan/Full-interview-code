import random
def number_guessing_game():
    print("Welcome to the number guessing game")
    print("I am thinking of a number between 1 and 100")
    print("You are having 7 attempts")
    secret=random.randint(1,100)
    attempts=1

    for attempt in range(1,attempts+1):
        try:
            guess=int(input("Guess a number between 1 and 100"))
            if guess<1 or guess>100:
                print("please guess a number between 1 and 100")
            if guess==secret:
                print("Congractulations you guessed the right number")
            elif guess<secret:
                print("Too Low")
            else:
                print("Too high")
        except ValueError:
            print("Invalid input")
    else:
        print("Beterr luck next time")
number_guessing_game()
