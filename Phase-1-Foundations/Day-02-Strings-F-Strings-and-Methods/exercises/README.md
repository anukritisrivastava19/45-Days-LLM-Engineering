# Day 02 — Exercises

Practice everything from today: indexing/slicing, `input()`, type casting, f-strings, and string
methods. Try each one yourself in the stub file first, then check the matching `*_solution.py`.

---

## Exercise 1 — Age Calculator 🎂
Ask the user for their **name** and **birth year**, then tell them how old they'll turn this year.

**Your task:** in `age_calculator.py`
1. `input()` their name and birth year (remember: input is a **string**).
2. Cast the year with `int()` and compute `age = 2026 - birth_year`.
3. Print a friendly message using an **f-string**, e.g.
   `Hi Riya, you turn 25 in 2026!`

*Skills:* `input()`, `int()`, f-strings.

➡ Solution: [`age_calculator_solution.py`](age_calculator_solution.py)

---

## Exercise 2 — Shopping Cart 🛒
Build a tiny receipt for an online order (₹ amounts), formatted neatly.

**Your task:** in `shopping_cart.py`, with these values already given:
- `item = "Wireless Mouse"`, `price = 799.0`, `quantity = 3`, `gst_rate = 0.18`

Compute `subtotal`, `gst` (subtotal × rate), and `total`, then print a receipt where **every amount
shows 2 decimals and a thousands separator**, e.g. `Rs 2,397.00`. Use f-string formatting (`:,.2f`).
(Print `Rs`, not `₹` — the default Windows console can't display the rupee symbol.)

*Skills:* f-strings, `:,.2f` and `:.0%` formatting.

➡ Solution: [`shopping_cart_solution.py`](shopping_cart_solution.py)

---

## Exercise 3 — Press Release 📰
A junior intern pasted a messy headline. Clean it up with string methods.

**Your task:** in `press_release.py`, starting from
`raw = "   softpro school of ai LAUNCHES new 45-day ai program!!!   "`
produce a tidy headline:
1. `.strip()` the surrounding spaces
2. `.replace("!!!", "")` to drop the extra punctuation
3. `.title()` to capitalise each word
4. Do it as **one chained expression**, then print the before and after.

*Bonus:* print how many characters were removed (`len(raw)` vs `len(clean)`).

*Skills:* `.strip()`, `.replace()`, `.title()`, method chaining, `len()`.

➡ Solution: [`press_release_solution.py`](press_release_solution.py)
