import json
import os
from datetime import datetime

DATA_FILE = "budget_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"income": [], "expenses": [], "budgets": {}}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_income(data):
    amount = float(input("Enter income amount: "))
    source = input("Source/Description: ")
    date = input("Date (YYYY-MM-DD, blank for today): ") or datetime.today().strftime("%Y-%m-%d")
    data["income"].append({"amount": amount, "source": source, "date": date})
    print("Income recorded.")

def add_expense(data):
    amount = float(input("Enter expense amount: "))
    category = input("Category (e.g., Food, Rent, Entertainment): ")
    desc = input("Description: ")
    date = input("Date (YYYY-MM-DD, blank for today): ") or datetime.today().strftime("%Y-%m-%d")
    data["expenses"].append({"amount": amount, "category": category, "desc": desc, "date": date})
    print("Expense recorded.")

def set_budget(data):
    category = input("Set budget for category: ")
    amount = float(input(f"Enter monthly budget for {category}: "))
    data["budgets"][category] = amount
    print(f"Budget for {category} set to {amount}.")

def show_summary(data):
    print("\n==== Budget Summary ====")
    monthly_expenses = {}
    for expense in data["expenses"]:
        cat = expense["category"]
        monthly_expenses[cat] = monthly_expenses.get(cat, 0) + expense["amount"]
    for cat, budget in data["budgets"].items():
        spent = monthly_expenses.get(cat, 0)
        print(f"{cat}: Budget = {budget}, Spent = {spent}, Remaining = {budget - spent}")
    print("=======================")

def main():
    data = load_data()
    while True:
        print("\n1. Add Income\n2. Add Expense\n3. Set Budget\n4. Show Summary\n5. Save & Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            set_budget(data)
        elif choice == "4":
            show_summary(data)
        elif choice == "5":
            save_data(data)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
