# nclab-p1

![jc181755-lang's GitHub stats](https://github-readme-stats.vercel.app/api?username=jc181755-lang&show_icons=true&theme=default)

Project Description — Personal Budget Tracker
Overview

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

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/f19ce42e-5a64-44d1-a269-0cb88e2293c4" />

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

Add Income

Add Expense

Set Budget

Show Summary

Save & Exit

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
