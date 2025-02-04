from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.units import inch

# Define a function to convert newlines to <br/> for Paragraph rendering.
def convert_newlines(text):
    return text.replace("\n", "<br/>")

# Create a PDF document
pdf_filename = "Complete_Pandas_Report.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
styles = getSampleStyleSheet()

# Define custom styles
title_style = styles["Title"]
heading_style = styles["Heading2"]

# Define a custom code style using a monospaced font (Courier)
code_style = ParagraphStyle(
    "Code",
    parent=styles["Normal"],
    fontName="Courier",
    fontSize=9,
    textColor=colors.black,
    backColor=colors.whitesmoke,
    leading=12,
)

# Define a normal paragraph style (for explanations) that will also use Courier
normal_code_style = ParagraphStyle(
    "NormalCode",
    parent=styles["Normal"],
    fontName="Courier",
    fontSize=9,
    textColor=colors.black,
    leading=12,
)

# Start building the content list
content = []

# Add a title
content.append(Paragraph("Detailed Pandas Data Manipulation and ReportLab PDF Generation", title_style))
content.append(Spacer(1, 0.25 * inch))

# Section 1: Introduction
intro_text = """
This document contains a detailed explanation of various Pandas data manipulation operations 
and how to generate a PDF report using ReportLab. All code and outputs are displayed in a monospaced font.
References: <a href="https://pandas.pydata.org/pandas-docs/stable/">Pandas Documentation</a> and 
<a href="https://www.reportlab.com/documentation/">ReportLab User Guide</a>.
"""
content.append(Paragraph(convert_newlines(intro_text), normal_code_style))
content.append(Spacer(1, 0.2 * inch))

# Section 2: Reading Data with Pandas
content.append(Paragraph("1. Reading Data with Pandas", heading_style))
code_block = """
import pandas as pd
df = pd.read_csv('data.csv')
"""
explanation = """
# Explanation:
# - Imports the pandas library.
# - Reads a CSV file named 'data.csv' into a DataFrame 'df'.
# Expected output: DataFrame with data from 'data.csv'.
"""
content.append(Paragraph(convert_newlines(code_block + explanation), code_style))
content.append(Spacer(1, 0.2 * inch))

# Section 3: Fetching Data
content.append(Paragraph("2. Fetching Data (head, tail, describe, and dtypes)", heading_style))
code_block = """
# Fetch the first 5 rows
df.head(5)

# Fetch the last 5 rows
df.tail(5)

# Generate summary statistics for numeric columns
df.describe()

# Check data types of columns
df.dtypes
"""
explanation = """
# Explanation:
# - df.head(5) and df.tail(5) display the first and last 5 rows, respectively.
# - df.describe() provides summary statistics for numeric columns.
# - df.dtypes shows the data types for each column.
"""
content.append(Paragraph(convert_newlines(code_block + explanation), code_style))
content.append(Spacer(1, 0.2 * inch))

# Section 4: Handling Missing Values
content.append(Paragraph("3. Handling Missing Values", heading_style))
code_block = """
# Identify missing values in the DataFrame
df.isnull()

# Check if any column contains missing values
df.isnull().any()

# Count missing values per column
df.isnull().sum()

# Fill missing values with 0
df_filled = df.fillna(0)

# Fill missing values in 'Sales' with the column's mean and create a new column
df['Sales_fillNA'] = df['Sales'].fillna(df['Sales'].mean())
"""
explanation = """
# Explanation:
# - df.isnull() returns a DataFrame of booleans indicating missing values.
# - df.isnull().any() returns True/False for each column based on if any missing values exist.
# - df.isnull().sum() provides the total count of missing values per column.
# - df.fillna(0) fills all missing values with 0.
# - For the 'Sales' column, missing values are replaced with the column's mean.
"""
content.append(Paragraph(convert_newlines(code_block + explanation), code_style))
content.append(Spacer(1, 0.2 * inch))

# Section 5: Renaming Columns
content.append(Paragraph("4. Renaming Columns", heading_style))
code_block = """
# Rename the column 'Date' to 'Sales Date'
df = df.rename(columns={'Date': 'Sales Date'})
df.head()
"""
explanation = """
# Explanation:
# - The rename() method changes column names.
# - 'Date' is renamed to 'Sales Date', and df.head() displays the updated DataFrame.
"""
content.append(Paragraph(convert_newlines(code_block + explanation), code_style))
content.append(Spacer(1, 0.2 * inch))

