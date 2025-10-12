import json
import os
from datetime import datetime

# -----------------------------
# Optional color support (works without extra installs)
# If 'colorama' is available, we'll use it to improve cross-platform behavior.
try:
    from colorama import init as colorama_init  # type: ignore
    colorama_init(autoreset=True)
except Exception:
    pass

# ANSI color codes (most Linux terminals support these)
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
CYAN = "\033[36m"

def c(text, color):
    """Wrap text in ANSI color escape codes."""
    return f"{color}{text}{RESET}"

# -----------------------------
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
    print(c("Income recorded.", GREEN))

def add_expense(data):
    amount = float(input("Enter expense amount: "))
    category = input("Category (e.g., Food, Rent, Entertainment): ")
    desc = input("Description: ")
    date = input("Date (YYYY-MM-DD, blank for today): ") or datetime.today().strftime("%Y-%m-%d")
    data["expenses"].append({"amount": amount, "category": category, "desc": desc, "date": date})
    print(c("Expense recorded.", GREEN))

def set_budget(data):
    category = input("Set budget for category: ")
    amount = float(input(f"Enter monthly budget for {category}: "))
    data["budgets"][category] = amount
    print(c(f"Budget for {category} set to {amount}.", GREEN))

def show_summary(data):
    print("\n" + c("==== Budget Summary ====", BOLD))

    # --- totals ---
    total_income = sum(float(i.get("amount", 0)) for i in data.get("income", []))
    total_expenses = sum(float(e.get("amount", 0)) for e in data.get("expenses", []))
    net_savings = total_income - total_expenses

    # --- aggregate expenses by category ---
    spent_by_cat = {}
    for e in data.get("expenses", []):
        cat = e.get("category", "Uncategorized")
        amt = float(e.get("amount", 0))
        spent_by_cat[cat] = spent_by_cat.get(cat, 0.0) + amt

    # header
    header = f"{'Category':<18} {'Budget':>12} {'Spent':>12} {'Remaining':>12} {'% Used':>9}"
    print(c(header, BOLD))
    print("-" * 65)

    # show all categories with a budget
    for cat, budget in data.get("budgets", {}).items():
        budget = float(budget)
        spent = float(spent_by_cat.get(cat, 0.0))
        remaining = budget - spent
        pct_used = (spent / budget * 100.0) if budget else 0.0

        # color logic for % used
        if budget == 0:
            pct_color = CYAN
        elif pct_used <= 80:
            pct_color = GREEN
        elif pct_used <= 100:
            pct_color = YELLOW
        else:
            pct_color = RED

        remaining_str = f"{remaining:>12.2f}"
        if remaining < 0:
            remaining_str = c(remaining_str, RED)
        elif remaining > 0 and pct_used <= 80:
            remaining_str = c(remaining_str, GREEN)

        line = (
            f"{cat:<18} "
            f"{budget:>12.2f} "
            f"{spent:>12.2f} "
            f"{remaining_str} "
            f"{c(f'{pct_used:>8.1f}%', pct_color)}"
        )
        print(line)

    # categories with spend but no budget
    for cat, spent in spent_by_cat.items():
        if cat not in data.get("budgets", {}):
            line = (
                f"{cat:<18} "
                f"{c('(no budget)', CYAN):>12} "
                f"{spent:>12.2f} "
                f"{'-':>12} "
                f"{'-':>9}"
            )
            print(line)

    print("-" * 65)

    # totals with color for net savings
    print(f"{'TOTAL INCOME':<18} {total_income:>12.2f}")
    print(f"{'TOTAL EXPENSES':<18} {total_expenses:>12.2f}")
    net_str = c(f"{net_savings:>12.2f}", GREEN if net_savings >= 0 else RED)
    print(f"{'NET SAVINGS':<18} {net_str}")
    print("=" * 65)

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
            print(c("Data saved. Goodbye!", GREEN))
            break
        else:
            print(c("Invalid choice. Try again.", YELLOW))

if __name__ == "__main__":
    main()

