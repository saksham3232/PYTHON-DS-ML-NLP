from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Define the PDF file name
pdf_file = "9-SQL_and_SQLite_Report.pdf"

# Create a PDF document
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a list to hold the content
content = []

# Define styles
styles = getSampleStyleSheet()
normal_style = styles['Normal']
heading_style = styles['Heading1']
subheading_style = styles['Heading2']

# Custom monospaced style for code snippets
code_style = ParagraphStyle(
    name='CodeStyle',
    fontName='Courier',
    fontSize=10,
    leading=12,
    spaceAfter=12,
)

# Title
content.append(Paragraph("SQL and SQLite: A Comprehensive Guide", heading_style))
content.append(Spacer(1, 12))

# Introduction
content.append(Paragraph("SQL (Structured Query Language) is a standard language for managing and manipulating relational databases. "
                         "SQLite is a self-contained, serverless, and zero-configuration database engine that is widely used for embedded database systems. "
                         "In this lesson, we will cover the basics of SQL and SQLite, including creating databases, tables, and performing various SQL operations.", normal_style))
content.append(Spacer(1, 12))

# Key Definitions
content.append(Paragraph("Key Definitions", subheading_style))
content.append(Paragraph("<b>SQL:</b> A standard language for accessing and manipulating databases.", normal_style))
content.append(Paragraph("<b>SQLite:</b> A lightweight, serverless, self-contained SQL database engine.", normal_style))
content.append(Spacer(1, 12))

# Section: Connecting to SQLite
content.append(Paragraph("Connecting to an SQLite Database", subheading_style))
code_lines_1 = [
    "import sqlite3",
    "",
    "# Connect to an SQLite database",
    "connection = sqlite3.connect('example.db')"
]
for line in code_lines_1:
    content.append(Paragraph(line, code_style))
