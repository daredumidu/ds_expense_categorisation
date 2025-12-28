import pandas as pd

# Load the Excel file
df = pd.read_excel("monthly_expense.xlsx", sheet_name="monthly_expense")

# Ensure month column is consistent (string or datetime)
df['month'] = df['month'].astype(str)

# Standardize category names (optional but helpful)
df['category'] = df['category'].str.lower().str.strip()

# Pivot table: rows = months, columns = categories, values = total amount
pivot_table = df.pivot_table(
    index='month',
    columns='category',
    values='amount',
    aggfunc='sum',
    fill_value=0
)

# Reorder columns based on your defined category list
categories = [
    "rent", "car installment", "electricity", "mobile", "transport",
    "groceries", "subscription", "maintenance", "other",
    "restaurants", "shopping", "total"
]

# Keep only categories that exist in the data
existing_cols = [c for c in categories if c in pivot_table.columns]
pivot_table = pivot_table[existing_cols]

# Save to CSV
pivot_table.to_csv("monthly_expense_summary.csv")

print("CSV file 'monthly_expense_summary.csv' created successfully!")
print(pivot_table)
