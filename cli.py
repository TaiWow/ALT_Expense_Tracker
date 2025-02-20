
from models import Expense, ExpenseDatabase
from tabulate import tabulate


def display_menu():
    print("\n--- Expense Tracker Menu ---")
    print("1. Add a new expense")
    print("2. Update an expense")
    print("3. Remove an expense")
    print("4. View all expenses")
    print("5. View expenses by title")
    print("6. Exit")

def add_expense(db):
    title = input("Enter the expense title: ")
    amount = float(input("Enter the expense amount: "))
    expense = Expense(title, amount)
    db.add_expense(expense)
    print(f"Expense added: {expense.to_dict()}")

def update_expense(db):
     #view_all_expenses(db)
    expense_id = input("Enter the expense ID to update: ")
    expense = db.get_expense_by_id(expense_id)
    if expense:
        title = input(f"Enter new title (current: {expense.title}): ") or expense.title
        amount = input(f"Enter new amount (current: {expense.amount}): ") or expense.amount
        if amount:
            amount = float(amount)
        expense.update(title, amount)
        print(f"Expense updated: {expense.to_dict()}")
    else:
        print("Expense not found.")

def remove_expense(db):
     #view_all_expenses(db)
    expense_id = input("Enter the expense ID to remove: ")
    if db.remove_expense(expense_id):
        print(f"Expense with ID {expense_id} removed.")
    else:
        print("Expense not found.")

def view_all_expenses(db):
    expenses = db.to_dict()
    if expenses:
        print("\n--- All Expenses ---")
        print(tabulate(expenses, headers="keys", tablefmt="pretty"))
    else:
        print("No expenses found.")

def view_expenses_by_title(db):
    #view_all_expenses(db)
    title = input("Enter the title to search for: ")
    expenses = db.get_expenses_by_title(title)
    if expenses:
        print(f"\n--- Expenses with Title: {title} ---")
        print(tabulate([expense.to_dict() for expense in expenses], headers="keys", tablefmt="pretty"))
    else:
        print(f"No expenses found with title: {title}")

def main():
    db = ExpenseDatabase()

    
    db_from_json = ExpenseDatabase()
    db_from_json.load_from_json('groceries.json')
    print("\n--- Loaded from JSON ---")
    print(tabulate(db_from_json.to_dict(), headers="keys", tablefmt="pretty"))

    db_from_csv = ExpenseDatabase()
    db_from_csv.load_from_csv('groceries.csv')
    print("\n--- Loaded from CSV ---")
    print(tabulate(db_from_csv.to_dict(), headers="keys", tablefmt="pretty"))


    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(db)
        elif choice == "2":
            update_expense(db)
        elif choice == "3":
            remove_expense(db)
        elif choice == "4":
            view_all_expenses(db)
        elif choice == "5":
            view_expenses_by_title(db)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()