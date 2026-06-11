# 06 — f-strings (the best way to build text)

Joining strings with `+` and `str()` gets ugly fast:

```python
"You are " + str(age) + " years old and " + str(height) + "m tall."   # 😣
```

**f-strings** fix this. Put an `f` before the opening quote, then drop variables (or any
expression) straight into `{curly braces}`:

```python
f"You are {age} years old and {height}m tall."   # 😍
```

| Feature | Example | Result (if `age=25`) |
|---------|---------|----------------------|
| Insert a variable | `f"Age: {age}"` | `Age: 25` |
| Insert an expression | `f"Next year: {age + 1}"` | `Next year: 26` |
| Call a method inline | `f"{name.upper()}"` | `RIYA` |

## Formatting numbers
Add a `:` after the value inside the braces to control how it looks — great for money and reports.

| Format | Example | Result |
|--------|---------|--------|
| 2 decimal places | `f"{3.14159:.2f}"` | `3.14` |
| Thousands separator | `f"{1000000:,}"` | `1,000,000` |
| Both together | `f"Rs {2499.5:,.2f}"` | `Rs 2,499.50` |
| Percentage | `f"{0.18:.0%}"` | `18%` |

> 💡 `:.2f` means "fixed-point, 2 digits after the dot." You'll use it constantly for prices.

> 🪟 **Why `Rs` and not `₹`?** The `₹` symbol is perfectly valid Python, but the default Windows
> terminal (cp1252 encoding) can't *display* it and will crash with a `UnicodeEncodeError`. We
> print `Rs` to stay portable. To use the real symbol, run with UTF-8 output — e.g. add at the top
> of your file: `import sys; sys.stdout.reconfigure(encoding="utf-8")`.

Run the examples:

```bash
python f_strings.py
```

➡ Next: [07-string-methods](../07-string-methods/)
