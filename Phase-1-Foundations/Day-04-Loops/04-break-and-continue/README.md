# 04 — `break` and `continue`

These two keywords let you change a loop's flow mid-stream:

| Keyword | Meaning | Picture |
|---------|---------|---------|
| `break` | **Quit the loop now** — jump out completely | emergency exit door |
| `continue` | **Skip the rest of this round**, go to the next item | skip-this-track button |

```python
for item in items:
    if bad(item):
        continue        # skip bad items, keep looping
    if done(item):
        break           # stop the whole loop
    process(item)
```

## `break` — stop as soon as you've found what you need
Searching a list? The moment you find the match, there's no reason to keep looking. `break` saves
work and clearly signals "we're done here."

## `continue` — ignore this one, carry on
Filtering as you go? `continue` skips items that don't qualify without nesting the rest of your body
inside an `if`. It keeps the "happy path" un-indented and readable.

## The loop-`else` (the feature almost nobody teaches)
A `for`/`while` can have an `else:` that runs **only if the loop finished without hitting `break`**.
It's the clean way to express "searched everything, found nothing":

```python
for user in users:
    if user == target:
        print("Found!")
        break
else:
    print("Not found.")     # runs only if we never broke out
```

## 🎤 Talking points (what to say & focus on)
- **`break` = leave the building; `continue` = skip to the next person in line.** Say it that simply,
  then show both in one loop so the contrast lands.
- **`break` is the natural exit for `while True:`** — tie it back to Module 01's menu. "Loop forever,
  break when they pick Quit."
- **`continue` flattens code.** Show the nested-`if` version, then the `continue` ("guard clause")
  version. The second is what reviewers prefer — early-skip the junk, keep the main logic flat.
- **Validation/retry loop is the killer demo:** "ask for a PIN, give 3 tries, `break` on success,
  fall through to lock-out." Real, relatable, uses both keywords + a counter.
- **loop-`else` is a genuine gem.** Most beginners write a clumsy `found = False` flag; show that
  first, then the `for/else` that deletes the flag. They'll remember it.
- **Both affect only the *innermost* loop.** Preview Module 05: a `break` inside a nested loop only
  exits the inner one.

## ⚠️ Common mistakes to call out
- Thinking `break` exits the program — it exits only the loop (use `return`/`exit()` for more).
- Thinking `continue` restarts the loop from the top item — it goes to the *next* item.
- In a `while`, putting the counter update *after* a `continue` so it never runs → infinite loop.
- Attaching `else` to a loop and expecting it to run "if the loop ran" — it runs if the loop **didn't
  `break`**.

Run the examples (it uses input() for the PIN demo):

```bash
python break_continue.py
```

➡ Next: **[05-nested-loops](../05-nested-loops/)**
