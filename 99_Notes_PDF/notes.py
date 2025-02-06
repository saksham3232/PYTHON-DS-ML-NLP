from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import sqlite3
import shutil

# Create a PDF document
pdf_file = "10-SQLite3_Assignments_Report.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a list to hold the content
content = []

# Title
title_style = ParagraphStyle(name='TitleStyle', fontSize=24, spaceAfter=12)
content.append(Paragraph("SQLite3 Assignments Report", title_style))
content.append(Spacer(1, 12))

# Introduction
intro_style = ParagraphStyle(name='IntroStyle', fontSize=12, spaceAfter=12)
content.append(Paragraph("This report covers various assignments related to SQLite3 database operations using Python. Each assignment includes code snippets and explanations.", intro_style))
content.append(Spacer(1, 12))

# Code style for code snippets
code_style = ParagraphStyle(name='CodeStyle', fontName='Courier', fontSize=10, spaceAfter=12)

# Assignment 1
content.append(Paragraph("Assignment 1: Creating and Connecting to a Database", title_style))
content.append(Spacer(1, 12))

# Task 1.1
task1_code = [
    "import sqlite3",
    "",
    "# Function to create a new SQLite3 database named 'test.db'.",
    "def create_database():",
    "    conn = sqlite3.connect('test.db')",
    "    conn.close()",
    "    print('Database created and successfully connected.')",
    "",
    "# Test the function",
    "create_database()"
]
for line in task1_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function creates a new SQLite3 database named 'test.db' and connects to it.", intro_style))
content.append(Spacer(1, 12))

# Task 1.2
task1_2_code = [
    "# Function to create a table named 'employees'.",
    "def create_table():",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    cursor.execute('''",
    "        CREATE TABLE IF NOT EXISTS employees (",
    "            id INTEGER PRIMARY KEY,",
    "            name TEXT NOT NULL,",
    "            age INTEGER,",
    "            department TEXT",
    "        )",
    "    ''')",
    "    conn.commit()",
    "    conn.close()",
    "    print(\"Table 'employees' created successfully.\")",
    "",
    "# Test the function",
    "create_table()"
]
for line in task1_2_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function creates a table named 'employees' with specified columns.", intro_style))
content.append(Spacer(1, 12))

# Assignment 2
content.append(Paragraph("Assignment 2: Inserting Data", title_style))
content.append(Spacer(1, 12))

# Task 2.1
task2_code = [
    "# Function to insert a new employee into the 'employees' table.",
    "def insert_employee(id, name, age, department):",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    cursor.execute('''",
    "        INSERT INTO employees (id, name, age, department)",
    "        VALUES (?, ?, ?, ?)",
    "    ''', (id, name, age, department))",
    "    conn.commit()",
    "    conn.close()",
    "    print('Employee inserted successfully.')",
    "",
    "# Insert 5 different employees",
    "insert_employee(1, 'Alice', 30, 'HR')",
    "insert_employee(2, 'Bob', 25, 'Engineering')",
    "insert_employee(3, 'Charlie', 28, 'Sales')",
    "insert_employee(4, 'David', 35, 'Marketing')",
    "insert_employee(5, 'Eve', 22, 'HR')"
]
for line in task2_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function inserts a new employee into the 'employees' table.", intro_style))
content.append(Spacer(1, 12))

# Task 2.2
task2_2_code = [
    "# Insert 5 different employees",
    "insert_employee(2, 'Bob', 25, 'Engineering')",
    "insert_employee(3, 'Charlie', 28, 'Sales')",
    "insert_employee(4, 'David', 35, 'Marketing')",
    "insert_employee(5, 'Eve', 22, 'HR')"
]
for line in task2_2_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This code snippet demonstrates inserting multiple employees into the table.", intro_style))
content.append(Spacer(1, 12))

# Assignment 3
content.append(Paragraph("Assignment 3: Querying Data", title_style))
content.append(Spacer(1, 12))

# Task 3.1
task3_code = [
    "# Function to fetch and display all records from the 'employees' table.",
    "def fetch_all_employees():",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    cursor.execute('SELECT * FROM employees')",
    "    rows = cursor.fetchall()",
    "    conn.close()",
    "    for row in rows:",
    "        print(row)",
    "",
    "# Test the function",
    "fetch_all_employees()"
]
for line in task3_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function fetches and displays all records from the 'employees' table.", intro_style))
content.append(Spacer(1, 12))

