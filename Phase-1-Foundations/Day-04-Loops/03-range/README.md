# 03 — `range()`

`range()` generates a sequence of numbers to loop over — when you want to repeat something **N times**
or count through positions. It comes in three forms:

| Call | Produces | Notes |
|------|----------|-------|
| `range(stop)` | `0 … stop-1` | starts at 0, **stop is excluded** |
| `range(start, stop)` | `start … stop-1` | inclusive start, exclusive stop |
| `range(start, stop, step)` | every `step`-th number | `step` can be **negative** (countdown) |

```python
range(5)          # 0, 1, 2, 3, 4         (five numbers, NOT up to 5)
range(1, 6)       # 1, 2, 3, 4, 5
range(0, 10, 2)   # 0, 2, 4, 6, 8         (evens)
range(10, 0, -1)  # 10, 9, 8, ... 1       (countdown)
```

## ⚠️ The off-by-one: stop is EXCLUSIVE
`range(5)` gives **five** numbers but the last is **4**, not 5. To loop `1..N` inclusive, write
`range(1, N + 1)`. This trips up everyone exactly once — make it the once.

## Why is it lazy? (worth one sentence)
`range(1_000_000)` doesn't build a million-item list in memory — it generates numbers on demand. So
it's cheap even for huge counts. Wrap it in `list(range(...))` only when you actually want to *see* it.

## 🎤 Talking points (what to say & focus on)
- **`range(n)` = "do this n times."** That's the headline use. Most `range` loops don't even use the
  number — they just need *n* repetitions.
- **Hammer the exclusive stop.** Write `range(1, 6)` and ask "what's the last value?" The answer is 5,
  not 6. Then show `range(1, N+1)` as the inclusive-N idiom.
- **`step` is the third gear.** `range(0, 101, 10)` for 0,10,…,100; negative step for countdowns.
  This replaces fiddly `while` arithmetic.
- **Prefer iterating the collection directly.** `range(len(items))` is usually a smell — if you want
  the items, do `for item in items`; if you want index+item, use `enumerate`. Reserve `range` for
  "pure counting" (repeat N times, build a number table, step by k).
- **It's lazy/memory-cheap** — one line is enough; don't over-explain generators on Day 4.

## ⚠️ Common mistakes to call out
- Expecting `range(5)` to include 5.
- Using `range(len(my_list))` then `my_list[i]` when `for item in my_list` (or `enumerate`) is cleaner.
- Forgetting the sign of `step` in a countdown (`range(10, 0, -1)`, not `range(10, 0)`).

Run the examples:

```bash
python range_demo.py
```

➡ Next: **[04-break-and-continue](../04-break-and-continue/)**
