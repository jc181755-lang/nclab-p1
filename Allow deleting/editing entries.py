import json
import os
from datetime import datetime

# -----------------------------
# Optional color support (works without extra installs)
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

# ---------- helpers ----------
def safe_float(prompt, default=None):
    while True:
        raw = input(prompt)
        if raw == "" and default is not None:
            return default
        try:
            return float(raw)
        except ValueError:
            print(c("Please enter a valid number.", YELLOW))

def safe_date(prompt, default=None):
    raw = input(prompt)
    if raw.strip() == "":
        return default or datetime.today().strftime("%Y-%m-%d")
    # very light validation (YYYY-MM-DD)
    try:
        datetime.strptime(raw, "%Y-%m-%d")
        return raw
    except ValueError:
        print(c("Invalid date format. Use YYYY-MM-DD. Using default/today.", YELLOW))
        return default or datetime.today().strftime("%Y-%m-%d")

def choose_index(items, title="Select item"):
    if not items:
        print(c("Nothing to select.", YELLOW))
        return None
    print(c(f"\n{title}", BOLD))
    for i, it in enumerate(items):
        print(f"[{i}] {it}")
    while True:
        raw = input("Enter index (or blank to cancel): ").strip()
        if raw == "":
            print(c("Cancelled.", YELLOW))
            return None
        if raw.isdigit():
            idx = int(raw)
            if 0 <= idx < len(items):
                return idx
        print(c("Invalid index. Try again.", YELLOW))

# ---------- add ----------
def add_income(data):
    amount = safe_float("Enter income amount: ")
    source = input("Source/Description: ")
    date = safe_date("Date (YYYY-MM-DD, blank for today): ")
    data["income"].append({"amount": amount, "source": source, "date": date})
    print(c("Income recorded.", GREEN))

def add_expense(data):
    amount = safe_float("Enter expense amount: ")
    category = input("Category (e.g., Food, Rent, Entertainment): ")
    desc = input("Description: ")
    date = safe_date("Date (YYYY-MM-DD, blank for today): ")
    data["expenses"].append({"amount": amount, "category": category, "desc": desc, "date": date})
    print(c("Expense recorded.", GREEN))

def set_budget(data):
    category = input("Set budget for category: ")
    amount = safe_float(f"Enter monthly budget for {category}: ")
    data["budgets"][category] = amount
    print(c(f"Budget for {category} set to {amount}.", GREEN))

# ---------- edit/delete income ----------
def list_income_lines(data):
    lines = []
    for i, inc in enumerate(data.get("income", [])):
        lines.append(f"[{i}] {inc.get('date','')} | ${inc.get('amount',0):.2f} | {inc.get('source','')}")
    return lines

def edit_income(data):
    lines = list_income_lines(data)
    idx = choose_index(lines, "Edit Income Entry")
    if idx is None: 
        return
    inc = data["income"][idx]
    print(c(f"Editing income #{idx}", BOLD))
    print(f"Current amount: {inc['amount']}")
    new_amount = safe_float("New amount (Enter to keep): ", default=float(inc["amount"]))
    print(f"Current source: {inc['source']}")
    new_source = input("New source/description (Enter to keep): ").strip() or inc["source"]
    print(f"Current date: {inc['date']}")
    new_date = safe_date("New date YYYY-MM-DD (Enter to keep): ", default=inc["date"])
    inc.update({"amount": new_amount, "source": new_source, "date": new_date})
    print(c("Income updated.", GREEN))

def delete_income(data):
    lines = list_income_lines(data)
    idx = choose_index(lines, "Delete Income Entry")
    if idx is None:
        return
    print(c(f"Deleting: {lines[idx]}", YELLOW))
    sure = input("Type 'yes' to confirm: ").strip().lower()
    if sure == "yes":
        del data["income"][idx]
        print(c("Income entry deleted.", GREEN))
    else:
        print(c("Deletion cancelled.", YELLOW))

