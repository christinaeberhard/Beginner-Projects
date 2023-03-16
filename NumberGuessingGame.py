import random

print("Welcome to the Number Guessing Game, let's start!")
level = input("Choose your difficulty level, type either 'easy' for 10 tries or 'hard' for 5 tries: ")
if level == "easy":
    left_tries = 10
elif level == "hard":
    left_tries = 5

answer = random.randint(0, 101)
should_continue = True

while should_continue:
    guess = int(input("Guess the number between 0 and 100: "))
    if guess > answer:
        left_tries -= 1
        print(f"Too high! Your remaining tries: {left_tries}")
    elif guess < answer:
        left_tries -= 1
        print(f"Too low! Your remaining tries: {left_tries}")
    elif guess == answer:
        should_continue = False
        print(f"The correct answer is {answer}, you won!")