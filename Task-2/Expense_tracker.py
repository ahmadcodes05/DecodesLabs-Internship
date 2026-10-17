import json
import os
file_name = "expenses.json"
if os.path.exists(file_name):
    try:
        with open(file_name, "r") as file:
            expenses = json.load(file)
    except (json.JSONDecodeError, OSError):
        expenses = []
else:
    expenses = []
def save_expenses():
    with open(file_name, "w") as file:
        json.dump(expenses, file, indent=4)
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        try:
            amount = float(input("Enter expense amount (Rs.): "))
            if amount <= 0:
                print("Amount must be greater than zero!")
            else:
                expenses.append(amount)
                save_expenses()
                print("Expense added successfully!")
        except ValueError:
            print("Please enter a valid amount!")
        except OSError:
            print("Could not save the expense to the file.")
    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\nYour Expenses:")
            for number, amount in enumerate(expenses, start=1):
                print(f"{number}. Rs. {amount:.2f}")
    elif choice == "3":
        total = sum(expenses)
        print(f"Total Expenses: Rs. {total:.2f}")
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice! Please try again.")
