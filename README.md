Name : Asti Sojitra

Project Title : File Operator

A Personal Journal Manager built using Python to demonstrate the practical implementation of File Handling, Exception Handling, and Object-Oriented Programming (OOP) concepts.

📌 Project Overview

File Operator is a simple command-line based Personal Journal Manager developed in Python.

The application allows users to:

Add new journal entries

View all saved journal entries

Search entries using a keyword or date

Delete all journal entries

Handle common file-related errors using exception handling

The project stores journal entries in a text file named journal.txt.

This project is designed to demonstrate how Python file operations and OOP concepts can be combined to build a simple real-world application.

🚀 Features

1. Add a New Entry

Users can enter a journal entry, and the application automatically records the current date and time.

Example:

[2026-10-02 20:30:15]
Today I learned about file handling in Python.

2. View All Entries

Displays all journal entries stored in the journal.txt file.

3. Search for an Entry

Users can search for an entry using:

A keyword

A date

A phrase contained in the journal entry

4. Delete All Entries

Users can delete all stored journal entries after confirmation.

5. Exception Handling

The application handles common file-related exceptions such as:

FileNotFoundError

PermissionError

FileExistsError

This prevents the program from crashing when common file errors occur.

🧠 Concepts Used

This project demonstrates the following Python concepts:

🔹 Object-Oriented Programming (OOP)

The project uses a class called JournalManager.

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

The class contains methods for different journal operations:

create_file()

add_entry()

view_entry()

search_entry()

delete_entry()

This follows the basic principles of encapsulation by keeping journal-related data and operations inside the JournalManager class.

🔹 File Handling

Python file handling is used to create, read, append, and modify the journal file.

The project uses different file modes:

Mode

Purpose

x

Creates a new file

a

Adds new entries to the file

r

Reads existing entries

w

Clears the file

Example:

with open(self.filename, "a") as file:
    file.write(f"[{date}]\n")
    file.write(f"{title}\n")

The with open() statement is used so that files are properly closed after the operation.

🔹 Exception Handling

The project uses try-except blocks to handle possible runtime errors.

Example:

try:
    with open(self.filename, "r") as file:
        data = file.read()

except FileNotFoundError:
    print("The journal file does not exist.")

except PermissionError:
    print("Error: You do not have permission to read.")

This makes the application more reliable and user-friendly.

🔹 Date and Time Handling

The datetime module is used to automatically record the date and time when a journal entry is created.

from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

🛠️ Technologies Used

Python 

File Handling

Exception Handling

Object-Oriented Programming

datetime module

No external libraries are required.

📂 Project Structure

File-Operator/
│
├── journal_manager.py
├── journal.txt
└── README.md

journal.txt is created automatically when the first journal entry is added.

📋 Main Menu

When the program starts, the following menu is displayed:

Welcome to Personal Journal Manager
Please select an option

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

The user can select an option by entering a number from 1 to 5.

💡 Sample Usage

Adding an Entry

Enter your journal entry: Today I practiced Python file handling.

Journal entry added successfully!

Viewing Entries

Your Journal Entries:
-------------------------------
[2026-10-02 20:30:15]
Today I practiced Python file handling.

Searching Entries

Enter a keyword or date to search: Python

Matching Entries:
-------------------------------
[2026-10-02 20:30:15]
Today I practiced Python file handling.

Deleting Entries

Are you sure you want to delete all entries? (yes/no): yes

All journal entries have been deleted.

🎯 Project Objectives

The main objectives of this project are:

To understand Python file handling

To practice different file modes

To implement exception handling

To understand classes and objects

To organize functionality using methods

To build a simple real-world command-line application

To improve problem-solving and Python programming skills

🔐 Error Handling

The application handles several possible errors:

Exception

Purpose

FileExistsError

Handles the situation when the journal file already exists

FileNotFoundError

Handles attempts to access a missing journal file

PermissionError

Handles insufficient file permissions

👨‍💻 Author

Asti SOjitra

Python Project — File Operator

📄 License

This project is created for educational purposes and can be modified or extended for learning and personal use.
