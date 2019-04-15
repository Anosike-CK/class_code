import random

my_number = random.randint(1,5)
guess = 0
noOfguesses = 0

while guess != my_number :

    guess = int(input("i have a number, can you guess it? "))

    noOfguesses += 1

    if noOfguesses == 3:

        print("you ran out of guesses")
        break

    if guess < my_number:

        print("you guessed number is below my number!")

    elif guess > my_number:

        print("you guessed number is above my number!")

    elif guess == my_number:

        print("you guessed right!")
    else:
        print("Your guess should be between 0 and 5")




    


