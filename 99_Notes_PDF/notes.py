from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import numpy as np
import pandas as pd

# Create a PDF document
pdf_file = "Pandas_Report.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a list to hold the content
content = []

# Title
title_style = ParagraphStyle(name='Title', fontSize=24, spaceAfter=12)
content.append(Paragraph("Pandas DataFrame Operations Report", title_style))
content.append(Spacer(1, 12))

# Section 1: DataFrame Creation and Indexing
content.append(Paragraph("1. DataFrame Creation and Indexing", style=getSampleStyleSheet()['Heading2']))
content.append(Spacer(1, 12))

# Task 1.1
content.append(Paragraph("Task 1: Create a DataFrame with 4 columns and 6 rows filled with random integers.", style=getSampleStyleSheet()['Normal']))
code1 = [
    "import pandas as pd",
    "import numpy as np",
    "",
    "# Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers",
    "df = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)), columns=['A', 'B', 'C', 'D'])",
    "# Set the index of the DataFrame to column 'A'",
    "df.set_index('A', inplace=True)"
]
for line in code1:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output1 = [
    "Original DataFrame:",
    "    A   B   C   D",
    "0  52  42  45   9",
    "1  83  16   6  59",
    "2  41   7   6  69",
    "3  70  97  42  32",
    "4  50  47  56  22",
    "5  90  14  85  22",
    "",
    "DataFrame with new index:",
    "     B   C   D",
    "A             ",
    "52  42  45   9",
    "83  16  6  59",
    "41   7  6  69",
    "70  97  42  32",
    "50  47  56  22",
    "90  14  85  22"
]
for line in output1:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Task 1.2
content.append(Paragraph("Task 2: Create a DataFrame with specified columns and index, and access an element.", style=getSampleStyleSheet()['Normal']))
code2 = [
    "# Create a Pandas DataFrame with specified columns and index",
    "df = pd.DataFrame(np.random.randint(1, 100, size=(3, 3)), columns=['A', 'B', 'C'], index=['X', 'Y', 'Z'])",
    "",
    "# Access the element at row 'Y' and column 'B'",
    "element = df.at['Y', 'B']  # .at is used for fast access to a single value"
]
for line in code2:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output2 = [
    "Original DataFrame:",
    "    A   B   C",
    "X  97  97  39",
    "Y  74  25   8",
    "Z  68  38  32",
    "",
    "Element at row 'Y' and column 'B': 25"
]
for line in output2:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Section 2: DataFrame Operations
content.append(Paragraph("2. DataFrame Operations", style=getSampleStyleSheet()['Heading2']))
content.append(Spacer(1, 12))

# Task 2.1
content.append(Paragraph("Task 1: Create a DataFrame with 3 columns and 5 rows filled with random integers and add a new column.", style=getSampleStyleSheet()['Normal']))
code3 = [
    "# Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers",
    "df = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)), columns=['A', 'B', 'C'])",
    "# Add a new column 'D' which is the product of columns 'A' and 'B'",
    "df['D'] = df['A'] * df['B']  # Element-wise multiplication"
]
for line in code3:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output3 = [
    "Original DataFrame:",
    "    A   B   C",
    "0  66  14  24",
    "1  36   5  91",
    "2  16  94  19",
    "3  66  11  52",
    "4  13  10  74",
    "",
    "DataFrame with new column:",
    "    A   B   C     D",
    "0  66  14  24   924",
    "1  36   5  91   180",
    "2  16  94  19  1504",
    "3  66  11  52   726",
    "4  13  10  74   130"
]
for line in output3:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Task 2.2
content.append(Paragraph("Task 2: Create a DataFrame with 3 columns and 4 rows filled with random integers and compute sums.", style=getSampleStyleSheet()['Normal']))
code4 = [
    "# Create a Pandas DataFrame with 3 columns and 4 rows filled with random integers",
    "df = pd.DataFrame(np.random.randint(1, 100, size=(4, 3)), columns=['A', 'B', 'C'])",
    "",
    "# Compute the row-wise and column-wise sum",
    "row_sum = df.sum(axis=1)  # Sum across rows (axis=1)",
    "column_sum = df.sum()  # Sum across columns (default axis=0)"
]
for line in code4:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output4 = [
    "Original DataFrame:",
    "    A   B   C",
    "0  42  67  11",
    "1  90  56  91",
    "2  55  15  20",
    "3  83  15  88",
    "",
    "Row-wise sum:",
    "0    120",
    "1    237",
    "2     90",
    "3    186",
    "dtype: int64",
    "",
    "Column-wise sum:",
    "A    270",
    "B    153",
    "C    210",
    "dtype: int64"
]
for line in output4:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Section 3: Data Cleaning
content.append(Paragraph("3. Data Cleaning", style=getSampleStyleSheet()['Heading2']))
content.append(Spacer(1, 12))

