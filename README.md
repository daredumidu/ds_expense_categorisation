 # 📊 Annual Expense Summary Script  
  
 This repository contains a Python script that reads an Excel file with annual expenses and generates a clean, structured Category × Month summary table. The output is saved as a CSV file for easy use in Excel, Power BI, or financial dashboards.  
  
 The script is ideal for anyone who wants to automate personal or household expense tracking.  
  
 ---  
  
 ## 📁 Features  
  
 - Reads data from the "expenses" tab of an Excel workbook  
 - Automatically groups expenses by month and category  
 - Calculates total spending per category per month  
 - Outputs a clean, pivot‑style CSV file  
 - Works with any dataset following the required format  
  
 ---  
  
 ## 📄 Input Format  
  
 Your Excel file must contain a sheet named \expenses\with the following columns
  
 | Column Name | Description |  
 |--------------------|-------------|  
 | month | Month name or number (e.g., Jan, 1, March) |  
 | category | Expense category (e.g., rent, groceries, transport) |  
 | date | Actual transaction date |  
 | monthly expenses | Optional descriptive field |  
 | amount | Numeric value of the expense |  
  
 ### Supported Categories  
 ``` 
 rent, car installment, electricity, mobile, transport, groceries, subscription, maintenance, other, restaurants, shopping, total  
 ```
 ---  
  
 ## 🛠️ Requirements  
  
 Make sure you have Python 3.8+ installed.  
  
 Install dependencies
 ```bash 
 pip install pandas openpyxl  
 ``` 
 ---  
  
 ## ▶️ How to Use  
  
 1. Place your Excel file (e.g., annual_expenses.xlsx) in the same directory as the script.  
 2. Ensure the data is inside a sheet named expenses.  
 3. Run the script
```bash
 python expense_summary.py
```
 4. After execution, a file named
  
 monthly_expense_summary.csv  
  
 will be created in the same folder.  
  
 ---  
  
 ## 📤 Output  
  
 The generated CSV will contain
  
 - Rows
 - Columns
 - Values
  
 Example
  
 | month | rent | groceries | transport | restaurants | shopping | total |  
 |-------|------|-----------|-----------|-------------|----------|--------|  
 | Jan | 1200 | 320 | 60 | 120 | 200 | 2445 |  
 | Feb | ... | ... | ... | ... | ... | ... |  
  
 ---  
  
 ## 🧩 Script Overview  
  
 The script
 - Loads the Excel file  
 - Reads only the expenses sheet  
 - Normalizes category names  
 - Builds a pivot table  
 - Exports the result to CSV  
  
 This makes it easy to extend the script with
 - Yearly totals  
 - Visualizations  
 - Budget comparisons  
 - Automated reporting  
  
 ---  
  
 ## 🤝 Contributing  
  
 Pull requests are welcome.  
 If you’d like to add new features (charts, dashboards, CLI options), feel free to open an issue.  
  
 ---  
