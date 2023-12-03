import random
# this library use to pick any random item from given list

name = input("What is your name? ")

print("Good Luck! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the characters")

guesses = ''

turns = 12

# continue till player exhaust all it's turn
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print(f"You have {turns}, more guesses")

        if turns == 0:
            print("You Lose")


