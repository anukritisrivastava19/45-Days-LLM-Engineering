# 02 — `for` Loops

A `for` loop runs the body **once for each item** in a collection (a string, list, range, dict…).
It's the most common loop in real Python because most work *is* "do this for every X."

```python
for item in collection:     # item takes each value in turn
    <indented block>
```

`for ch in "AI":` gives you `ch = "A"`, then `ch = "I"`. No counter to manage, no infinite-loop risk —
the loop ends automatically when the collection runs out. That's why we prefer `for` over `while`
whenever we already have the collection.

## `for` vs `while`
| | `for` | `while` |
|--|-------|---------|
| Use when | You have a collection / known count | You're waiting on a condition |
| Loop variable | Managed for you | You manage it (init/update) |
| Infinite-loop risk | None | Yes, if you forget to update |

## `enumerate` — when you need the index too
```python
for index, name in enumerate(players, start=1):
    print(index, name)        # 1 Asha, 2 Ben, ...
```
Cleaner than tracking a manual `i += 1` counter. Reach for it the moment you catch yourself wanting
"the position *and* the value."

## 🎤 Talking points (what to say & focus on)
- **"For each item, do this."** Read the loop out loud in English — `for student in class:` → "for
  each student in the class." If it reads naturally, it's the right tool.
- **The loop variable is just a name you pick.** `for x in ...` and `for student in ...` behave
  identically — pick a name that documents what one item *is*. Good names teach the reader.
- **No counter, no off-by-one.** Contrast with the `while` version of the same task: `for` removes a
  whole class of bugs because Python handles the start/stop/advance for you.
- **`enumerate` beats a manual counter.** Show the "bad" `i = 0; i += 1` version, then replace it
  with `enumerate(..., start=1)`. This is the idiomatic upgrade interviewers like to see.
- **You can loop over almost anything iterable** — strings, lists, `range`, dict keys, file lines.
  Today: strings/lists/range. Dicts come on Day 6.

## ⚠️ Common mistakes to call out
- Modifying the list you're looping over (adding/removing items mid-loop) → skipped or repeated items.
- Reaching for `range(len(items))` just to index — usually you want the item directly, or `enumerate`.
- Expecting the loop variable to "survive" meaningfully after the loop (it keeps its *last* value).

Run the examples:

```bash
python for_loops.py
```

➡ Next: **[03-range](../03-range/)**
