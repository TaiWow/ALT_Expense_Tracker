from models import Expense, ExpenseDatabase
from tabulate import tabulate

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