# Task 3.2
task3_2_code = [
    "# Function to fetch and display all employees from a specific department.",
    "def fetch_employees_by_department(department):",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    cursor.execute('SELECT * FROM employees WHERE department = ?', (department,))",
    "    records = cursor.fetchall()",
    "    conn.close()",
    "    for record in records:",
    "        print(record)",
    "",
    "# Test the function",
    "fetch_employees_by_department('HR')"
]
for line in task3_2_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function fetches and displays employees from a specified department.", intro_style))
content.append(Spacer(1, 12))

# Assignment 4
content.append(Paragraph("Assignment 4: Updating Data", title_style))
content.append(Spacer(1, 12))

# Task 4.1
task4_code = [
    "# Function to update the department of an employee based on their ID.",
    "def update_employee_department(employee_id, new_department):",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    cursor.execute('''",
    "        UPDATE employees",
    "        SET department = ?",
    "        WHERE id = ?",
    "    ''', (new_department, employee_id))",
    "    conn.commit()",
    "    conn.close()",
    "    print('Employee department updated successfully.')",
    "",
    "# Test the function",
    "update_employee_department(1, 'Finance')"
]
for line in task4_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function updates the department of an employee based on their ID.", intro_style))
content.append(Spacer(1, 12))

# Task 4.2
task4_2_code = [
    "# Update the department of 2 employees",
    "update_employee_department(2, 'Research')",
    "update_employee_department(3, 'Customer Support')",
    "",
    "# Fetch and display all records",
    "fetch_all_employees()"
]
for line in task4_2_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This code updates the departments of two employees and fetches all records to display the changes.", intro_style))
content.append(Spacer(1, 12))

# Assignment 5
content.append(Paragraph("Assignment 5: Deleting Data", title_style))
content.append(Spacer(1, 12))

# Task 5.1
task5_code = [
    "# Function to delete an employee from the 'employees' table based on their ID.",
    "def delete_employee(employee_id):",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    cursor.execute('''",
    "        DELETE FROM employees",
    "        WHERE id = ?",
    "    ''', (employee_id,))",
    "    conn.commit()",
    "    conn.close()",
    "    print('Employee deleted successfully.')",
    "",
    "# Test the function",
    "delete_employee(5)"
]
for line in task5_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function deletes an employee from the 'employees' table based on their ID.", intro_style))
content.append(Spacer(1, 12))

# Task 5.2
task5_2_code = [
    "# Delete an employee",
    "delete_employee(4)",
    "",
    "# Fetch and display all records",
    "fetch_all_employees()"
]
for line in task5_2_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This code deletes an employee and fetches all records to display the remaining employees.", intro_style))
content.append(Spacer(1, 12))

# Assignment 6
content.append(Paragraph("Assignment 6: Advanced Queries", title_style))
content.append(Spacer(1, 12))

# Task 6.1
task6_code = [
    "# Function to fetch and display employees older than a certain age.",
    "def fetch_employees_older_age(age):",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    cursor.execute('SELECT * FROM employees WHERE age > ?', (age,))",
    "    records = cursor.fetchall()",
    "    conn.close()",
    "    for record in records:",
    "        print(record)",
    "",
    "# Test the function",
    "fetch_employees_older_age(25)"
]
for line in task6_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function fetches and displays employees older than a specified age.", intro_style))
content.append(Spacer(1, 12))

# Task 6.2
task6_2_code = [
    "# Function to fetch and display employees whose names start with a specific letter.",
    "def fetch_employees_name_starts_with(letter):",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    cursor.execute('SELECT * FROM employees WHERE name LIKE ?', (letter + '%',))",
    "    records = cursor.fetchall()",
    "    conn.close()",
    "    for record in records:",
    "        print(record)",
    "",
    "# Test the function",
    "fetch_employees_name_starts_with('A')"
]
for line in task6_2_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function fetches and displays employees whose names start with a specified letter.", intro_style))
content.append(Spacer(1, 12))

# Assignment 7
content.append(Paragraph("Assignment 7: Handling Transactions", title_style))
content.append(Spacer(1, 12))

