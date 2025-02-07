from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted

# Create a PDF document
pdf_file = "9-sql_and_sqlite_guide.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Define styles
styles = getSampleStyleSheet()
normal_style = styles['Normal']
code_style = ParagraphStyle(
    'CodeStyle',
    parent=normal_style,
    fontName='Courier',
    fontSize=10,
    textColor=colors.black,
    spaceAfter=12,
)

# Content to be added to the PDF
content = []

# Title
content.append(Paragraph("SQL and SQLite: A Comprehensive Guide", styles['Title']))
content.append(Spacer(1, 12))

# Introduction
content.append(Paragraph("SQL (Structured Query Language) is a standard language for managing and manipulating relational databases. SQLite is a self-contained, serverless, and zero-configuration database engine that is widely used for embedded database systems. In this lesson, we will cover the basics of SQL and SQLite, including creating databases, tables, and performing various SQL operations.", normal_style))
content.append(Spacer(1, 12))

# Key Definitions
content.append(Paragraph("Key Definitions", styles['Heading2']))
content.append(Paragraph("SQL: A standard language for accessing and manipulating databases.", normal_style))
content.append(Paragraph("SQLite: A lightweight, serverless, self-contained SQL database engine.", normal_style))
content.append(Spacer(1, 12))

# Connecting to an SQLite Database
content.append(Paragraph("Connecting to an SQLite Database", styles['Heading2']))
connecting_code = """\
import sqlite3

# Connect to an SQLite database
connection = sqlite3.connect('example.db')
"""
content.append(Preformatted(connecting_code, code_style))
content.append(Paragraph("This code snippet demonstrates how to connect to an SQLite database using the sqlite3 module.", normal_style))
content.append(Paragraph("Key Definition: sqlite3.connect(database) - Establishes a connection to the SQLite database specified by 'database'.", normal_style))
content.append(Spacer(1, 12))

# Creating a Table
content.append(Paragraph("Creating a Table", styles['Heading2']))
creating_table_code = """\
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
''')
# Commit the changes
connection.commit()
"""
content.append(Preformatted(creating_table_code, code_style))
content.append(Paragraph("This snippet creates a table named 'employees' with columns for id, name, age, and department.", normal_style))
content.append(Paragraph("Key Definition: cursor.execute(sql) - Executes the SQL statement provided in 'sql'.", normal_style))
content.append(Paragraph("Key Definition: CREATE TABLE - Creates a new table in the database.", normal_style))
content.append(Paragraph("Key Definition: connection.commit() - Saves all changes made to the database.", normal_style))
content.append(Spacer(1, 12))

# Inserting Data
content.append(Paragraph("Inserting Data", styles['Heading2']))
inserting_data_code = """\
# Insert data into the employees table
cursor.execute('''
INSERT INTO employees(name, age, department)
VALUES('Krish', 32, 'Data Scientist')
''')
# Commit the changes
connection.commit()
"""
content.append(Preformatted(inserting_data_code, code_style))
content.append(Paragraph("This code inserts a new employee record into the 'employees' table.", normal_style))
content.append(Paragraph("Key Definition: INSERT INTO table_name (columns) VALUES (values) - Inserts a new record into the specified table.", normal_style))
content.append(Spacer(1, 12))

# Querying Data
content.append(Paragraph("Querying Data", styles['Heading2']))
querying_data_code = """\
# Query the data from the table
cursor.execute('SELECT * FROM employees')
rows = cursor.fetchall()
"""
content.append(Preformatted(querying_data_code, code_style))
content.append(Paragraph("This snippet retrieves all records from the 'employees' table.", normal_style))
content.append(Paragraph("Key Definition: SELECT * FROM table_name - Retrieves all records from the specified table.", normal_style))
content.append(Paragraph("Key Definition: fetchall() - Fetches all (remaining) rows of a query result, returning a list.", normal_style))
content.append(Spacer(1, 12))

