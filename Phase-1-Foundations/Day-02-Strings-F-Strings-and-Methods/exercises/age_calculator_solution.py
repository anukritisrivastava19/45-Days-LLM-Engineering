"""
Exercise 1 — Age Calculator (solution).

Run (it will ask you for input):
    python age_calculator_solution.py
"""

CURRENT_YEAR = 2026

# input() always returns a string...
name = input("What's your name? ")

# ...so cast the year to an int before doing maths
birth_year = int(input("What year were you born? "))

age = CURRENT_YEAR - birth_year

# An f-string drops the variables straight into the message
print(f"Hi {name}, you turn {age} in {CURRENT_YEAR}!")
