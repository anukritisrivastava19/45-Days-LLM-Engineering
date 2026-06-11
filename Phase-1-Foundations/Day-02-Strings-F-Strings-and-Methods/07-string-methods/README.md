# 07 — String Methods

A **method** is a function that "belongs to" a value — you call it with a dot:
`value.method()`. Strings come with dozens of handy methods for cleaning and transforming text.

> 🔑 **Strings are immutable**, so a string method **never changes the original** — it *returns a
> new string*. You must capture the result: `cleaned = text.strip()`.

## The everyday methods

| Method | What it does | Example | Result |
|--------|--------------|---------|--------|
| `.upper()` | ALL CAPS | `"hi".upper()` | `'HI'` |
| `.lower()` | all lowercase | `"HI".lower()` | `'hi'` |
| `.title()` | Capitalise Each Word | `"riya sharma".title()` | `'Riya Sharma'` |
| `.strip()` | remove leading/trailing spaces | `"  hi  ".strip()` | `'hi'` |
| `.replace(a, b)` | swap text | `"2024".replace("2024","2025")` | `'2025'` |
| `.find(x)` | index of first match (`-1` if none) | `"hello".find("l")` | `2` |
| `.count(x)` | how many times | `"hello".count("l")` | `2` |
| `.startswith(x)` | True/False | `"hello".startswith("he")` | `True` |

## How to discover methods yourself
You don't memorise these — you look them up. Two ways from the REPL:

```python
>>> help(str.strip)      # shows what strip does and how to call it
>>> "hello".upper       # tab-complete in many editors lists all methods
```

`help()` and the official docs at <https://docs.python.org/3/library/stdtypes.html#string-methods>
are your friends. Learning to *read the docs* matters more than memorising.

Run the examples:

```bash
python string_methods.py
```

➡ Next: [08-method-chaining](../08-method-chaining/)
