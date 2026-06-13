# 01 — `while` Loops

A `while` loop repeats a block **as long as a condition stays `True`**. Use it when you don't know
how many times you'll loop ahead of time — you're waiting on something to change.

```python
while <condition>:        # checked BEFORE each round
    <indented block>      # runs, then we check the condition again
```

| You want to… | Reach for |
|--------------|-----------|
| Repeat **until** something becomes true (user types "quit", retries succeed, game ends) | `while` |
| Repeat **once per item** in a known collection | `for` (Module 02) |

## The anatomy of every `while` loop
Three parts — miss the third and you loop forever:
1. **Initialise** a variable *before* the loop (`count = 0`).
2. **Test** it in the condition (`while count < 3:`).
3. **Update** it *inside* the loop (`count += 1`) so the condition eventually goes `False`.

## ⚠️ Infinite loops — the #1 beginner bug
```python
count = 0
while count < 3:
    print("hi")        # ❌ count never changes → prints forever
```
The fix is the **update step** (`count += 1`). If you ever start an accidental infinite loop in the
terminal, press **Ctrl + C** to kill it.

## 🎤 Talking points (what to say & focus on)
- **"While the light is red, wait."** Frame it physically — the loop body is the thing you keep doing
  *while* the condition holds. The moment it's false, you walk out the bottom.
- **The condition is checked at the top**, before each pass — so a `while False:` loop runs **zero**
  times. That's a feature, not a bug.
- **Three parts, always.** Initialise → test → update. Make students point at each one in your code.
- **Real use is "wait for a condition," not counting.** Counting is a `for` job. `while` shines for
  menus ("loop until they pick Quit"), retries ("loop until the API responds"), and games ("loop
  until someone wins"). Show the menu/retry examples, not just `count < 5`.
- **`while True:` + `break` is a legit, common idiom** — an intentional infinite loop you exit from
  the inside when a condition is met. We preview `break` here and go deep in Module 04.

## ⚠️ Common mistakes to call out
- Forgetting the update step → infinite loop.
- Updating the wrong variable (`count` in the test, `i` in the update).
- Using `while` when a `for` is clearer (looping over a known list).
- Putting the update step *after* a `break`/`continue` so it sometimes gets skipped.

Run the examples:

```bash
python while_loops.py
```

➡ Next: **[02-for-loops](../02-for-loops/)**
