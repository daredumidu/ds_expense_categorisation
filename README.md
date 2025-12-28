LINE 1: # 📊 Annual Expense Summary Script  
LINE 2:  
LINE 3: This repository contains a Python script that reads an Excel file with annual expenses and generates a clean, structured Category × Month summary table. The output is saved as a CSV file for easy use in Excel, Power BI, or financial dashboards.  
LINE 4:  
LINE 5: The script is ideal for anyone who wants to automate personal or household expense tracking.  
LINE 6:  
LINE 7: ---  
LINE 8:  
LINE 9: ## 📁 Features  
LINE 10:  
LINE 11: - Reads data from the "expenses" tab of an Excel workbook  
LINE 12: - Automatically groups expenses by month and category  
LINE 13: - Calculates total spending per category per month  
LINE 14: - Outputs a clean, pivot‑style CSV file  
LINE 15: - Works with any dataset following the required format  
LINE 16:  
LINE 17: ---  
LINE 18:  
LINE 19: ## 📄 Input Format  
LINE 20:  
LINE 21: Your Excel file must contain a sheet named \expenses\with the following columns:  
LINE 22:  
LINE 23: | Column Name | Description |  
LINE 24: |--------------------|-------------|  
LINE 25: | month | Month name or number (e.g., Jan, 1, March) |  
LINE 26: | category | Expense category (e.g., rent, groceries, transport) |  
LINE 27: | date | Actual transaction date |  
LINE 28: | monthly expenses | Optional descriptive field |  
LINE 29: | amount | Numeric value of the expense |  
LINE 30:  
LINE 31: ### Supported Categories  
LINE 32:  
LINE 33: rent, car installment, electricity, mobile, transport, groceries, subscription, maintenance, other, restaurants, shopping, total  
LINE 34:  
LINE 35: ---  
LINE 36:  
LINE 37: ## 🛠️ Requirements  
LINE 38:  
LINE 39: Make sure you have Python 3.8+ installed.  
LINE 40:  
LINE 41: Install dependencies:  
LINE 42:  
LINE 43: pip install pandas openpyxl  
LINE 44:  
LINE 45: ---  
LINE 46:  
LINE 47: ## ▶️ How to Use  
LINE 48:  
LINE 49: 1. Place your Excel file (e.g., annual_expenses.xlsx) in the same directory as the script.  
LINE 50: 2. Ensure the data is inside a sheet named expenses.  
LINE 51: 3. Run the script:  
LINE 52:  
LINE 53: python expense_summary.py  
LINE 54:  
LINE 55: 4. After execution, a file named:  
LINE 56:  
LINE 57: monthly_expense_summary.csv  
LINE 58:  
LINE 59: will be created in the same folder.  
LINE 60:  
LINE 61: ---  
LINE 62:  
LINE 63: ## 📤 Output  
LINE 64:  
LINE 65: The generated CSV will contain:  
LINE 66:  
LINE 67: - Rows: Months  
LINE 68: - Columns: Expense categories  
LINE 69: - Values: Total amount spent per category per month  
LINE 70:  
LINE 71: Example:  
LINE 72:  
LINE 73: | month | rent | groceries | transport | restaurants | shopping | total |  
LINE 74: |-------|------|-----------|-----------|-------------|----------|--------|  
LINE 75: | Jan | 1200 | 320 | 60 | 120 | 200 | 2445 |  
LINE 76: | Feb | ... | ... | ... | ... | ... | ... |  
LINE 77:  
LINE 78: ---  
LINE 79:  
LINE 80: ## 🧩 Script Overview  
LINE 81:  
LINE 82: The script:  
LINE 83: - Loads the Excel file  
LINE 84: - Reads only the expenses sheet  
LINE 85: - Normalizes category names  
LINE 86: - Builds a pivot table  
LINE 87: - Exports the result to CSV  
LINE 88:  
LINE 89: This makes it easy to extend the script with:  
LINE 90: - Yearly totals  
LINE 91: - Visualizations  
LINE 92: - Budget comparisons  
LINE 93: - Automated reporting  
LINE 94:  
LINE 95: ---  
LINE 96:  
LINE 97: ## 🤝 Contributing  
LINE 98:  
LINE 99: Pull requests are welcome.  
LINE 100: If you’d like to add new features (charts, dashboards, CLI options), feel free to open an issue.  
LINE 101:  
LINE 102: ---  
LINE 103:  
LINE 104: ## 📜 License  
LINE 105:  
LINE 106: This project is released under the MIT License.
