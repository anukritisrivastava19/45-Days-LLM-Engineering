# 04 — Escape Characters & Triple-Quoted Strings

Some characters are hard to type inside a string — a newline, a tab, or the very quote you're using
to wrap the string. **Escape characters** solve this: a backslash `\` plus a letter means
"something special."

| Escape | Meaning |
|--------|---------|
| `\n` | new line |
| `\t` | tab |
| `\"` | a literal double quote (inside a `"..."` string) |
| `\'` | a literal single quote (inside a `'...'` string) |
| `\\` | a literal backslash |

```python
print("Line 1\nLine 2")     # prints on two lines
print("Name:\tRiya")        # Name:   Riya  (tab gap)
print("She said \"hi\"")    # She said "hi"
```

> 🪟 **Windows paths gotcha:** `"C:\name"` has a sneaky `\n`! Use `\\` (`"C:\\Users"`) or a raw
> string `r"C:\Users"` where the `r` turns off escaping.

## Triple-quoted strings
Wrap text in `"""..."""` (or `'''...'''`) to write **multi-line strings** exactly as they appear —
no `\n` needed. Perfect for paragraphs, and later for **LLM prompts**.

```python
prompt = """You are a helpful assistant.
Summarise the text below in 3 bullet points.
Keep it under 50 words."""
```

Run the examples:

```bash
python escape_and_triple_quotes.py
```

➡ Next: [05-len-input-typecasting](../05-len-input-typecasting/)
