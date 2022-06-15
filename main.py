import random

number = random.randint(1,100)

guess = int(input("Guess the number : "))

attempt = 1

while (True):
    if(guess>number):
        guess = int(input("Guess another number.This one is big : "))
        attempt += 1

    elif(guess<number):
        guess = int(input("Guess another number.This is one less : "))
        attempt += 1

    else:
        print(f"Yeah thats the number!! You guessed it right in {attempt} attempts")
        break