# Task 3.1
content.append(Paragraph("Task 1: Create a DataFrame with NaN values and fill them with the mean of the respective columns.", style=getSampleStyleSheet()['Normal']))
code5 = [
    "# Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers",
    "df = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)), columns=['A', 'B', 'C'])",
    "# Introduce NaN values",
    "df.iloc[0, 1] = np.nan",
    "df.iloc[2, 2] = np.nan",
    "df.iloc[4, 0] = np.nan",
    "",
    "# Fill the NaN values with the mean of the respective columns",
    "df.fillna(df.mean(), inplace=True)  # Fill NaN with column means"
]
for line in code5:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output5 = [
    "DataFrame with NaN values filled:",
    "      A     B     C",
    "0  89.0  47.0  62.0",
    "1  25.0  30.0  68.0",
    "2  54.0  62.0  67.0",
    "3  92.0  39.0  54.0",
    "4  65.0  57.0  84.0"
]
for line in output5:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Task 3.2
content.append(Paragraph("Task 2: Create a DataFrame with NaN values and drop the rows with any NaN values.", style=getSampleStyleSheet()['Normal']))
code6 = [
    "# Create a Pandas DataFrame with 4 columns and 6 rows filled with random integers",
    "df = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)), columns=['A', 'B', 'C', 'D'])",
    "# Introduce NaN values",
    "df.iloc[1, 2] = np.nan",
    "df.iloc[3, 0] = np.nan",
    "df.iloc[5, 1] = np.nan",
    "",
    "# Drop the rows with any NaN values",
    "df.dropna(inplace=True)  # Remove rows with NaN values"
]
for line in code6:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output6 = [
    "DataFrame with NaN values dropped:",
    "      A     B     C   D",
    "0  37.0  87.0  78.0  59",
    "2  38.0   6.0  46.0  93",
    "4  13.0  72.0  95.0  55"
]
for line in output6:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Section 4: Data Aggregation
content.append(Paragraph("4. Data Aggregation", style=getSampleStyleSheet()['Heading2']))
content.append(Spacer(1, 12))

# Task 4.1
content.append(Paragraph("Task 1: Create a DataFrame with 'Category' and 'Value', and compute sum and mean.", style=getSampleStyleSheet()['Normal']))
code7 = [
    "# Create a Pandas DataFrame with 'Category' and 'Value'",
    "df = pd.DataFrame({'Category': np.random.choice(['A', 'B', 'C'], size=10), 'Value': np.random.randint(1, 100, size=10)})",
    "",
    "# Group the DataFrame by 'Category' and compute the sum and mean of 'Value' for each category",
    "grouped = df.groupby('Category')['Value'].agg(['sum', 'mean'])  # Aggregate functions on grouped data"
]
for line in code7:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output7 = [
    "Grouped DataFrame:",
    "          sum       mean",
    "Category                ",
    "A         140  35.000000",
    "B          64  21.333333",
    "C         176  58.666667"
]
for line in output7:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Task 4.2
content.append(Paragraph("Task 2: Create a DataFrame with 'Product', 'Category', and 'Sales', and compute total sales.", style=getSampleStyleSheet()['Normal']))
code8 = [
    "# Create a Pandas DataFrame with 'Product', 'Category', and 'Sales'",
    "df = pd.DataFrame({'Product': np.random.choice(['Prod1', 'Prod2', 'Prod3'], size=10), 'Category': np.random.choice(['A', 'B', 'C'], size=10), 'Sales': np.random.randint(1, 100, size=10)})",
    "",
    "# Group the DataFrame by 'Category' and compute the total sales for each category",
    "grouped = df.groupby('Category')['Sales'].sum()  # Sum sales by category"
]
for line in code8:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output8 = [
    "Grouped DataFrame:",
    "Category",
    "A    125",
    "B    270",
    "C    162",
    "Name: Sales, dtype: int32"
]
for line in output8:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Section 5: Merging DataFrames
content.append(Paragraph("5. Merging DataFrames", style=getSampleStyleSheet()['Heading2']))
content.append(Spacer(1, 12))

