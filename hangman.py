#hangman game

import random

words = ["move", "sign", "copy", "hunt", "ping"]

word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("====Welcome to Hangman!====")
print("->Guess the word one letter at a time.")
print(" ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

    print(" ".join(guessed_word))

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
    print("Thank you for playing Hangman!")
    