# Section 6: Changing Data Types and Creating New Columns
content.append(Paragraph("5. Changing Data Types and Creating New Columns", heading_style))
code_block = """
# Replace missing values in 'Value' with its mean, convert to int, and create 'Value_New'
df['Value_New'] = df['Value'].fillna(df['Value'].mean()).astype(int)
df.head()

# Create a new column 'New Value' by doubling the 'Value'
df['New Value'] = df['Value'].apply(lambda x: x * 2)
df.head()
"""
explanation = """
# Explanation:
# - Missing values in 'Value' are replaced with the mean, then converted to integer for 'Value_New'.
# - A lambda function doubles each element in the 'Value' column for 'New Value'.
"""
content.append(Paragraph(convert_newlines(code_block + explanation), code_style))
content.append(Spacer(1, 0.2 * inch))

# Section 7: Data Aggregation and Grouping
content.append(Paragraph("6. Data Aggregation and Grouping", heading_style))
code_block = """
# Group by 'Product' and calculate the mean of 'Value'
grouped_mean = df.groupby('Product')['Value'].mean()
print(grouped_mean)
print(type(grouped_mean))

# Group by 'Product' and 'Region', then sum 'Value' and 'Sales'
grouped_sum = df.groupby(['Product', 'Region'])[['Value', 'Sales']].sum()
print(grouped_sum)

# Aggregate multiple functions (mean, sum, count) on 'Value' grouped by 'Region'
grouped_agg = df.groupby('Region')['Value'].agg(['mean', 'sum', 'count'])
grouped_agg
"""
explanation = """
# Explanation:
# - Grouping is performed using groupby().
# - The first grouping calculates the mean of 'Value' per 'Product'.
# - The second grouping calculates the sum of 'Value' and 'Sales' per 'Product' and 'Region'.
# - The last aggregation applies multiple functions on 'Value' for each 'Region'.
"""
content.append(Paragraph(convert_newlines(code_block + explanation), code_style))
content.append(Spacer(1, 0.2 * inch))

# Section 8: Merging and Joining DataFrames
content.append(Paragraph("7. Merging and Joining DataFrames", heading_style))
code_block = """
# Create two sample DataFrames for merging
df1 = pd.DataFrame({'Key': ['A', 'B', 'C'], 'Value1': [1, 2, 3]})
df2 = pd.DataFrame({'Key': ['A', 'B', 'D'], 'Value2': [4, 5, 6]})

# Display the DataFrames
print(df1)
print(df2)

# Merge DataFrames on the 'Key' column with different join types:
# Inner Join - only matching keys
pd.merge(df1, df2, on='Key', how='inner')

# Outer Join - all keys, fill missing with NaN
pd.merge(df1, df2, on='Key', how='outer')

# Left Join - all keys from df1
pd.merge(df1, df2, on='Key', how='left')

# Right Join - all keys from df2
pd.merge(df1, df2, on='Key', how='right')
"""
explanation = """
# Explanation:
# - Two DataFrames (df1 and df2) are created with a common 'Key' column.
# - Different merge strategies (inner, outer, left, right) are demonstrated.
# - The printed outputs show how rows are matched and non-matching entries are handled.
"""
content.append(Paragraph(convert_newlines(code_block + explanation), code_style))
content.append(Spacer(1, 0.2 * inch))

# Section 9: Summary
content.append(Paragraph("Summary", heading_style))
summary_text = """
This document detailed:
- How to import and read data using Pandas.
- How to fetch data using head, tail, describe, and dtypes.
- Techniques for handling missing values.
- Renaming columns and changing data types.
- Creating new columns using lambda functions.
- Aggregating and grouping data.
- Merging and joining multiple DataFrames.
- Finally, generating a PDF report with ReportLab, displaying all code in a monospaced font.

References:
- Pandas Documentation: https://pandas.pydata.org/pandas-docs/stable/
- ReportLab User Guide: https://www.reportlab.com/documentation/
"""
content.append(Paragraph(convert_newlines(summary_text), normal_code_style))
content.append(Spacer(1, 0.2 * inch))

# Build the PDF document
doc.build(content)
print(f"PDF report '{pdf_filename}' has been generated successfully!")
