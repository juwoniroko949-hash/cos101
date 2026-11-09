# Student Weekly Expense Calculator - Week 3

name = input("Student name: ")

transport = float(input("Daily transport cost: "))
while transport < 0:
    print("Expense cannot be negative")
    transport = float(input("Enter transport cost again: "))

feeding = float(input("Daily feeding cost: "))
while feeding < 0:
    print("Expense cannot be negative")
    feeding = float(input("Enter feeding cost again: "))

days = int(input("Days on campus: "))
while days < 0:
    print("Days cannot be negative")
    days = int(input("Enter days again: "))

other = float(input("Other weekly expenses: "))
while other < 0:
    print("Expense cannot be negative")
    other = float(input("Enter other expenses again: "))

# Calculate expenses
transport_total = transport * days
feeding_total = feeding * days
total = transport_total + feeding_total + other

# Display summary
print("\nWEEKLY EXPENSE SUMMARY")
print("Student:", name)
print(f"Transport total: NGN {transport_total:,.2f}")
print(f"Feeding total: NGN {feeding_total:,.2f}")
print(f"Other expenses: NGN {other:,.2f}")
print(f"Weekly total: NGN {total:,.2f}")

# Enter weekly budget
budget = float(input("\nEnter your weekly budget: "))

while budget < 0:
    print("Budget cannot be negative")
    budget = float(input("Enter budget again: "))

# Check budget
print("\nBUDGET SUMMARY")

if total < budget:
    remaining = budget - total
    print("Status: WITHIN BUDGET")
    print(f"Amount remaining: NGN {remaining:,.2f}")

elif total == budget:
    print("Status: EXACTLY ON BUDGET")
    print("Amount remaining: NGN 0.00")

else:
    exceeded = total - budget
    print("Status: OVER BUDGET")
    print(f"Amount exceeded: NGN {exceeded:,.2f}")