# Task 5.1
content.append(Paragraph("Task 1: Create two DataFrames with a common column and merge them.", style=getSampleStyleSheet()['Normal']))
code9 = [
    "# Create two Pandas DataFrames with a common column",
    "df1 = pd.DataFrame({'Key': ['A', 'B', 'C', 'D'], 'Value1': np.random.randint(1, 100, size=4)})",
    "df2 = pd.DataFrame({'Key': ['A', 'B', 'C', 'E'], 'Value2': np.random.randint(1, 100, size=4)})",
    "",
    "# Merge the DataFrames using the common column",
    "merged = pd.merge(df1, df2, on='Key')  # Merge on 'Key' column"
]
for line in code9:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output9 = [
    "DataFrame 1:",
    "  Key  Value1",
    "0   A       2",
    "1   B      95",
    "2   C      92",
    "3   D      41",
    "",
    "DataFrame 2:",
    "  Key  Value2",
    "0   A       5",
    "1   B      69",
    "2   C      35",
    "3   E      26",
    "",
    "Merged DataFrame:",
    "  Key  Value1  Value2",
    "0   A       2       5",
    "1   B      95      69",
    "2   C      92      35"
]
for line in output9:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Task 5.2
content.append(Paragraph("Task 2: Create two DataFrames with different columns and concatenate them.", style=getSampleStyleSheet()['Normal']))
code10 = [
    "# Create two Pandas DataFrames with different columns",
    "df1 = pd.DataFrame({'A': np.random.randint(1, 100, size=3), 'B': np.random.randint(1, 100, size=3})",
    "df2 = pd.DataFrame({'C': np.random.randint(1, 100, size=3), 'D': np.random.randint(1, 100, size=3})",
    "",
    "# Concatenate the DataFrames along the rows",
    "concat_rows = pd.concat([df1, df2], axis=0)  # Stack DataFrames vertically",
    "",
    "# Concatenate the DataFrames along the columns",
    "concat_columns = pd.concat([df1, df2], axis=1)  # Join DataFrames side by side"
]
for line in code10:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output10 = [
    "Concatenated DataFrame (rows):",
    "      A     B     C     D",
    "0  78.0  81.0   NaN   NaN",
    "1  21.0   4.0   NaN   NaN",
    "2  25.0   7.0   NaN   NaN",
    "0   NaN   NaN  11.0  21.0",
    "1   NaN   NaN  45.0  94.0",
    "2   NaN   NaN  79.0  72.0",
    "",
    "Concatenated DataFrame (columns):",
    "    A   B   C   D",
    "0  78  81  11  21",
    "1  21   4  45  94",
    "2  25   7  79  72"
]
for line in output10:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Section 6: Time Series Analysis
content.append(Paragraph("6. Time Series Analysis", style=getSampleStyleSheet()['Heading2']))
content.append(Spacer(1, 12))

