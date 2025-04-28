# ---
# jupyter:
#   jupytext_format_version: '1.5'
#   kernelspec: {display_name: python3, language: python}
# ---

# %% [markdown]
# # Monthly Sales Report
day_from = "2025-04-01"
day_to   = "2025-04-30"

# %%
from sql_helper import query
import matplotlib.pyplot as plt

df = query(f"""
SELECT order_date, SUM(amount) revenue
FROM dbo.sales
WHERE order_date BETWEEN '{day_from}' AND '{day_to}'
GROUP BY order_date
""")

df.plot(x="order_date", y="revenue")
plt.title("Daily revenue")
plt.savefig("revenue.png")
