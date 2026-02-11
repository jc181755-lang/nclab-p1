# nclab-p1
Personal Budget Expense Tracker project.

###Hi there in Jonathan aka entry level pyhton dev. 

##Hi im a husband, father, developer and a teacher.

# 💰 Personal Budget & Expense Tracker (CLI)

A **Python 3 command-line application** that helps users track income, expenses, and category-based budgets with persistent local storage. Designed for simplicity, clarity, and expandability, this project demonstrates real-world Python application flow and data handling.

---

## 🚀 Features

* ✅ Persistent JSON data storage (no data loss between sessions)
* ➕ Add income entries
* ➖ Add expense entries
* 🎯 Set monthly budgets by category
* 📊 Color-coded summary showing:

  * Budget per category
  * Amount spent
  * Remaining balance
  * Percentage of budget used
* 🧠 Smart defaults (auto-fills today’s date when left blank)
* 🛡 Defensive input validation and error handling
* 🧩 Modular, easy-to-extend codebase

---

## 🧩 Example Walkthrough

1. Start the program
2. Add income (e.g., **$1500 – Paycheck**)
3. Add an expense (e.g., **$200 – Food**)
4. Set a budget for **Food** (e.g., **$300**)
5. View summary → see remaining balance and % used
6. Save & Exit → data persists in JSON

---

## 📂 Data Storage

All data is stored locally in a file named:

```
budget_data.json
```

If the file does not exist, it is automatically created on first run.

### Stored Data Structure

* **Income**: amount, source, date
* **Expenses**: amount, category, description, date
* **Budgets**: monthly limit per category

---

## 🧭 Menu Options

1. Add Income
2. Add Expense
3. Set Budget
4. Show Summary
5. Save & Exit

Invalid selections are handled safely with user-friendly prompts.

---

## 🖼 Screenshots

---

## 🛠 Tech Stack

* **Language:** Python 3
* **Libraries:** `json`, `os`, `datetime`
* **Optional:** `colorama` (for enhanced color support; not required)
* **Architecture:** Modular procedural design
* **Data Format:** JSON

---

## ▶️ How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/jc181755-lang/budget-tracker.git
   cd budget-tracker
   ```

2. (Optional) Install color support:

   ```bash
   pip install colorama
   ```

3. Run the application:

   ```bash
   main code
   ```

---

## 🏆 Achievements

* ✔ Reliable data persistence between sessions
* ✔ Clean, color-coded CLI summary output
* ✔ User-friendly input handling with defaults
* ✔ Expandable structure for future features

---

## 🔮 Future Enhancements

* Monthly income vs. expense reports
* Savings calculations
* CSV / Excel export
* Automatic monthly budget reset
* Tkinter GUI version
* Charts and visualizations (Matplotlib)

---

## 🧑‍💻 Author

**Jonathan Cordova**
GitHub: [@jc181755-lang](https://github.com/jc181755-lang)
NCLAB Python Developer | Personal Project | 2025

---

## 📌 About

This project demonstrates strong Python fundamentals, practical CLI user interface design, and real-world data persistence techniques.

