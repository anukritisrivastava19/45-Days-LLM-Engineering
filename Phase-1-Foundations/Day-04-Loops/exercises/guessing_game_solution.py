"""
Exercise 1 — Number Guessing Game (solution).

Run (asks for input):
    python guessing_game_solution.py
"""

import random

secret = random.randint(1, 100)    # 1..100 inclusive
attempts = 0

print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:                                  # loop until the player wins
    raw = input("Your guess: ").strip()
    if not raw.isdigit():                    # be kind about bad input
        print("  Please type a whole number.")
        continue                             # skip the rest, ask again
    guess = int(raw)
    attempts += 1                            # accumulator: count the tries

    if guess < secret:
        print("  Too low!")
    elif guess > secret:
        print("  Too high!")
    else:
        print(f"  Correct! You got it in {attempts} attempt(s).")
        break                                # win condition -> leave the loop
