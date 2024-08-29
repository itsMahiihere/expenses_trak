def add_expense(expenses):
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    expenses.append({"description": description, "amount": amount})
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nRecorded Expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['description']}: ${expense['amount']:.2f}")

    total_expenses = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: ${total_expenses:.2f}")

def main():
    expenses = []
    
    while True:
        print("\nExpense Tracker")
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
