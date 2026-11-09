"""Check: median sale price by city, sales under $10,000 left out.

Uses the SQLite copy of the data and Python's statistics module, not the site's
JavaScript, so a mistake in the site can't also hide here.

Run from the repository folder:
    python checks/median_price_by_city.py
"""
import sqlite3
import statistics
from decimal import Decimal, ROUND_HALF_UP

con = sqlite3.connect("data/college_town_home_sales.sqlite")
rows = con.execute(
    "SELECT city, state, sale_price FROM home_sales WHERE sale_price >= 10000"
).fetchall()
total = con.execute("SELECT COUNT(*) FROM home_sales").fetchone()[0]

prices = {}
for city, state, price in rows:
    prices.setdefault((city, state), []).append(price)

print(f"Excluded: {total - len(rows)} of {total} sales\n")
results = []
for (city, state), p in prices.items():
    m = Decimal(str(statistics.median(p))).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    results.append((int(m), city, state, len(p)))

for m, city, state, n in sorted(results, reverse=True):
    print(f"{city:<16} {state}  {n:>6,}  ${m:>9,}")
