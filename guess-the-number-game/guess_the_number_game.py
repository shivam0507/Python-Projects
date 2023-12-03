# Python code to guess the number based on the user given range in minimum number of tries
import math
import random


def start():
    print("Welcome to the game of Guessing!\n"
          "Please select the range")
    _start = int(input("Enter start number: "))
    _end = int(input("Enter end number: "))
    attempts = int(math.log2(_end - _start + 1))
    print(f"You will get {attempts} attempts to guess the correct number")
    target = random.randrange(_start, _end+1)
    while attempts > 0:
        _guess = int(input("Guess the number: "))
        if _guess == target:
            print("Wooohhh!! you guess the number correct!!!")
            break
        elif _guess > target:
            print("Try Again! You guessed too large")
        else:
            print("Try Again! You guessed too small")
        attempts -= 1

    if attempts == 0:
        print("You lose. Better luck next time!!")


if __name__ == "__main__":
    while True:
        start()
        play_again = input("Wanted to play again[Y/N]")
        if play_again not in ["Y", "N"]:
            play_again = input("Invalid input. Please provide input in [Y/N]: ")

        if play_again == "N":
            break
