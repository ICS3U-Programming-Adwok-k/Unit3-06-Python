#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: March 28th, 2025
# The program asks the user

import random


def main():

    correct_number = random.randint(0, 9)

    user_guess_as_string = input("Guess a number between 0 and 8: ")

    try:
        user_guess = int(user_guess_as_string)
        if user_guess == correct_number:
            print("You guessed the correct number.")

    except ValueError:
        print("You entered a number that is not an integer.")

    else:
        print("You guessed the wrong number\n")
        print("The correct number is {}\n".format(correct_number))

    finally:
        print("Thank you gor playing.")


if __name__ == "__main__":
    main()
