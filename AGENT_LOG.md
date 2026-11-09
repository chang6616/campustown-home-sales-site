# Agent log

Add a dated entry each time you work with your AI coding agent, with the newest entry at the bottom. Each entry records what you asked the agent, what it produced, and what you checked or changed. Paste your key prompts in exactly as you typed them. Include at least one time the agent got something wrong, and how you caught it.

Copy this outline for each entry:

```markdown
## YYYY-MM-DD: What you worked on

- **Asked:** "Paste your prompt here."
- **Agent produced:** What it made or changed.
- **Checked or changed:** How you checked it, and what you fixed.
```

## 2026-11-09: First page, median sale price by city

- **Asked:** "先完成老師的requirement吧" (do the course's example task: replace the placeholder index.html with median sale price per city from data/college_town_home_sales.csv, leaving out sales under $10,000 and stating the rule).
- **Agent produced:** A new `index.html` that loads the CSV in the browser, drops sales under $10,000, and shows a table of each city's sales count and median price, rounded to whole dollars. Also `checks/median_price_by_city.py`, a separate check using the SQLite file.
- **Checked or changed:** The first version loaded a CSV library (Papa Parse) from a CDN, and the page got stuck on "Loading data…" when the CDN could not be reached. The agent replaced it with a small built-in CSV parser so the page has no outside dependency. Then all 18 medians on the page matched the check script. Pittsboro's raw median is $876,985.50, so the page rounds it to $876,986.
