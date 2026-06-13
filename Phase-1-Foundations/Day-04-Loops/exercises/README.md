# Day 04 — Exercises

Put today's tools to work: `while`, `for`, `range`, `break`/`continue`, nested loops, and the loop
patterns. Try each in the stub file first, then check the matching `*_solution.py`.

---

## Exercise 1 — Number Guessing Game 🎯
The computer picks a secret number 1–100; the player guesses until they get it.

**Your task:** in `guessing_game.py`
1. `import random` and pick `secret = random.randint(1, 100)`.
2. Loop with `while True:` — ask for a guess each round and `int()`-cast it.
3. Tell them `"Too high"` / `"Too low"` / `"Correct!"` using `if/elif/else`.
4. `break` when they're right; count attempts and print them at the end.

*Skills:* `while True`, `break`, `random.randint`, comparisons, an accumulator (attempt counter).
*Focus:* the `while True` + `break` idiom — loop until the win condition, then leave.

➡ Solution: [`guessing_game_solution.py`](guessing_game_solution.py)

---

## Exercise 2 — FizzBuzz 🍷
The famous interview screen. Print numbers `1..N`, but:
- multiples of **3** → `"Fizz"`
- multiples of **5** → `"Buzz"`
- multiples of **both 3 and 5** → `"FizzBuzz"`

**Your task:** in `fizzbuzz.py`
1. `for n in range(1, N + 1):` (remember: stop is exclusive!).
2. Check **`n % 15 == 0` FIRST** (or build the string) — order matters, this is the classic trap.
3. Otherwise `% 3`, then `% 5`, else the number itself.

*Skills:* `for`, `range`, the modulo operator `%`, `if/elif/else` **ordering**.
*Focus:* why you must test "divisible by both" before the individual cases.

➡ Solution: [`fizzbuzz_solution.py`](fizzbuzz_solution.py)

---

## Exercise 3 — Multiplication Table 🔢
Print a clean, aligned multiplication grid up to `N × N` using **nested loops**.

**Your task:** in `multiplication_table.py`
1. Outer `for` over rows `1..N`, inner `for` over columns `1..N`.
2. Build each row (inner loop), then `print()` it — newline **after** the inner loop.
3. Align columns with an f-string width like `f"{value:>4}"` so it lines up.

*Skills:* nested `for` loops, `range`, f-string alignment, "build a row" pattern.
*Focus:* row/column flow — where the per-row `print()` goes, and why alignment needs a fixed width.

➡ Solution: [`multiplication_table_solution.py`](multiplication_table_solution.py)

---

### Stretch goals (if you finish early)
- **Guessing game:** cap it at 7 guesses (`break` + a "you lose, it was N" message via `for/else`).
- **FizzBuzz:** make 3/5/the words configurable at the top; print to one line separated by spaces.
- **Times table:** add a header row/column of labels and a divider line (see Module 05's grid).
