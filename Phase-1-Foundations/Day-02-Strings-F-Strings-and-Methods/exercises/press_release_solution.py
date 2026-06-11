"""
Exercise 3 — Press Release clean-up (solution).

Run:
    python press_release_solution.py
"""

raw = "   softpro school of ai LAUNCHES new 45-day ai program!!!   "

# One chained expression, read left to right:
#   strip the spaces -> drop the !!! -> Title Case every word
clean = raw.strip().replace("!!!", "").title()

print("BEFORE:", repr(raw))     # repr() shows the quotes + spaces clearly
print("AFTER :", clean)         # Softpro School Of Ai Launches New 45-Day Ai Program

# Bonus: how much shorter is it now?
print("Removed", len(raw) - len(clean), "characters")
