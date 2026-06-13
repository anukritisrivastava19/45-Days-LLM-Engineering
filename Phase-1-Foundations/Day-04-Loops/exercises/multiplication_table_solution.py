"""
Exercise 3 — Multiplication Table (solution).

Run:
    python multiplication_table_solution.py
"""

N = 10

# --- Header row (optional but makes it look pro) ---
print("    |" + "".join(f"{c:>4}" for c in range(1, N + 1)))
print("----+" + "----" * N)

# --- The grid: outer = rows, inner = columns ---
for r in range(1, N + 1):              # each pass = one full row
    row = ""
    for c in range(1, N + 1):          # inner loop fills that row
        row += f"{r * c:>4}"           # >4 right-aligns each number in 4 chars
    print(f"{r:>3} |{row}")            # print ONCE per row (after inner loop)
