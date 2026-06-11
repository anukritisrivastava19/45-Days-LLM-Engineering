# 08 — Method Chaining (+ `split` / `join`)

Because each string method **returns a new string**, you can immediately call another method on
that result — back to back. This is **method chaining**, read left to right.

```python
"  Riya Sharma  ".strip().upper()
#  └ "Riya Sharma"  └ "RIYA SHARMA"
```

Each `.method()` hands its result to the next:

| Step | Value |
|------|-------|
| `"  Riya Sharma  "` | `'  Riya Sharma  '` |
| `.strip()` | `'Riya Sharma'` |
| `.upper()` | `'RIYA SHARMA'` |
| `.replace(" ", "_")` | `'RIYA_SHARMA'` |

Chaining keeps cleaning code short and readable — very common when tidying messy text (like the
kind you get back from files or the web).

## A taster: `split()` and `join()`
Two methods you'll use a lot (full treatment comes with lists on Day 6):

| Method | Does | Example | Result |
|--------|------|---------|--------|
| `.split(sep)` | string → list of pieces | `"a,b,c".split(",")` | `['a', 'b', 'c']` |
| `sep.join(list)` | list of pieces → string | `"-".join(["a","b","c"])` | `'a-b-c'` |

`split` and `join` are opposites — break apart, then put back together.

Run the examples:

```bash
python method_chaining.py
```

➡ Next: practice in [exercises/](../exercises/)
