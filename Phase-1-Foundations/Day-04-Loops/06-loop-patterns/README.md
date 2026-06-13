# 06 — Loop Patterns ("loops in the wild")

You've met the loop *keywords*. This module is the payoff: the handful of **reusable shapes** that
cover ~90% of the loops you'll ever write at work. Learn to recognise them and most "how do I loop
this?" questions answer themselves.

| Pattern | Question it answers | Core move |
|---------|---------------------|-----------|
| **Accumulate** | "What's the total / sum / max?" | keep a running variable, update each pass |
| **Count** | "How many match?" | `count += 1` when a condition holds |
| **Search + flag** | "Is there any…? Which one?" | set a flag / `break` on first hit (or `for/else`) |
| **Build** | "Make a new collection from this one" | start empty, `.append()` each pass |
| **Retry** | "Keep trying until it works (or give up)" | `while` + attempt counter + `break` |

These map directly onto data work and AI engineering: accumulate token counts, count how many
documents matched a query, search for the first relevant chunk, build a list of cleaned records, retry
a flaky model call with backoff.

## The accumulator, in detail
```python
total = 0                  # 1) start at the identity (0 for +, 1 for *, "" for text)
for x in items:
    total += x             # 2) fold each item in
# 3) total now holds the answer
```
Sum, product, max/min, longest string, concatenated report — all the same skeleton with a different
update line.

## 🎤 Talking points (what to say & focus on)
- **Patterns > syntax.** By now they *can* write loops; today is about *naming the shape* so they
  reach for the right one instantly. Put the table on screen and keep referring to it.
- **Accumulator is the big one.** Sum, count, max, build — show they're the same skeleton: initialise
  → update each pass → use after. Change one line, get a different answer.
- **Initialise to the right "empty."** `0` for sums, `1` for products, `""` for string-building,
  `[]` for lists, `-infinity`/first-item for max. A wrong start value is a classic bug.
- **Count is accumulate-with-a-condition.** `if matches: n += 1`. Tie it to "how many emails are
  invalid," "how many tests passed."
- **Retry-with-backoff is the most AI-relevant pattern** — model APIs fail transiently. Walk the
  attempts/`sleep`/`break` shape; they'll reuse it verbatim in Phase 1's LLM calls.
- **Hook forward:** "build a new list" is exactly what a **list comprehension** compresses (Day 6),
  and `sum()`/`max()`/`min()` are built-ins that do the accumulator for you — but knowing the long
  form means you understand what they do.

## ⚠️ Common mistakes to call out
- Initialising the accumulator *inside* the loop (it resets every pass → always equals the last item).
- Using `+` to build a string in a hot loop when `"".join(list)` is cleaner/faster (mention, don't dwell).
- A retry loop with no maximum → it can hang forever. Always cap attempts.

Run the examples:

```bash
python loop_patterns.py
```

➡ Next: **[exercises/](../exercises/)** — Number Guessing Game, FizzBuzz & Multiplication Table
