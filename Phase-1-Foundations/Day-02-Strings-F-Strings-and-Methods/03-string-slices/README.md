# 03 — String Slices

Indexing grabs **one** character. **Slicing** grabs a *range* of characters using
`string[start:stop:step]`.

The rule that trips everyone up at first: **`start` is included, `stop` is NOT.**

```
 P  y  t  h  o  n
 0  1  2  3  4  5
```

| Code | Means | Result |
|------|-------|--------|
| `"Python"[0:3]` | index 0,1,2 (stop 3 excluded) | `'Pyt'` |
| `"Python"[2:5]` | index 2,3,4 | `'tho'` |
| `"Python"[:3]` | from the start to 3 | `'Pyt'` |
| `"Python"[3:]` | from 3 to the end | `'hon'` |
| `"Python"[:]` | the whole string (a copy) | `'Python'` |
| `"Python"[-3:]` | last 3 characters | `'hon'` |

## The third number: step
`[start:stop:step]` — `step` says "how many to jump."

| Code | Result | Why |
|------|--------|-----|
| `"Python"[::2]` | `'Pto'` | every 2nd character |
| `"Python"[::-1]` | `'nohtyP'` | **step -1 reverses the string** ✨ |

`[::-1]` is the classic Python one-liner to reverse text — remember it.

Run the examples:

```bash
python string_slices.py
```

➡ Next: [04-escape-and-triple-quotes](../04-escape-and-triple-quotes/)
