# 02 — String Indexing

A string is an ordered sequence of characters, and **each character has a position (index)**.
Indexing starts at **0**, not 1.

```
 H   e   l   l   o
 0   1   2   3   4      ← positive index (from the start)
-5  -4  -3  -2  -1      ← negative index (from the end)
```

Use square brackets `[]` to grab one character:

| Code | Result |
|------|--------|
| `"Hello"[0]` | `'H'` (first character) |
| `"Hello"[4]` | `'o'` (fifth character) |
| `"Hello"[-1]` | `'o'` (last character) |
| `"Hello"[-2]` | `'l'` (second from the end) |
| `"Hello"[10]` | ❌ `IndexError` (out of range) |

## Two things to remember
- **Negative indexing counts from the end** — `[-1]` is always the last character. Super handy.
- **Strings are immutable** — you can *read* a character but you can't *change* one in place.
  `name[0] = "J"` is an error. To "change" a string you build a new one (you'll see how with
  slicing and methods).

## The special value `None`
`None` is Python's way of saying "nothing here / no value." It is **not** the string `"None"` and
**not** `0`. You'll meet it again when a function returns nothing.

```python
result = None        # a deliberate "empty" placeholder
print(result)        # None
```

Run the examples:

```bash
python string_indexing.py
```

➡ Next: [03-string-slices](../03-string-slices/)
