# Day 04 — Loops

Day 3 taught your program to **decide** (`if`). Today it learns to **repeat** — to do the same work
over a list of customers, every line in a file, every retry of a flaky network call, or every token
streaming back from an AI model. Loops are the single most-used control structure in real code: a web
server loops over requests, a data pipeline loops over rows, an agent loops "think → act → observe"
until the task is done.

We build from the two loop keywords (`while`, `for`) up to the patterns you'll actually reach for at
work: accumulators, counters, search-with-flag, retry-with-backoff, and building reports with nested
loops.

> 🐙 **GitHub mini-track starts today (Part 1 of 3).** A beginner-friendly visual deck —
> *Why GitHub? (the time machine for your code)* — lives in [`github-basics/`](github-basics/).
> Open `github-basics/index.html` in any browser. Continues Day 5 (the everyday workflow) and Day 6
> (branching & pull requests).

## Learning objectives
By the end of today you can:
- Write a **`while` loop** for "repeat until a condition changes" and **avoid infinite loops**
- Write a **`for` loop** to iterate over strings, lists, and ranges — the everyday workhorse
- Use **`range(start, stop, step)`** correctly (stop is *exclusive*) for counting and countdowns
- Control flow inside loops with **`break`** (quit early) and **`continue`** (skip this one)
- Combine `for`/`while` with **`else`** (the loop-`else` most beginners never learn) and use **`enumerate`**
- Write **nested loops** for grids, tables, and "every pair" problems — and know their cost
- Recognise the **real-world loop patterns**: accumulate a total, count matches, find-then-stop,
  build a new collection, and retry-until-success

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [while-loops](01-while-loops/) | `while`, the loop variable, infinite loops & how to avoid them, `break` as the exit |
| 02 | [for-loops](02-for-loops/) | Iterating strings/lists, the loop variable, `enumerate`, `for` vs `while` |
| 03 | [range](03-range/) | `range(stop)`, `range(start, stop)`, `range(start, stop, step)`, countdowns |
| 04 | [break-and-continue](04-break-and-continue/) | `break` (quit), `continue` (skip), loop-`else`, validation/retry loops |
| 05 | [nested-loops](05-nested-loops/) | Loop inside a loop: grids, tables, pairs; reading the row/column flow |
| 06 | [loop-patterns](06-loop-patterns/) | The 5 patterns you reuse forever: accumulate, count, search-flag, build, retry |

Then test yourself in **[exercises/](exercises/)**.

## The 5 things to really nail today
1. **`while` = "repeat *until*", `for` = "repeat *for each*".** Reach for `for` when you know the
   collection; reach for `while` when you're waiting on a condition (user input, retries, a game).
2. **Always change the loop variable** inside a `while` — forgetting `i += 1` is the #1 infinite loop.
3. **`range(5)` is `0,1,2,3,4`** — the stop value is *not* included. This off-by-one bites everyone once.
4. **`break` quits the whole loop; `continue` skips to the next round.** Don't confuse them.
5. **Nested loops multiply:** an outer loop of 1,000 with an inner loop of 1,000 runs **1,000,000**
   times. Cheap to write, expensive to run — notice when you're doing it.

## How to run
From this folder, run any file directly:

```bash
python 01-while-loops/while_loops.py
```

A few files use `input()` (Module 01's countdown, Module 04's PIN demo, and the exercises) — they'll
**pause and wait** for you to type and press Enter. That's expected. To stop a runaway loop, press
**Ctrl + C**.

Or open the REPL and experiment:

```bash
python
>>> for ch in "AI":
...     print(ch)
A
I
```

## Today's exercises
Three of them — see [`exercises/`](exercises/):
1. **Number Guessing Game** — `while` + `random` + `break` + comparisons (the classic first loop game)
2. **FizzBuzz** — `for` + `range` + `%` + `if/elif/else` (the famous screening question)
3. **Multiplication Table** — **nested** `for` loops building a clean grid with f-string alignment

➡ Next: **[Day 05 — Functions & Scope](../Day-05-Functions-and-Scope/)**
