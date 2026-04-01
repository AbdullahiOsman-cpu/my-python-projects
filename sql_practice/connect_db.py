import sqlite3

# 1. Connect to the database file
connection = sqlite3.connect('finance.db')
cursor = connection.cursor()

# 2. Get data from the user
month = input("Enter the month: ")
income = int(input("Enter monthly income: "))
savings = int(income * 0.20)

# 3. The Backend Magic: Send data to SQL
cursor.execute("INSERT INTO monthly_budgets (month, income, savings) VALUES (?, ?, ?)", (month, income, savings))

# 4. Save and Close
connection.commit()
connection.close()

print(f"Success! {month} budget has been recorded in the database.")

