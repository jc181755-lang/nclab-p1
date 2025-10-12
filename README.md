# nclab-p1

![jc181755-lang's GitHub stats](https://github-readme-stats.vercel.app/api?username=jc181755-lang&show_icons=true&theme=default)

Project Description — Personal Budget Tracker
Overview

🧩 Example Walkthrough

1️⃣ Start the program
2️⃣ Add income (e.g., $1500 Paycheck)
3️⃣ Add an expense (e.g., $200 Food)
4️⃣ Set a budget for Food ($300)
5️⃣ View summary → shows remaining balance and % used
6️⃣ Save & exit (data persists in JSON file)

Developed a command-line Personal Budget Tracker in Python that allows users to manage and monitor their personal finances in a 
simple, interactive way.

The application stores financial data locally, provides an easy-to-navigate menu system, and generates summaries of spending versus budgeted goals.

Core Features and Functionality

Data Management

Uses a JSON file (budget_data.json) for persistent data storage.

Automatically creates the file if it doesn’t exist.

Stores three key categories of data:

Income (amount, source, date)

Expenses (amount, category, description, date)

Budgets (monthly limit per category)

Here is an example on how the budget should look.

Adding Income and Expenses

Users can record income or expense entries interactively.

The app prompts for details such as:

Amount

Category/Source

Description

Date

If the date is left blank, the program automatically assigns today’s date using:

datetime.today().strftime("%Y-%m-%d")


This feature ensures usability and consistent record-keeping.

Setting Budgets

Users can define custom monthly budgets per expense category.

Budgets are stored persistently, allowing long-term tracking.

Summary Report

The show_summary() function displays a clear, text-based summary of:

Each category’s budget, total spent, and remaining balance.

Helps users quickly identify overspending or savings in specific areas.

Main Menu System

Offers an intuitive loop with five options:



🎥 Example video:
Screen Recording Demo

https://github.com/user-attachments/assets/3a785476-b247-4d0c-860d-1e52048c541b

Add Income

Add Expense

Set Budget

Show Summary 

ones you select 5 it show come up like this exaple.=

<img width="672" height="211" alt="Image" src="https://github.com/user-attachments/assets/0e4c7f4b-6107-47e1-afc8-281dfc184f56" />

Save & Exit

<img width="1366" height="181" alt="Image" src="https://github.com/user-attachments/assets/8499241b-ca00-4652-94eb-4d8ab532a8e5" />


Includes error handling for invalid input choices.

Technical Highlights

Language: Python 3

Libraries: json, os, datetime (no external dependencies)

Design Pattern: Modular procedural structure — each function handles a specific task.

Data Format: JSON (lightweight and easy to read/edit manually).

Approximate Lines of Code: ~140 lines

Achievements

Implemented reliable data persistence (no data loss between sessions).

Streamlined user input with sensible defaults (auto-date fill).

Designed an expandable structure that can later support visualization (e.g., charts or GUI).

Potential Future Enhancements

Add total income vs. total expenses summary and savings calculation.

Include percentage of budget spent per category.

Implement data export (CSV or Excel).

Create a Tkinter GUI version with charts using Matplotlib.

Add monthly reports and automatic reset of budgets.

Summary

Project demonstrates:

Strong understanding of Python fundamentals (functions, file I/O, conditionals, loops).

Practical application of data handling and user interface design (via CLI).

Good programming habits such as modularization, data validation, and persistence.

🧑‍💻 Author

Jonathan Cordova
GitHub: @jc181755-lang

NCLAB Python Developer | Personal Project | 2025