# Task 7.1
task7_code = [
    "# Function to insert multiple employees into the 'employees' table in a single transaction.",
    "def insert_multiple_employees(employees):",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    try:",
    "        cursor.executemany('''",
    "            INSERT INTO employees (id, name, age, department)",
    "            VALUES (?, ?, ?, ?)",
    "        ''', employees)",
    "        conn.commit()",
    "        print('All employees inserted successfully.')",
    "    except Exception as e:",
    "        conn.rollback()",
    "        print('Error occurred, transaction rolled back.')",
    "        print(e)",
    "    finally:",
    "        conn.close()",
    "",
    "# Test the function with valid and invalid data",
    "employees = [",
    "    (6, 'Frank', 40, 'Finance'),",
    "    (7, 'Grace', 29, 'Engineering'),",
    "    (8, 'Hannah', 35, 'Marketing'),",
    "    (9, 'Ivan', 38, 'Sales'),",
    "    (6, 'Jack', 45, 'HR')  # Duplicate ID to cause an error",
    "]",
    "insert_multiple_employees(employees)"
]
for line in task7_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function inserts multiple employees in a single transaction, rolling back if any insertion fails.", intro_style))
content.append(Spacer(1, 12))

# Task 7.2
task7_2_code = [
    "# Function to update the ages of multiple employees in a single transaction.",
    "def update_multiple_employees_ages(updates):",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    try:",
    "        cursor.executemany('''",
    "            UPDATE employees",
    "            SET age = ?",
    "            WHERE id = ?",
    "        ''', updates)",
    "        conn.commit()",
    "        print('All employee ages updated successfully.')",
    "    except Exception as e:",
    "        conn.rollback()",
    "        print('Error occurred, transaction rolled back.')",
    "        print(e)",
    "    finally:",
    "        conn.close()",
    "",
    "# Test the function with valid and invalid data",
    "updates = [",
    "    (32, 1),",
    "    (26, 2),",
    "    (33, 3),",
    "    (41, 19),  # Non-existing ID to cause an error",
    "    (23, 5)",
    "]",
    "update_multiple_employees_ages(updates)"
]
for line in task7_2_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function updates the ages of multiple employees in a single transaction, rolling back if any update fails.", intro_style))
content.append(Spacer(1, 12))

# Assignment 8
content.append(Paragraph("Assignment 8: Creating Relationships", title_style))
content.append(Spacer(1, 12))

# Task 8.1
task8_code = [
    "# Function to create a new table named 'departments'.",
    "def create_departments_table():",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    cursor.execute('''",
    "        CREATE TABLE IF NOT EXISTS departments (",
    "            id INTEGER PRIMARY KEY,",
    "            name TEXT NOT NULL",
    "        )",
    "    ''')",
    "    conn.commit()",
    "    conn.close()",
    "    print(\"Table 'departments' created successfully.\")",
    "",
    "# Test the function",
    "create_departments_table()"
]
for line in task8_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function creates a new table named 'departments' with columns for ID and name.", intro_style))
content.append(Spacer(1, 12))

# Task 8.2
task8_2_code = [
    "# Function to modify the 'employees' table to include a foreign key referencing the 'departments' table.",
    "def add_department_foreign_key():",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "",
    "    # Disable foreign keys temporarily",
    "    cursor.execute(\"PRAGMA foreign_keys=off;\")",
    "    conn.commit()",
    "    # Start transaction",
    "    cursor.execute(\"BEGIN TRANSACTION;\")",
    "    # Rename old table",
    "    cursor.execute(\"ALTER TABLE employees RENAME TO old_employees;\")",
    "    # Create new table with foreign key",
    "    cursor.execute('''",
    "        CREATE TABLE employees (",
    "            id INTEGER PRIMARY KEY,",
    "            name TEXT NOT NULL,",
    "            age INTEGER,",
    "            department TEXT,",
    "            department_id INTEGER,",
    "            FOREIGN KEY(department_id) REFERENCES departments(id)",
    "        );",
    "    ''')",
    "    # Copy data, ensuring department_id is handled properly",
    "    cursor.execute('''",
    "        INSERT INTO employees (id, name, age, department, department_id)",
    "        SELECT id, name, age, department, NULL FROM old_employees;",
    "    ''')",
    "    # Drop old table",
    "    cursor.execute(\"DROP TABLE old_employees;\")",
    "    # Commit transaction",
    "    conn.commit()",
    "    # Re-enable foreign keys",
    "    cursor.execute(\"PRAGMA foreign_keys=on;\")",
    "    conn.commit()",
    "    conn.close()",
    "    print(\"Table 'employees' modified successfully.\")",
    "",
    "# Test the function",
    "add_department_foreign_key()"
]
for line in task8_2_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function modifies the 'employees' table to include a foreign key that references the 'departments' table.", intro_style))
content.append(Spacer(1, 12))

