import random
num=random.randint(1,100)
guess=0
print("Guess the number")
while guess!=num:
    guess=int(input("enter the number"))
    if guess>num:
        print("too high")
    elif guess<num:
        print("too low")
    else:
        print("You guessed right")