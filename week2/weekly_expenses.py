# Program to calculate a student's weekly expenses

student = input("Student name: ")

transport_cost = float(input("Daily transport cost: "))
feeding_cost = float(input("Daily feeding cost: "))
campus_days = int(input("Days on campus: "))
extra_expenses = float(input("Other weekly expenses: "))

transport = transport_cost * campus_days
feeding = feeding_cost * campus_days

total = transport + feeding + extra_expenses

print("\nWEEKLY EXPENSE SUMMARY")
print("Student:", student)
print(f"Transport total: NGN {transport:,.2f}")
print(f"Feeding total: NGN {feeding:,.2f}")
print(f"Other expenses: NGN {extra_expenses:,.2f}")
print(f"Weekly total: NGN {total:,.2f}")