content.append(Paragraph("This code snippet demonstrates how to connect to an SQLite database using the sqlite3 module.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("<b>Key Definition:</b> <i>sqlite3.connect(database)</i> - Establishes a connection to the SQLite database specified by 'database'.", normal_style))
content.append(Spacer(1, 12))

# Section: Creating a Table
content.append(Paragraph("Creating a Table", subheading_style))
code_lines_2 = [
    "cursor = connection.cursor()",
    "cursor.execute('''",
    "CREATE TABLE IF NOT EXISTS employees(",
    "    id INTEGER PRIMARY KEY,",
    "    name TEXT NOT NULL,",
    "    age INTEGER,",
    "    department TEXT",
    ")''')",
    "# Commit the changes",
    "connection.commit()"
]
for line in code_lines_2:
    content.append(Paragraph(line, code_style))
content.append(Paragraph("This snippet creates a table named 'employees' with columns for id, name, age, and department.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("<b>Key Definition:</b> <i>cursor.execute(sql)</i> - Executes the SQL statement provided in 'sql'.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("<b>Key Definition:</b> <i>connection.commit()</i> - Saves all changes made to the database.", normal_style))
content.append(Spacer(1, 12))

# Section: Inserting Data
content.append(Paragraph("Inserting Data", subheading_style))
code_lines_3 = [
    "# Insert data into the employees table",
    "cursor.execute('''",
    "INSERT INTO employees(name, age, department)",
    "VALUES('Krish', 32, 'Data Scientist')",
    "''')",
    "# Commit the changes",
    "connection.commit()"
]
for line in code_lines_3:
    content.append(Paragraph(line, code_style))
content.append(Paragraph("This code inserts a new employee record into the 'employees' table.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("<b>Key Definition:</b> <i>INSERT INTO table_name (columns) VALUES (values)</i> - Inserts a new record into the specified table.", normal_style))
content.append(Spacer(1, 12))

# Section: Querying Data
content.append(Paragraph("Querying Data", subheading_style))
code_lines_4 = [
    "# Query the data from the table",
    "cursor.execute('SELECT * FROM employees')",
    "rows = cursor.fetchall()"
]
for line in code_lines_4:
    content.append(Paragraph(line, code_style))
content.append(Paragraph("This snippet retrieves all records from the 'employees' table.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("<b>Key Definition:</b> <i>SELECT * FROM table_name</i> - Retrieves all records from the specified table.", normal_style))
content.append(Spacer(1, 12))

# Section: Updating Data
content.append(Paragraph("Updating Data", subheading_style))
code_lines_5 = [
    "# Update the data in the table",
    "cursor.execute('''",
    "UPDATE employees",
    "SET age = 34",
    "WHERE name = 'Krish'",
    "''')",
    "# Commit the changes",
    "connection.commit()"
]
for line in code_lines_5:
    content.append(Paragraph(line, code_style))
content.append(Paragraph("This code updates the age of the employee named 'Krish'.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("<b>Key Definition:</b> <i>UPDATE table_name SET column = value WHERE condition</i> - Updates existing records in the specified table based on a condition.", normal_style))
content.append(Spacer(1, 12))

# Section: Deleting Data
content.append(Paragraph("Deleting Data", subheading_style))
code_lines_6 = [
    "# Delete the data from the table",
    "cursor.execute('''",
    "DELETE FROM employees",
    "WHERE name = 'Bob'",
    "''')",
    "# Commit the changes",
    "connection.commit()"
]
for line in code_lines_6:
    content.append(Paragraph(line, code_style))
content.append(Paragraph("This snippet deletes the record of the employee named 'Bob' from the table.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("<b>Key Definition:</b> <i>DELETE FROM table_name WHERE condition</i> - Deletes records from the specified table based on a condition.", normal_style))
content.append(Spacer(1, 12))

# Section: Working with Sales Data
content.append(Paragraph("Working with Sales Data", subheading_style))
code_lines_7 = [
    "# Create a sales table",
    "cursor.execute('''",
    "CREATE TABLE IF NOT EXISTS sales(",
    "    id INTEGER PRIMARY KEY,",
    "    date TEXT NOT NULL,",
    "    product TEXT NOT NULL,",
    "    sales INTEGER,",
    "    region TEXT)",
    "''')",
    "# Commit the changes",
    "connection.commit()"
]
for line in code_lines_7:
    content.append(Paragraph(line, code_style))
content.append(Paragraph("This code creates a 'sales' table to store sales data.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("<b>Key Definition:</b> <i>CREATE TABLE IF NOT EXISTS table_name</i> - Creates a new table if it does not already exist.", normal_style))
content.append(Spacer(1, 12))

# Section: Inserting Sales Data
content.append(Paragraph("Inserting Sales Data", subheading_style))
code_lines_8 = [
    "# Prepare sales data",
    "sales_data = [",
    "    ('2023-01-01', 'Product1', 100, 'North'),",
    "    ('2023-01-02', 'Product2', 200, 'South'),",
    "    ('2023-01-03', 'Product1', 150, 'East'),",
    "    ('2023-01-04', 'Product3', 250, 'West'),",
    "    ('2023-01-05', 'Product2', 300, 'North')",
    "]",
    "# Insert multiple records into the sales table",
    "cursor.executemany('''",
    "INSERT INTO sales(date, product, sales, region)",
    "VALUES(?, ?, ?, ?)",
    "''', sales_data)",
    "# Commit the changes",
    "connection.commit()"
]
for line in code_lines_8:
    content.append(Paragraph(line, code_style))
content.append(Paragraph("This code inserts multiple records into the 'sales' table using the executemany method.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("<b>Key Definition:</b> <i>executemany(sql, seq_of_params)</i> - Executes the same SQL command for each parameter sequence in the provided list.", normal_style))
content.append(Spacer(1, 12))

# Section: Querying Sales Data
content.append(Paragraph("Querying Sales Data", subheading_style))
code_lines_9 = [
    "# Query the sales data",
    "cursor.execute('SELECT * FROM sales')",
    "rows = cursor.fetchall()"
]
for line in code_lines_9:
    content.append(Paragraph(line, code_style))
content.append(Paragraph("This snippet retrieves all records from the 'sales' table.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("<b>Key Definition:</b> <i>fetchall()</i> - Fetches all (remaining) rows of a query result, returning a list.", normal_style))
content.append(Spacer(1, 12))

# Closing the Connection
content.append(Paragraph("Closing the Database Connection", subheading_style))
code_lines_close = [
    "# Close the database connection",
    "connection.close()"
]
for line in code_lines_close:
    content.append(Paragraph(line, code_style))
content.append(Paragraph("This code closes the connection to the SQLite database, ensuring that all resources are released.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("<b>Key Definition:</b> <i>connection.close()</i> - Closes the database connection.", normal_style))
content.append(Spacer(1, 12))

# References
content.append(Paragraph("References", subheading_style))
content.append(Paragraph("1. SQLite Documentation: https://www.sqlite.org/docs.html", normal_style))
content.append(Paragraph("2. SQL Tutorial: https://www.w3schools.com/sql/", normal_style))

# Build the PDF
doc.build(content)

print(f"PDF report '{pdf_file}' has been generated successfully.")