"""
Exercise 2 — FizzBuzz (solution).

Run:
    python fizzbuzz_solution.py
"""

N = 20

for n in range(1, N + 1):              # 1..N inclusive (note the + 1)
    # ORDER MATTERS: test "both" first. If you checked % 3 first, every
    # multiple of 15 would print "Fizz" and never reach "FizzBuzz".
    if n % 15 == 0:                    # divisible by 3 AND 5
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# --- Alternative "build the string" style (no ordering trap at all) ---
print("\nSame thing, built by concatenation:")
for n in range(1, N + 1):
    out = ""
    if n % 3 == 0:
        out += "Fizz"
    if n % 5 == 0:
        out += "Buzz"
    print(out or n)                    # `out or n`: if out is "" (falsy), print n
