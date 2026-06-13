"""
Exercise 1 — Number Guessing Game (STUDENT STUB).

The computer picks a secret 1-100; keep asking until the player gets it,
then report how many attempts it took.

Run (asks for input):
    python guessing_game.py
"""

import random

secret = random.randint(1, 100)   # inclusive on BOTH ends: 1..100
attempts = 0

print("I'm thinking of a number between 1 and 100. Can you guess it?")

# TODO 1: loop forever with `while True:`
# TODO 2: each round -> input() a guess, int()-cast it, and do attempts += 1
# TODO 3: if guess < secret -> "Too low"; elif guess > secret -> "Too high"
# TODO 4: else -> print "Correct!" with the attempt count, then break
