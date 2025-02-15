import sys
import random

# Assignment 5 - Cristobal Lara
a = sys.argv[1]
b = sys.argv[2]

pair = "odd"

if ((int(a) % 2) == 0):
    pair = "even"

binary_form = ' '.join(format(ord(x), '08b') for x in b)

def count_vowels(word):
    return sum(1 for letter in word.lower() if letter in "aeiou")

num_vowels = count_vowels(b)

print("<h2>Number Puzzle:</h2>")
print("<ul>")
print(f"<li>The number {a} is {pair}. Its cube is {int(a)**3}.</li>")
print("</ul>")
print("<br>")

print("<h2>Text Puzzle:</h2>")
print("<ul>")
print(f"<li>Binary: {binary_form}.</li>")
print(f"<li>Vowel Count: {num_vowels}.</li>")
print("</ul>")
print("<br>")

def generate_secret_number():
    return random.randint(1, 100)

def get_feedback(guess, secret):
    if guess > secret:
        return "Too high!"
    elif guess < secret:
        return "Too low!"
    else:
        return "Correct!"

def treasure_hunt():
    secret_number = generate_secret_number()
    attempts = 1
    founded = False
    print("<h2>Treasure Hunt:</h2>")
    print("<ul>")
    print(f"<li>The secret number is {secret_number}.</li>")
    
    while attempts<5:
        try:
            guess = random.randint(1, 100)
            feedback = get_feedback(guess, secret_number)
            print(f"<li>Attempt {attempts}: {guess} ({feedback})</li>")
            attempts += 1
            if guess == secret_number:
                print(f"<li>You found the treasure in {attempts} attempts!</li>")
                founded = True
                break
        except ValueError:
            print("<li>Please enter a valid number!</li>")
    if founded == False:
        guess = secret_number
        feedback = get_feedback(guess, secret_number)
        print(f"<li>Attempt {attempts}: {guess} ({feedback})</li>")
        print(f"<li>You found the treasure in {attempts} attempts!</li>")
    print("</ul>")

# Start the game
treasure_hunt()