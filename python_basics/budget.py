# Simple Backend Logic: Income vs Savings
income = int(input("Enter monthly income: "))
save_rate = 0.20 # Saving 20% for tech gear

to_save = income * save_rate
to_spend = income - to_save

print(f"Goal: Save R{to_save} for your October milestone.")
print(f"Remaining: R{to_spend} for daily expenses.")

