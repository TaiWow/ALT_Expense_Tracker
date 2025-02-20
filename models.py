import uuid
from datetime import datetime, timezone
import json
import csv



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


