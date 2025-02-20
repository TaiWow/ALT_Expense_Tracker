
import uuid
from datetime import datetime, timezone
import json
import csv
from tabulate import tabulate

# models.py

class Expense:
    def __init__(self, title: str, amount: float):
        self.id = str(uuid.uuid4())[:5]
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at

    def update(self, title: str = None, amount: float = None):
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        expense = cls(data['title'], float(data['amount']))
        expense.id = data['id']
        expense.created_at = datetime.fromisoformat(data['created_at'])
        expense.updated_at = datetime.fromisoformat(data['updated_at'])
        return expense

class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str):
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

    def get_expense_by_id(self, expense_id: str):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, title: str):
        return [expense for expense in self.expenses if expense.title.lower() == title.lower()]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]

    def save_to_json(self, filename: str):
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.expenses = [Expense.from_dict(exp) for exp in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

    def save_to_csv(self, filename: str):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "amount", "created_at", "updated_at"])
            writer.writeheader()
            for expense in self.to_dict():
                writer.writerow(expense)

    def load_from_csv(self, filename: str):
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                self.expenses = [Expense.from_dict(row) for row in reader]
        except FileNotFoundError:
            self.expenses = []
   
# main.py         
dummy_groceries = [
    Expense("Milk", 2.50),
    Expense("Bread", 1.20),
    Expense("Eggs", 3.00),
    Expense("Cheese", 4.50),
    Expense("Apples", 2.00),
    Expense("Chicken", 8.00),
    Expense("Rice", 5.00),
    Expense("Pasta", 1.50),
    Expense("Tomatoes", 2.30),
    Expense("Potatoes", 1.80)
]
        
def main():
    db = ExpenseDatabase()

    for grocery in dummy_groceries:
        db.add_expense(grocery)

    db.save_to_json('groceries.json')
    db.save_to_csv('groceries.csv')
    
    db_from_json = ExpenseDatabase()
    db_from_json.load_from_json('groceries.json')
    print("\n--- Loaded from JSON ---")
    print(tabulate(db_from_json.to_dict(), headers="keys", tablefmt="pretty"))

    db_from_csv = ExpenseDatabase()
    db_from_csv.load_from_csv('groceries.csv')
    print("\n--- Loaded from CSV ---")
    print(tabulate(db_from_csv.to_dict(), headers="keys", tablefmt="pretty"))


if __name__ == "__main__":
    main()


# cli.py

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