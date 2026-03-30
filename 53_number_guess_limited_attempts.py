import random

number = random.randint(1, 50)
attempts = 5

while attempts > 0:
    guess = int(input("Guess the number: "))

    if guess == number:
        print("You guessed it!")
        break
    else:
        attempts -= 1
        print("Wrong guess. Attempts left:", attempts)

if attempts == 0:
    print("Game Over! Number was:", number)