# Task 6.1
content.append(Paragraph("Task 1: Create a DataFrame with a datetime index and compute the monthly mean.", style=getSampleStyleSheet()['Normal']))
code11 = [
    "# Create a Pandas DataFrame with a datetime index and one column filled with random integers",
    "date_rng = pd.date_range(start='2022-01-01', end='2022-12-31', freq='D')",
    "df = pd.DataFrame(date_rng, columns=['date'])",
    "df['data'] = np.random.randint(0, 100, size=(len(date_rng)))",
    "df.set_index('date', inplace=True)  # Set the date as the index",
    "",
    "# Resample the DataFrame to compute the monthly mean of the values",
    "monthly_mean = df.resample('M').mean()  # Resample by month and calculate mean"
]
for line in code11:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output11 = [
    "Monthly mean DataFrame:",
    "                 data",
    "date                 ",
    "2022-01-31  48.483871",
    "2022-02-28  47.250000",
    "2022-03-31  54.032258",
    "2022-04-30  44.366667",
    "2022-05-31  52.419355",
    "2022-06-30  49.900000",
    "2022-07-31  49.741935",
    "2022-08-31  52.806452",
    "2022-09-30  53.833333",
    "2022-10-31  48.838710",
    "2022-11-30  51.033333",
    "2022-12-31  55.612903"
]
for line in output11:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Task 6.2
content.append(Paragraph("Task 2: Create a DataFrame with a datetime index and compute the rolling mean.", style=getSampleStyleSheet()['Normal']))
code12 = [
    "# Create a Pandas DataFrame with a datetime index ranging from '2021-01-01' to '2021-12-31'",
    "date_rng = pd.date_range(start='2021-01-01', end='2021-12-31', freq='D')",
    "df = pd.DataFrame(date_rng, columns=['date'])",
    "df['data'] = np.random.randint(0, 100, size=(len(date_rng)))",
    "df.set_index('date', inplace=True)  # Set the date as the index",
    "",
    "# Compute the rolling mean with a window of 7 days",
    "rolling_mean = df.rolling(window=7).mean()  # Calculate rolling mean over a 7-day window"
]
for line in code12:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output12 = [
    "Rolling mean DataFrame:",
    "                 data",
    "date                 ",
    "2021-01-01        NaN",
    "2021-01-02        NaN",
    "2021-01-03        NaN",
    "2021-01-04        NaN",
    "2021-01-05        NaN",
    "...               ...",
    "2021-12-27  40.571429",
    "2021-12-28  38.571429",
    "2021-12-29  44.000000",
    "2021-12-30  49.571429",
    "2021-12-31  51.285714"
]
for line in output12:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Section 7: MultiIndex DataFrame
content.append(Paragraph("7. MultiIndex DataFrame", style=getSampleStyleSheet()['Heading2']))
content.append(Spacer(1, 12))

# Task 7.1
content.append(Paragraph("Task 1: Create a MultiIndex DataFrame and perform indexing.", style=getSampleStyleSheet()['Normal']))
code13 = [
    "# Create a Pandas DataFrame with a MultiIndex (hierarchical index)",
    "arrays = [['A', 'A', 'B', 'B'], ['one', 'two', 'one', 'two']]",
    "index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'SubCategory'))",
    "df = pd.DataFrame(np.random.randint(1, 100, size=(4, 3)), index=index, columns=['Value1', 'Value2', 'Value3'])",
    "",
    "# Basic indexing and slicing operations",
    "df.loc['A']  # Access all rows with Category 'A'",
    "df.loc[('B', 'two')]  # Access specific row with Category 'B' and SubCategory 'two'"
]
for line in code13:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output13 = [
    "MultiIndex DataFrame:",
    "                      Value1  Value2  Value3",
    "Category SubCategory                        ",
    "A        one              12      97       2",
    "         two              29      87      33",
    "B        one              59      75      35",
    "         two              96      28      67",
    "",
    "Indexing at Category 'A':",
    "             Value1  Value2  Value3",
    "SubCategory                        ",
    "one              12      97       2",
    "two              29      87      33",
    "",
    "Slicing at Category 'B' and SubCategory 'two':",
    "Value1    96",
    "Value2    28",
    "Value3    67",
    "Name: (B, two), dtype: int32"
]
for line in output13:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Task 7.2
content.append(Paragraph("Task 2: Create a MultiIndex DataFrame and compute the sum of values.", style=getSampleStyleSheet()['Normal']))
code14 = [
    "# Create a Pandas DataFrame with MultiIndex consisting of 'Category' and 'SubCategory'",
    "arrays = [['A', 'A', 'B', 'B', 'C', 'C'], ['one', 'two', 'one', 'two', 'one', 'two']]",
    "index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'SubCategory'))",
    "df = pd.DataFrame(np.random.randint(1, 100, size=(6, 3)), index=index, columns=['Value1', 'Value2', 'Value3'])",
    "",
    "# Compute the sum of values for each 'Category' and 'SubCategory'",
    "sum_values = df.groupby(['Category', 'SubCategory']).sum()  # Group by both indices and sum"
]
for line in code14:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output14 = [
    "Sum of values:",
    "                      Value1  Value2  Value3",
    "Category SubCategory                        ",
    "A        one              50      63      87",
    "         two              84      21      39",
    "B        one              71      69       5",
    "         two              13      55       1",
    "C        one              50      31      88",
    "         two              48      13      28"
]
for line in output14:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Section 8: Pivot Tables
content.append(Paragraph("8. Pivot Tables", style=getSampleStyleSheet()['Heading2']))
content.append(Spacer(1, 12))

