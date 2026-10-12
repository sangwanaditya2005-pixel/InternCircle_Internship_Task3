
import random
import re
from collections import Counter


def number_guessing_game():
    print("\n=== Number Guessing Game ===")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))

            if guess < 1 or guess > 100:
                print("Enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                score = max(100 - (attempts - 1) * 10, 10)
                print("Correct! You guessed it in", attempts, "attempts.")
                print("Your score:", score)
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def word_counter():
    print("\n=== File-Based Word Counter ===")
    filename = input("Enter text file name (e.g., sample.txt): ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = re.findall(r"\b[\w']+\b", text.lower())
        frequency = Counter(words)

        print("Total words:", len(words))
        print("\nWord frequency:")

        for word, count in frequency.most_common():
            print(word, ":", count)

    except FileNotFoundError:
        print("File not found. Make sure the file exists in this folder.")
    except OSError:
        print("Unable to read the file.")


while True:
    print("\n=== InternCircle Task 3 ===")
    print("1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number_guessing_game()
    elif choice == "2":
        word_counter()
    elif choice == "3":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice. Try again.")