# Task 8.3
task8_3_code = [
    "# Function to insert data into both the 'departments' and 'employees' tables, ensuring referential integrity.",
    "def insert_department_and_employee(department_id, department_name, employee_id, name, age, department):",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    try:",
    "        cursor.execute('''",
    "            INSERT INTO departments (id, name)",
    "            VALUES (?, ?)",
    "        ''', (department_id, department_name))",
    "        cursor.execute('''",
    "            INSERT INTO employees (id, name, age, department, department_id)",
    "            VALUES (?, ?, ?, ?, ?)",
    "        ''', (employee_id, name, age, department, department_id))",
    "        conn.commit()",
    "        print(\"Department and employee inserted successfully.\")",
    "    except Exception as e:",
    "        conn.rollback()",
    "        print('Error occurred, transaction rolled back.')",
    "        print(e)",
    "    finally:",
    "        conn.close()",
    "",
    "# Test the function",
    "insert_department_and_employee(1, 'HR', 10, 'Alice', 30, 'HR')"
]
for line in task8_3_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function inserts data into both the 'departments' and 'employees' tables, ensuring referential integrity.", intro_style))
content.append(Spacer(1, 12))


# Assignment 9
content.append(Paragraph("Assignment 9: Indexing and Optimization", title_style))
content.append(Spacer(1, 12))

# Task 9.1
task9_1_code = [
    "# Function to create an index on the 'name' column of the 'employees' table.",
    "def create_index_on_name():",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    cursor.execute('CREATE INDEX idx_name ON employees(name)')",
    "    conn.commit()",
    "    conn.close()",
    "    print(\"Index on 'name' column created successfully.\")",
    "",
    "# Test the function",
    "create_index_on_name()"
]
for line in task9_1_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function creates an index on the 'name' column of the 'employees' table to optimize queries.", intro_style))
content.append(Spacer(1, 12))

# Task 9.2
task9_2_code = [
    "# Function to fetch employees whose names start with a specific letter and compare performance with and without the index.",
    "import time",
    "",
    "def fetch_employees_name_starts_with_performance(letter):",
    "    conn = sqlite3.connect('test.db')",
    "    cursor = conn.cursor()",
    "    start_time = time.time()",
    "    cursor.execute('SELECT * FROM employees WHERE name LIKE ?', (letter + '%',))",
    "    records = cursor.fetchall()",
    "    end_time = time.time()",
    "    conn.close()",
    "    print(\"Time taken: {} seconds\".format(end_time - start_time))",
    "    for record in records:",
    "        print(record)",
    "",
    "# Test the function with the index",
    "fetch_employees_name_starts_with_performance('A')"
]
for line in task9_2_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function fetches employees whose names start with a specified letter and measures the query performance.", intro_style))
content.append(Spacer(1, 12))

# Assignment 10
content.append(Paragraph("Assignment 10: Backing Up and Restoring Data", title_style))
content.append(Spacer(1, 12))

# Task 10.1
task10_1_code = [
    "# Function to back up the 'test.db' database to a file named 'backup.db'.",
    "import shutil",
    "",
    "def backup_database():",
    "    shutil.copy('test.db', 'backup.db')",
    "    print(\"Database backed up successfully.\")",
    "",
    "# Test the function",
    "backup_database()"
]
for line in task10_1_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function backs up the 'test.db' database to a file named 'backup.db'.", intro_style))
content.append(Spacer(1, 12))

# Task 10.2
task10_2_code = [
    "# Function to restore the 'test.db' database from the backup file 'backup.db'.",
    "def restore_database():",
    "    shutil.copy('backup.db', 'test.db')",
    "    print(\"Database restored successfully.\")",
    "",
    "# Test the function",
    "restore_database()"
]
for line in task10_2_code:
    content.append(Paragraph(line, style=code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("This function restores the 'test.db' database from the backup file 'backup.db'.", intro_style))
content.append(Spacer(1, 12))

# Build the PDF document
document.build(content)

print("PDF report generated successfully.")