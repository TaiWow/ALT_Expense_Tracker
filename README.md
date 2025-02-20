
# ALT_School_Expense_Tracker

AltSchool of Data Engineering Tinyuka 2024 First Semester Project Exam - The goal of this project is to assess understanding of **object-oriented programming (OOP)** concepts in Python. Tasked with implementing two classes, `Expense` and `ExpenseDatabase`, to model and manage financial expenses.

## Table of Contents
1. [Project Description](#project-description)
2. [Features](#features)
3. [How to Use](#how-to-use)
   - [Clone the Repository](#clone-the-repository)
   - [Install Dependencies](#install-dependencies)
   - [Run the Application](#run-the-application)
4. [Project Structure](#project-structure)
5. [CLI Commands](#cli-commands)
6. [Example Usage](#example-usage)
7. [Classes Overview](#classes-overview)
   - [Expense Class](#expense-class)
   - [ExpenseDatabase Class](#expensedatabase-class)
8. [License](#license)
9. [GitHub Repository](#github-repository)

---

## Project Description

This project is an **Expense Tracker** application designed to help users manage their financial expenses. The application allows users to add, update, remove, and view expenses. Expenses are stored in a database that can be saved to and loaded from **JSON** and **CSV** files. The project is implemented in Python and is structured into multiple modules for better organization and maintainability.

---

## Features
- **Expense Management**: Add, update, remove, and view expenses.
- **Data Persistence**: Save and load expenses from **JSON** and **CSV** files.
- **Search Functionality**: Retrieve expenses by **ID** or **title**.
- **CLI Interface**: A simple command-line interface for managing expenses.

---

## How to Use

### Clone the Repository
```bash
git clone https://github.com/TaiWow/ALT_School_Expense_Tracker.git
cd ALT_School_Expense_Tracker
```

### Install Dependencies
Install the `tabulate` library for pretty-printing tables:
```bash
pip install tabulate
```

### Run the Application
- Run the main script:
  ```bash
  python main.py
  ```
- Or use the CLI interface:
  ```bash
  python cli.py
  ```

---

## Project Structure

The project is organized into the following files:

- **`models.py`**: Contains the `Expense` and `ExpenseDatabase` classes, which handle the core logic of expense management and data persistence.
- **`main.py`**: Demonstrates the basic functionality of the application by creating a list of dummy expenses and saving/loading them from JSON and CSV files.
- **`cli.py`**: Provides a command-line interface for interacting with the expense tracker.

---

## CLI Commands
1. **Add Expense**: Enter title and amount.
2. **Update Expense**: Enter ID and update title/amount.
3. **Remove Expense**: Enter ID to delete.
4. **View All Expenses**: Display all expenses.
5. **View Expenses by Title**: Search expenses by title.
6. **Exit**: Exit the application.

---

## Example Usage

### Add an Expense
```bash
Enter your choice: 1
Enter the expense title: Coffee
Enter the expense amount: 3.5
Expense added: {'id': 'abc12', 'title': 'Coffee', 'amount': 3.5, 'created_at': '2025-02-19T22:06:06.188644+00:00', 'updated_at': '2025-02-19T22:06:06.188644+00:00'}
```

### Update an Expense
```bash
Enter your choice: 2
Enter the expense ID to update: abc12
Enter new title (current: Coffee): Latte
Enter new amount (current: 3.5): 4.0
Expense updated: {'id': 'abc12', 'title': 'Latte', 'amount': 4.0, 'created_at': '2025-02-19T22:06:06.188644+00:00', 'updated_at': '2025-02-19T22:06:06.188644+00:00'}
```

### View All Expenses
```bash
Enter your choice: 4
--- All Expenses ---
+-------+----------+--------+----------------------------+----------------------------+
|   id  |   title  | amount |         created_at         |         updated_at         |
+-------+----------+--------+----------------------------+----------------------------+
| 0cf21 |   Milk   |  2.5   | 2025-02-19T22:06:06.188644 | 2025-02-19T22:06:06.188644 |
| fdb74 |   Bread  |  1.2   | 2025-02-19T22:06:06.188871 | 2025-02-19T22:06:06.188871 |
| 6b183 |   Eggs   |  3.0   | 2025-02-19T22:06:06.188877 | 2025-02-19T22:06:06.188877 |
| d9495 |  Cheese  |  4.5   | 2025-02-19T22:06:06.188881 | 2025-02-19T22:06:06.188881 |
| eb1dc |  Apples  |  2.0   | 2025-02-19T22:06:06.188885 | 2025-02-19T22:06:06.188885 |
| 3cfba | Chicken  |  8.0   | 2025-02-19T22:06:06.188889 | 2025-02-19T22:06:06.188889 |
| e2718 |   Rice   |  5.0   | 2025-02-19T22:06:06.188892 | 2025-02-19T22:06:06.188892 |
| 24d97 |  Pasta   |  1.5   | 2025-02-19T22:06:06.188895 | 2025-02-19T22:06:06.188895 |
| 427c6 | Tomatoes |  2.3   | 2025-02-19T22:06:06.188901 | 2025-02-19T22:06:06.188901 |
| 2abe7 | Potatoes |  1.8   | 2025-02-19T22:06:06.188904 | 2025-02-19T22:06:06.188904 |
+-------+----------+--------+----------------------------+----------------------------+
```

---

## Classes Overview

### Expense Class
Represents a financial expense with the following attributes:
- `id`: Unique identifier (auto-generated).
- `title`: Title/description of the expense.
- `amount`: Amount of money spent.
- `created_at`: Timestamp when the expense was created.
- `updated_at`: Timestamp when the expense was last updated.

**Methods**:
- `update()`: Update the title or amount.
- `to_dict()`: Convert the expense to a dictionary.

### ExpenseDatabase Class
Manages a collection of `Expense` objects.

**Methods**:
- `add_expense()`: Add a new expense.
- `remove_expense()`: Remove an expense by ID.
- `get_expense_by_id()`: Retrieve an expense by ID.
- `get_expenses_by_title()`: Retrieve expenses by title.
- `save_to_json()`: Save expenses to a JSON file.
- `load_from_json()`: Load expenses from a JSON file.
- `save_to_csv()`: Save expenses to a CSV file.
- `load_from_csv()`: Load expenses from a CSV file.

---