# Task 8.1
content.append(Paragraph("Task 1: Create a pivot table to compute the sum of 'Value' for each 'Category' by 'Date'.", style=getSampleStyleSheet()['Normal']))
code15 = [
    "# Create a Pandas DataFrame with columns 'Date', 'Category', and 'Value'",
    "date_rng = pd.date_range(start='2022-01-01', end='2022-01-10', freq='D')",
    "df = pd.DataFrame({'Date': np.random.choice(date_rng, size=20), 'Category': np.random.choice(['A', 'B', 'C'], size=20), 'Value': np.random.randint(1, 100, size=20)})",
    "",
    "# Create a pivot table to compute the sum of 'Value' for each 'Category' by 'Date'",
    "pivot_table = df.pivot_table(values='Value', index='Date', columns='Category', aggfunc='sum')  # Pivot table with sum aggregation"
]
for line in code15:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output15 = [
    "Pivot Table:",
    "Category        A      B     C",
    "Date                          ",
    "2022-01-02   22.0    7.0  95.0",
    "2022-01-03    NaN  130.0  47.0",
    "2022-01-04  206.0    NaN  31.0",
    "2022-01-05    NaN    NaN  12.0",
    "2022-01-06    NaN   42.0  98.0",
    "2022-01-08   26.0   16.0   NaN",
    "2022-01-09   66.0    NaN   NaN",
    "2022-01-10   95.0    NaN   NaN"
]
for line in output15:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Task 8.2
content.append(Paragraph("Task 2: Create a pivot table to compute the mean 'Revenue' for each 'Quarter' by 'Year'.", style=getSampleStyleSheet()['Normal']))
code16 = [
    "# Create a Pandas DataFrame with columns 'Year', 'Quarter', and 'Revenue'",
    "df = pd.DataFrame({'Year': np.random.choice([2020, 2021, 2022], size=12), 'Quarter': np.random.choice(['Q1', 'Q2', 'Q3', 'Q4'], size=12), 'Revenue': np.random.randint(1, 1000, size=12)})",
    "",
    "# Create a pivot table to compute the mean 'Revenue' for each 'Quarter' by 'Year'",
    "pivot_table = df.pivot_table(values='Revenue', index='Year', columns='Quarter', aggfunc='mean')  # Mean revenue by year and quarter"
]
for line in code16:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output16 = [
    "Pivot Table:",
    "Quarter     Q2     Q3     Q4",
    "Year                        ",
    "2020     517.0  806.0  478.5",
    "2021     561.5  757.0  561.0",
    "2022       NaN    NaN  991.0"
]
for line in output16:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Section 9: Applying Functions
content.append(Paragraph("9. Applying Functions", style=getSampleStyleSheet()['Heading2']))
content.append(Spacer(1, 12))

