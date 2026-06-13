# 05 — Nested Loops

A **nested loop** is a loop inside another loop. For every single pass of the *outer* loop, the
*inner* loop runs all the way through.

```python
for row in range(3):          # outer: runs 3 times
    for col in range(4):      # inner: runs 4 times PER outer pass
        print(row, col)       # => 3 x 4 = 12 lines total
```

Think of a clock: the hour hand (outer) moves once; the minute hand (inner) sweeps a full circle for
each hour. Or a spreadsheet: for each **row**, walk every **column**.

## Where you actually use them
- **Grids & tables** — multiplication tables, calendars, game boards, pixel images.
- **Every combination** — pair every product with every size; every team vs every other team.
- **Nested data** — a list of orders, each order a list of items (Day 6 makes this common).

## ⚠️ They multiply — watch the cost
Outer `n` × inner `m` = `n × m` runs. `1000 × 1000` is a **million** iterations. Easy to type,
sometimes slow to run. Not a reason to fear them — just notice when the numbers get big.

## `break`/`continue` hit only the inner loop
A `break` inside the inner loop exits **that** inner loop, not the outer one. To bail out of both,
break the inner loop and check a flag (or refactor into a function and `return` — Day 5).

## 🎤 Talking points (what to say & focus on)
- **"For each row, for each column."** Say it out loud while pointing — outer = rows, inner =
  columns. The multiplication grid makes this concrete and memorable.
- **Trace the first few passes by hand.** `(0,0) (0,1) (0,2) (1,0)…` — watching the inner counter
  reset each outer pass is the "aha." Do it live; don't just run the file.
- **Where the `print()` goes matters.** A bare `print()` *after* the inner loop (still inside the
  outer) is what creates the line break between rows. Show the grid with and without it.
- **Multiplication = cost.** Drop the "n×m runs" line and a real number (a million). Plants the seed
  for "is there a cheaper way?" without derailing into Big-O on Day 4.
- **`break` is inner-only.** Demo it, then mention the two real fixes: a flag, or (better) wrap it in
  a function and `return` — a nice forward-hook to Day 5.

## ⚠️ Common mistakes to call out
- Reusing the **same loop variable** name for inner and outer (`for i … for i …`) → the inner clobbers
  the outer. Use distinct names (`row`/`col`, `i`/`j`).
- Expecting one `break` to escape both loops.
- Putting the per-row `print()` in the wrong place (inside vs after the inner loop).
- Accidental nesting that explodes the iteration count on big inputs.

Run the examples:

```bash
python nested_loops.py
```

➡ Next: **[06-loop-patterns](../06-loop-patterns/)**