# Updating Data
content.append(Paragraph("Updating Data", styles['Heading2']))
updating_data_code = """\
# Update the data in the table
cursor.execute('''
UPDATE employees
SET age = 34
WHERE name = 'Krish'
''')
# Commit the changes
connection.commit()
"""
content.append(Preformatted(updating_data_code, code_style))
content.append(Paragraph("This code updates the age of the employee named 'Krish'.", normal_style))
content.append(Paragraph("Key Definition: UPDATE table_name SET column = value WHERE condition - Updates existing records in the specified table based on a condition.", normal_style))
content.append(Spacer(1, 12))

# Deleting Data
content.append(Paragraph("Deleting Data", styles['Heading2']))
deleting_data_code = """\
# Delete the data from the table
cursor.execute('''
DELETE FROM employees
WHERE name = 'Bob'
''')
# Commit the changes
connection.commit()
"""
content.append(Preformatted(deleting_data_code, code_style))
content.append(Paragraph("This snippet deletes the record of the employee named 'Bob' from the table.", normal_style))
content.append(Paragraph("Key Definition: DELETE FROM table_name WHERE condition - Deletes records from the specified table based on a condition.", normal_style))
content.append(Spacer(1, 12))

# Working with Sales Data
content.append(Paragraph("Working with Sales Data", styles['Heading2']))
working_with_sales_code = """\
# Create a sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    product TEXT NOT NULL,
    sales INTEGER,
    region TEXT)
''')
# Commit the changes
connection.commit()
"""
content.append(Preformatted(working_with_sales_code, code_style))
content.append(Paragraph("This code creates a 'sales' table to store sales data.", normal_style))
content.append(Paragraph("Key Definition: CREATE TABLE IF NOT EXISTS table_name - Creates a new table if it does not already exist.", normal_style))
content.append(Spacer(1, 12))

# Inserting Sales Data
content.append(Paragraph("Inserting Sales Data", styles['Heading2']))
inserting_sales_data_code = """\
# Prepare sales data
sales_data = [
    ('2023-01-01', 'Product1', 100, 'North'),
    ('2023-01-02', 'Product2', 200, ' South'),
    ('2023-01-03', 'Product1', 150, 'East'),
    ('2023-01-04', 'Product3', 250 , 'West'),
    ('2023-01-05', 'Product2', 300, 'North')
]
# Insert multiple records into the sales table
cursor.executemany('''
INSERT INTO sales(date, product, sales, region)
VALUES(?, ?, ?, ?)
''', sales_data)
# Commit the changes
connection.commit()
"""
content.append(Preformatted(inserting_sales_data_code, code_style))
content.append(Paragraph("This code inserts multiple records into the 'sales' table using the executemany method.", normal_style))
content.append(Paragraph("Key Definition: executemany(sql, seq_of_params) - Executes the same SQL command for each parameter sequence in the provided list.", normal_style))
content.append(Spacer(1, 12))

# Querying Sales Data
content.append(Paragraph("Querying Sales Data", styles['Heading2']))
querying_sales_data_code = """\
# Query the sales data
cursor.execute('SELECT * FROM sales')
rows = cursor.fetchall()
"""
content.append(Preformatted(querying_sales_data_code, code_style))
content.append(Paragraph("This snippet retrieves all records from the 'sales' table.", normal_style))
content.append(Paragraph("Key Definition: SELECT * FROM table_name - Retrieves all records from the specified table.", normal_style))
content.append(Paragraph("Key Definition: fetchall() - Fetches all (remaining) rows of a query result, returning a list.", normal_style))
content.append(Spacer(1, 12))

# Closing the Database Connection
content.append(Paragraph("Closing the Database Connection", styles['Heading2']))
closing_connection_code = """\
# Close the database connection
connection.close()
"""
content.append(Preformatted(closing_connection_code, code_style))
content.append(Paragraph("This code closes the connection to the SQLite database, ensuring that all resources are released.", normal_style))
content.append(Paragraph("Key Definition: connection.close() - Closes the database connection.", normal_style))
content.append(Spacer(1, 12))

# References
content.append(Paragraph("References", styles['Heading2']))
content.append(Paragraph("1. SQLite Documentation: https://www.sqlite.org/docs.html", normal_style))
content.append(Paragraph("2. SQL Tutorial: https://www.w3schools.com/sql/", normal_style))

# Build the PDF
document.build(content)

print(f"PDF document '{pdf_file}' created successfully.")