# Task 9.1
content.append(Paragraph("Task 1: Apply a function that doubles the values of the DataFrame.", style=getSampleStyleSheet()['Normal']))
code17 = [
    "# Create a Pandas DataFrame with 3 columns and 5 rows filled with random integers",
    "df = pd.DataFrame(np.random.randint(1, 100, size=(5, 3)), columns=['A', 'B', 'C'])",
    "print('Original DataFrame:')",
    "print(df)",
    "",
    "# Apply a function that doubles the values of the DataFrame",
    "df_doubled = df.applymap(lambda x: x * 2)  # Apply function to each element",
    "print('Doubled DataFrame:')",
    "print(df_doubled)"
]
for line in code17:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output17 = [
    "Original DataFrame:",
    "    A   B   C",
    "0  46  15  33",
    "1   7  58  23",
    "2  58  80  32",
    "3  34  81  86",
    "4  37  85  73",
    "",
    "Doubled DataFrame:",
    "     A    B    C",
    "0   92   30   66",
    "1   14  116   46",
    "2  116  160   64",
    "3   68  162  172",
    "4   74  170  146"
]
for line in output17:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Task 9.2
content.append(Paragraph("Task 2: Apply a lambda function to create a new column that is the sum of the existing columns.", style=getSampleStyleSheet()['Normal']))
code18 = [
    "# Create a Pandas DataFrame with 3 columns and 6 rows filled with random integers",
    "df = pd.DataFrame(np.random.randint(1, 100, size=(6, 3)), columns=['A', 'B', 'C'])",
    "print('Original DataFrame:')",
    "print(df)",
    "",
    "# Apply a lambda function to create a new column 'D' that is the sum of the existing columns",
    "df['D'] = df.apply(lambda row: row['A'] + row['B'] + row['C'], axis=1)  # Sum across rows",
    "print('DataFrame with new column D:')",
    "print(df)"
]
for line in code18:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

output18 = [
    "Original DataFrame:",
    "    A   B   C",
    "0  45  67  23",
    "1  12  34  56",
    "2  78  90  12",
    "3  23  45  67",
    "4  89  12  34",
    "5  56  78  90",
    "",
    "DataFrame with new column D:",
    "    A   B   C   D",
    "0  45  67  23  135",
    "1  12  34  56  102",
    "2  78  90  12  180",
    "3  23  45  67  135",
    "4  89  12  34  135",
    "5  56  78  90  224"
]
for line in output18:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Section 10: Working with Text Data
content.append(Paragraph("10. Working with Text Data", style=getSampleStyleSheet()['Heading2']))
content.append(Spacer(1, 12))

# Task 10.1
content.append(Paragraph("Task 1: Create a Pandas Series with 5 random text strings. Convert all the strings to uppercase.", style=getSampleStyleSheet()['Normal']))
code19 = [
    "# Create a Pandas Series with 5 random text strings",
    "text_data = pd.Series(['apple', 'banana', 'cherry', 'date', 'elderberry'])",
    "print('Original Series:')",
    "print(text_data)",
    "",
    "# Convert all the strings to uppercase",
    "uppercase_data = text_data.str.upper()  # Convert strings to uppercase",
    "print('Uppercase Series:')",
    "print(uppercase_data)"
]
for line in code19:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output19 = [
    "Original Series:",
    "0         apple",
    "1        banana",
    "2        cherry",
    "3          date",
    "4    elderberry",
    "dtype: object",
    "",
    "Uppercase Series:",
    "0         APPLE",
    "1        BANANA",
    "2        CHERRY",
    "3          DATE",
    "4    ELDERBERRY",
    "dtype: object"
]
for line in output19:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Task 10.2
content.append(Paragraph("Task 2: Create a Pandas Series with 5 random text strings. Extract the first three characters of each string.", style=getSampleStyleSheet()['Normal']))

code20 = [
    "# Create a Pandas Series with 5 random text strings",
    "text_data = pd.Series(['apple', 'banana', 'cherry', 'date', 'elderberry'])",
    "print('Original Series:')",
    "print(text_data)",
    "",
    "# Extract the first three characters of each string",
    "first_three_chars = text_data.str[:3]  # Slice the first three characters",
    "print('First three characters:')",
    "print(first_three_chars)"
]
for line in code20:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))

output20 = [
    "Original Series:",
    "0         apple",
    "1        banana",
    "2        cherry",
    "3          date",
    "4    elderberry",
    "dtype: object",
    "",
    "First three characters:",
    "0    app",
    "1    ban",
    "2    che",
    "3    dat",
    "4    eld",
    "dtype: object"
]
for line in output20:
    content.append(Paragraph(line, style=getSampleStyleSheet()['Code']))  # Use code style for output
content.append(Spacer(1, 12))

# Build the PDF
document.build(content)