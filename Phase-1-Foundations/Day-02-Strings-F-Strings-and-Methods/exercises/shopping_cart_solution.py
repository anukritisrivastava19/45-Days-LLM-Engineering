"""
Exercise 2 — Shopping Cart receipt (solution).

Run:
    python shopping_cart_solution.py
"""

item = "Wireless Mouse"
price = 799.0
quantity = 3
gst_rate = 0.18

subtotal = price * quantity
gst = subtotal * gst_rate
total = subtotal + gst

# :,.2f  ->  thousands separator AND 2 decimal places
# :.0%   ->  show a fraction as a whole-number percentage
# We print "Rs" (not ₹) so this runs on the default Windows console — see the
# f-strings module README for the UTF-8 note if you want the real symbol.
print("------ RECEIPT ------")
print(f"{item} x {quantity}  @ Rs {price:,.2f}")
print(f"Subtotal:     Rs {subtotal:,.2f}")
print(f"GST ({gst_rate:.0%}):    Rs {gst:,.2f}")
print(f"TOTAL:        Rs {total:,.2f}")
print("---------------------")
