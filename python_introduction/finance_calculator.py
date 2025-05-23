monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_expenses - monthly_income
projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: {projected_Savings}")
