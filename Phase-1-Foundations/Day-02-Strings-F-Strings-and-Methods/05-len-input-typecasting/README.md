# 05 — `len()`, `input()` & Type Casting

Three small but essential tools.

## `len()` — how long is it?
`len()` is a **built-in function** that gives the number of characters in a string.

```python
len("Python")      # 6
len("")            # 0  (an empty string)
```

## `input()` — read something the user types
`input()` pauses the program, waits for the user to type and press Enter, and hands you back what
they typed. **It always returns a string** — even if they type `25`.

```python
name = input("What's your name? ")   # the text before is the prompt shown to the user
```

> ▶️ A script with `input()` will **pause and wait** when you run it. Type your answer, press Enter.

## Type casting — converting between types
Because `input()` always gives a string, you must **convert** it before doing maths. Casting
functions:

| Function | Converts to | Example | Result |
|----------|-------------|---------|--------|
| `int()` | whole number | `int("25")` | `25` |
| `float()` | decimal number | `float("3.5")` | `3.5` |
| `str()` | string | `str(25)` | `"25"` |

```python
age_text = input("Age? ")     # "25"  (a string)
age = int(age_text)           # 25    (now a number)
next_year = age + 1           # 26
```

> ⚠️ `int("hello")` and `int("3.5")` raise a `ValueError` — you can only cast text that *looks*
> like that number. (`int("3.5")` fails because of the dot; use `float()` then `int()` if needed.)

Run the example (it will ask you for input):

```bash
python len_input_typecasting.py
```

➡ Next: [06-f-strings](../06-f-strings/)
