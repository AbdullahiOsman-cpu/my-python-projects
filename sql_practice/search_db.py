import sqlite3

# 1. Connect to our finance database
connection = sqlite3.connect('finance.db')
cursor = connection.cursor()

# 2. Ask the user what they are looking for
search_month = input("Which month would you like to check? ")

# 3. The 'LIKE' operator makes the search case-insensitive
# We use '%' around the word so it finds any match
query = "SELECT * FROM monthly_budgets WHERE month LIKE ?"
cursor.execute(query, (search_month,))

# 4. Get the result
result = cursor.fetchone()

if result:
    print(f"\n--- Found Data for {result[1]} ---")
    print(f"Income: R{result[2]}")
    print(f"Savings: R{result[3]}")
else:
    print(f"\nSorry, no data found for '{search_month}'.")

connection.close()

