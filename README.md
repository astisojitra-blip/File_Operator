# 📔 Personal Journal Manager

### 👨‍💻 Created By: Asti Sojitra

A simple command-line based **Personal Journal Manager** built with Python. This project allows users to create, add, view, search, and delete journal entries using a text file.

## ✨ Features

- 📝 Add a new journal entry
- 📖 View all saved journal entries
- 🔍 Search entries by keyword or date
- 🗑️ Delete all journal entries
- 📅 Automatically records the date and time of each entry
- 💾 Stores journal entries in a text file
- ⚠️ Handles common file-related errors using exception handling
- 📋 Simple interactive menu-based interface

## 🛠️ Technologies Used

- Python 
- `datetime` module
- File Handling
- Object-Oriented Programming (OOP)
- Exception Handling
- User Input

## 📂 Project Structure

```text
Personal-Journal-Manager/
│
├── journal.py
├── journal.txt
└── README.md
```

> `journal.txt` is created automatically when the first journal entry is added.



## 💻 How to Use

When you run the program, you will see the following menu:

```text
Welcome to Personal Journal Manager...

Please select an option
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

### 1️⃣ Add a New Entry

Select option `1` and enter your journal entry.

```text
Enter your journal entry: Today I learned Python file handling.

Journal entry added successfully!
```

The entry is automatically saved with the current date and time.

Example:

```text
[2026-10-02 21:00:00]
Today I learned Python file handling.
```

### 2️⃣ View All Entries

Select option `2` to display all saved journal entries.

```text
Your Journal Entries:
-------------------------------
[2026-10-02 21:00:00]
Today I learned Python file handling.
```

### 3️⃣ Search for an Entry

Select option `3` and enter a keyword or date.

```text
Enter a keyword or date to search: Python

Matching Entries:
-------------------------------
[2026-10-02 21:00:00]
Today I learned Python file handling.
```

### 4️⃣ Delete All Entries

Select option `4` to delete all saved journal entries.

The program asks for confirmation:

```text
Are you sure you want to delete all entries? (yes/no):
```

If you enter `yes`, all existing journal entries will be removed.

### 5️⃣ Exit

Select option `5` to exit the application.

```text
Thank you for using Journal Manager. Goodbye!
```

## 🧠 Concepts Covered

This project demonstrates several important Python concepts.

### Object-Oriented Programming

The project uses a `JournalManager` class to organize journal-related operations.

```python
class JournalManager:
```

### Constructor

The `__init__()` method is used to set the journal file name.

```python
def __init__(self, filename="journal.txt"):
    self.filename = filename
```

### File Handling

The project uses Python's `open()` function to create, read, append, and modify the journal file.

```python
with open(self.filename, "a") as file:
    file.write(...)
```

### Date and Time

The `datetime` module is used to automatically record the date and time.

```python
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

### Exception Handling

The program handles common file-related errors such as:

- `FileNotFoundError`
- `PermissionError`
- `FileExistsError`

This helps prevent the program from crashing when a file-related error occurs.

## 📌 Main Methods

| Method | Description |
|---|---|
| `create_file()` | Creates the journal file if it does not exist |
| `add_entry()` | Adds a new journal entry with date and time |
| `view_entry()` | Displays all journal entries |
| `search_entry()` | Searches entries using a keyword or date |
| `delete_entry()` | Deletes all journal entries |

## 📚 Learning Outcomes

This project helped in understanding:

- Python classes and objects
- Object-Oriented Programming
- File handling
- Reading and writing text files
- Exception handling
- Working with date and time
- Functions and methods
- Loops and conditional statements
- Building a menu-driven Python application



## 👨‍💻 Author

Asti Sojitra

## License

Created as a Python practice project to learn **Object-Oriented Programming, File Handling, Date & Time, and Exception Handling**.

---

⭐ If you found this project useful, feel free to star the repository!
