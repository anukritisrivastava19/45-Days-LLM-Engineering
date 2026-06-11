# 01 — Strings: Creating & Combining Text

A **string** is text — a sequence of characters. You write it inside quotes.

| You write | Python sees |
|-----------|-------------|
| `'hello'` | the text `hello` |
| `"hello"` | the text `hello` (same thing) |
| `"it's fine"` | use double quotes when the text has a `'` inside |
| `'She said "hi"'` | use single quotes when the text has a `"` inside |

Single and double quotes are **identical** in Python — pick whichever avoids clashing with quotes
*inside* your text.

## String operators
Two operators work on strings:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | concatenation (join) | `"AI" + "Engineer"` | `"AIEngineer"` |
| `*` | repetition | `"ha" * 3` | `"hahaha"` |

> ⚠️ `+` only joins **string + string**. `"Age: " + 25` is an error — you must convert the number
> first: `"Age: " + str(25)`. (More on that in Module 05, and f-strings in Module 06 make this easy.)

Run the examples:

```bash
python strings.py
```

➡ Next: [02-string-indexing](../02-string-indexing/)