# ---------- edit/delete expense ----------
def list_expense_lines(data):
    lines = []
    for i, ex in enumerate(data.get("expenses", [])):
        lines.append(
            f"[{i}] {ex.get('date','')} | ${ex.get('amount',0):.2f} | {ex.get('category','')} | {ex.get('desc','')}"
        )
    return lines

def edit_expense(data):
    lines = list_expense_lines(data)
    idx = choose_index(lines, "Edit Expense Entry")
    if idx is None:
        return
    ex = data["expenses"][idx]
    print(c(f"Editing expense #{idx}", BOLD))
    print(f"Current amount: {ex['amount']}")
    new_amount = safe_float("New amount (Enter to keep): ", default=float(ex["amount"]))
    print(f"Current category: {ex['category']}")
    new_cat = input("New category (Enter to keep): ").strip() or ex["category"]
    print(f"Current description: {ex['desc']}")
    new_desc = input("New description (Enter to keep): ").strip() or ex["desc"]
    print(f"Current date: {ex['date']}")
    new_date = safe_date("New date YYYY-MM-DD (Enter to keep): ", default=ex["date"])
    ex.update({"amount": new_amount, "category": new_cat, "desc": new_desc, "date": new_date})
    print(c("Expense updated.", GREEN))

def delete_expense(data):
    lines = list_expense_lines(data)
    idx = choose_index(lines, "Delete Expense Entry")
    if idx is None:
        return
    print(c(f"Deleting: {lines[idx]}", YELLOW))
    sure = input("Type 'yes' to confirm: ").strip().lower()
    if sure == "yes":
        del data["expenses"][idx]
        print(c("Expense entry deleted.", GREEN))
    else:
        print(c("Deletion cancelled.", YELLOW))

# ---------- summary ----------
def show_summary(data):
    print("\n" + c("==== Budget Summary ====", BOLD))

    # totals
    total_income = sum(float(i.get("amount", 0)) for i in data.get("income", []))
    total_expenses = sum(float(e.get("amount", 0)) for e in data.get("expenses", []))
    net_savings = total_income - total_expenses

    # aggregate expenses by category
    spent_by_cat = {}
    for e in data.get("expenses", []):
        cat = e.get("category", "Uncategorized")
        amt = float(e.get("amount", 0))
        spent_by_cat[cat] = spent_by_cat.get(cat, 0.0) + amt

    # header
    header = f"{'Category':<18} {'Budget':>12} {'Spent':>12} {'Remaining':>12} {'% Used':>9}"
    print(c(header, BOLD))
    print("-" * 65)

    # categories with budget
    for cat, budget in data.get("budgets", {}).items():
        budget = float(budget)
        spent = float(spent_by_cat.get(cat, 0.0))
        remaining = budget - spent
        pct_used = (spent / budget * 100.0) if budget else 0.0

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
    print(f"{'TOTAL INCOME':<18} {total_income:>12.2f}")
    print(f"{'TOTAL EXPENSES':<18} {total_expenses:>12.2f}")
    net_str = c(f"{net_savings:>12.2f}", GREEN if net_savings >= 0 else RED)
    print(f"{'NET SAVINGS':<18} {net_str}")
    print("=" * 65)

# ---------- main ----------
def main():
    data = load_data()
    while True:
        print("\n" + c("Budget Tracker Menu", BOLD))
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Budget")
        print("4. Show Summary")
        print("5. Save & Exit")
        print("6. Edit Income")
        print("7. Delete Income")
        print("8. Edit Expense")
        print("9. Delete Expense")

        choice = input("Choose an option: ").strip()
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
        elif choice == "6":
            edit_income(data)
        elif choice == "7":
            delete_income(data)
        elif choice == "8":
            edit_expense(data)
        elif choice == "9":
            delete_expense(data)
        else:
            print(c("Invalid choice. Try again.", YELLOW))

if __name__ == "__main__":
    main()
