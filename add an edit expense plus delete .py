
import json
import os
from datetime import datetime

# Optional color support
try:
    from colorama import init as colorama_init
    colorama_init(autoreset=True)
except Exception:
    pass

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
CYAN = "\033[36m"

DATA_FILE = "budget_data.json"


def c(text, color):
    """Return colored text."""
    return f"{color}{text}{RESET}"


def load_data():
    """Load data from JSON file or initialize default structure."""
    if not os.path.exists(DATA_FILE):
        return {"income": [], "expenses": [], "budgets": {}}
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    """Save data to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=2)


# -------------------- INCOME --------------------

def add_income(data):
    """Add a new income entry."""
    try:
        amount = float(input("Enter income amount: "))
    except ValueError:
        print(c("Invalid amount.", RED))
        return

    source = input("Source/Description: ")
    date = input("Date (YYYY-MM-DD, blank for today): ") or \
        datetime.today().strftime("%Y-%m-%d")

    data["income"].append({
        "amount": amount,
        "source": source,
        "date": date
    })

    print(c("Income added successfully.", GREEN))


def edit_income(data):
    """Edit an existing income entry."""
    incomes = data.get("income", [])

    if not incomes:
        print(c("No income entries available.", YELLOW))
        return

    for idx, income in enumerate(incomes):
        print(f"{idx}. {income['amount']} | "
              f"{income['source']} | {income['date']}")

    try:
        index = int(input("Select index to edit: "))
        if index < 0 or index >= len(incomes):
            raise IndexError
    except (ValueError, IndexError):
        print(c("Invalid selection.", RED))
        return

    income = incomes[index]

    new_amount = input(f"New amount ({income['amount']}): ")
    new_source = input(f"New source ({income['source']}): ")
    new_date = input(f"New date ({income['date']}): ")

    if new_amount:
        try:
            income["amount"] = float(new_amount)
        except ValueError:
            print(c("Invalid amount entered. Keeping original.", YELLOW))

    if new_source:
        income["source"] = new_source

    if new_date:
        income["date"] = new_date

    print(c("Income updated.", GREEN))


def delete_income(data):
    """Delete an income entry."""
    incomes = data.get("income", [])

    if not incomes:
        print(c("No income entries available.", YELLOW))
        return

    for idx, income in enumerate(incomes):
        print(f"{idx}. {income['amount']} | "
              f"{income['source']} | {income['date']}")

    try:
        index = int(input("Select index to delete: "))
        if index < 0 or index >= len(incomes):
            raise IndexError
    except (ValueError, IndexError):
        print(c("Invalid selection.", RED))
        return

    deleted = incomes.pop(index)
    print(c(f"Deleted income: {deleted['amount']}", GREEN))


# -------------------- EXPENSE --------------------

def add_expense(data):
    """Add a new expense entry."""
    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print(c("Invalid amount.", RED))
        return

    category = input("Category: ")
    desc = input("Description: ")
    date = input("Date (YYYY-MM-DD, blank for today): ") or \
        datetime.today().strftime("%Y-%m-%d")

    data["expenses"].append({
        "amount": amount,
        "category": category,
        "desc": desc,
        "date": date
    })

    print(c("Expense added successfully.", GREEN))


def edit_expense(data):
    """Edit an existing expense entry."""
    expenses = data.get("expenses", [])

    if not expenses:
        print(c("No expenses available.", YELLOW))
        return

    for idx, expense in enumerate(expenses):
        print(f"{idx}. {expense['amount']} | "
              f"{expense['category']} | "
              f"{expense['desc']} | "
              f"{expense['date']}")

    try:
        index = int(input("Select index to edit: "))
        if index < 0 or index >= len(expenses):
            raise IndexError
    except (ValueError, IndexError):
        print(c("Invalid selection.", RED))
        return

    expense = expenses[index]

    new_amount = input(f"New amount ({expense['amount']}): ")
    new_category = input(f"New category ({expense['category']}): ")
    new_desc = input(f"New description ({expense['desc']}): ")
    new_date = input(f"New date ({expense['date']}): ")

    if new_amount:
        try:
            expense["amount"] = float(new_amount)
        except ValueError:
            print(c("Invalid amount entered. Keeping original.", YELLOW))

    if new_category:
        expense["category"] = new_category

    if new_desc:
        expense["desc"] = new_desc

    if new_date:
        expense["date"] = new_date

    print(c("Expense updated.", GREEN))


def delete_expense(data):
    """Delete an expense entry."""
    expenses = data.get("expenses", [])

    if not expenses:
        print(c("No expenses available.", YELLOW))
        return

    for idx, expense in enumerate(expenses):
        print(f"{idx}. {expense['amount']} | "
              f"{expense['category']} | "
              f"{expense['desc']} | "
              f"{expense['date']}")

    try:
        index = int(input("Select index to delete: "))
        if index < 0 or index >= len(expenses):
            raise IndexError
    except (ValueError, IndexError):
        print(c("Invalid selection.", RED))
        return

    deleted = expenses.pop(index)
    print(c(f"Deleted expense: {deleted['amount']}", GREEN))


# -------------------- BUDGET --------------------

def set_budget(data):
    """Set a budget for a category."""
    category = input("Category: ")
    try:
        amount = float(input("Monthly budget amount: "))
    except ValueError:
        print(c("Invalid amount.", RED))
        return

    data["budgets"][category] = amount
    print(c("Budget set successfully.", GREEN))


def show_summary(data):
    """Display income, expenses, and budget summary."""
    print("\n" + c("==== SUMMARY ====", BOLD))

    total_income = sum(i["amount"] for i in data["income"])
    total_expenses = sum(e["amount"] for e in data["expenses"])
    net = total_income - total_expenses

    print(f"Total Income:   {total_income:.2f}")
    print(f"Total Expenses: {total_expenses:.2f}")
    print("Net Savings:   " +
          c(f"{net:.2f}", GREEN if net >= 0 else RED))


# -------------------- MAIN MENU --------------------

def main():
    """Main application loop."""
    data = load_data()

    while True:
        print("\n--- MENU ---")
        print("1. Add Income")
        print("2. Edit Income")
        print("3. Delete Income")
        print("4. Add Expense")
        print("5. Edit Expense")
        print("6. Delete Expense")
        print("7. Set Budget")
        print("8. Show Summary")
        print("9. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_income(data)
        elif choice == "2":
            edit_income(data)
        elif choice == "3":
            delete_income(data)
        elif choice == "4":
            add_expense(data)
        elif choice == "5":
            edit_expense(data)
        elif choice == "6":
            delete_expense(data)
        elif choice == "7":
            set_budget(data)
        elif choice == "8":
            show_summary(data)
        elif choice == "9":
            save_data(data)
            print(c("Data saved. Goodbye!", GREEN))
            break
        else:
            print(c("Invalid option.", YELLOW))


if __name__ == "__main__":
    main()
