from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
import pandas as pd
import seaborn as sns

# Create a PDF document
pdf_file = "20-Missing_Values_Report.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a list to hold the content
content = []

# Define styles
styles = getSampleStyleSheet()
title_style = styles['Title']
heading_style = styles['Heading1']
normal_style = styles['BodyText']
code_style = ParagraphStyle(name='CodeStyle', fontName='Courier', fontSize=10, textColor=colors.black)

# Title
content.append(Paragraph("Missing Values in Datasets", title_style))

# Introduction
content.append(Paragraph("This report covers the concept of missing values in datasets, "
                         "the mechanisms behind them, and various imputation techniques. "
                         "We will explore examples using the Titanic dataset.", normal_style))
content.append(Spacer(1, 12))

# Section 1: Mechanisms of Missing Values
content.append(Paragraph("1. Mechanisms of Missing Values", heading_style))
content.append(Paragraph("Missing values occur in datasets when some information is not stored for a variable. "
                         "There are three main mechanisms:", normal_style))
content.append(Spacer(1, 12))

# MCAR
content.append(Paragraph("1.1 Missing Completely at Random (MCAR)", heading_style))
content.append(Paragraph("Missing completely at random (MCAR) is a type of missing data mechanism in which the probability of a value being missing is unrelated to both the observed data and the missing data. In other words, if the data is MCAR, the missing values are randomly distributed throughout the dataset, and there is no systematic reason for why they are missing."
                         "\nFor example, in a survey about the prevalence of a certain disease, the missing data might be MCAR if the survey participants with missing values for certain questions were selected randomly and their missing responses are not related to their disease status or any other variables measured in the survey.", normal_style))
content.append(Spacer(1, 12))

# MAR
content.append(Paragraph("1.2 Missing at Random (MAR)", heading_style))
content.append(Paragraph("Missing at Random (MAR) is a type of missing data mechanism in which the probability of a value being missing depends only on the observed data, but not on the missing data itself. In other words, if the data is MAR, the missing values are systematically related to the observed data, but not to the missing data. Here are a few examples of missing at random:"
                         "\nIncome data: Suppose you are collecting income data from a group of people, but some participants choose not to report their income. If the decision to report or not report income is related to the participant's age or gender, but not to their income level, then the data is missing at random."
                         "\nMedical data: Suppose you are collecting medical data on patients, including their blood pressure, but some patients do not report their blood pressure. If the patients who do not report their blood pressure are more likely to be younger or have healthier lifestyles, but the missingness is not related to their actual blood pressure values, then the data is missing at random.", normal_style))
content.append(Spacer(1, 12))

# MNAR
content.append(Paragraph("1.3 Missing Not at Random (MNAR)", heading_style))
content.append(Paragraph("It is a type of missing data mechanism where the probability of missing values depends on the value of the missing data itself. In other words, if the data is MNAR, the missingness is not random and is dependent on unobserved or unmeasured factors that are associated with the missing values."
                         "\nFor example, suppose you are collecting data on the income and job satisfaction of employees in a company. If employees who are less satisfied with their jobs are more likely to refuse to report their income, then the data is not missing at random. In this case, the missingness is dependent on job satisfaction, which is not directly observed or measured.", normal_style))
content.append(Spacer(1, 12))

# Section 2: Example with Titanic Dataset
content.append(Paragraph("2. Example with Titanic Dataset", heading_style))
content.append(Paragraph("We will use the Titanic dataset to demonstrate how to handle missing values.", normal_style))
content.append(Spacer(1, 12))

# Code Snippet: Load Dataset
code1 = """
import seaborn as sns
df = sns.load_dataset('titanic')
df.head()
"""
content.append(Paragraph("Code Snippet: Load Dataset", heading_style))
content.append(Preformatted(code1, style=code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This code snippet loads the Titanic dataset using the seaborn library and displays the first few rows.", normal_style))
content.append(Spacer(1, 12))

# Check for missing values
code2 = "df.isnull().sum()"
content.append(Paragraph("Code Snippet: Check for Missing Values", heading_style))
content.append(Preformatted(code2, style=code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This code checks for missing values in each column of the dataset.", normal_style))
content.append(Spacer(1, 12))

# Deleting Rows with Missing Values
code3 = "df.dropna().shape"
content.append(Paragraph("Code Snippet: Delete Rows with Missing Values", heading_style))
content.append(Preformatted(code3, style=code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This code snippet deletes rows with any missing values and shows the new shape of the dataset.", normal_style))
content.append(Spacer(1, 12))

# Imputation Techniques
content.append(Paragraph("3. Imputation Techniques", heading_style))
content.append(Paragraph("We can handle missing values using various imputation techniques:", normal_style))
content.append(Spacer(1, 12))

# Mean Value Imputation
code4 = """
df['age_mean'] = df['age'].fillna(df['age'].mean())
"""
content.append(Paragraph("3.1 Mean Value Imputation", heading_style))
content.append(Preformatted(code4, style=code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This code fills missing values in the 'age' column with the mean age.", normal_style))
content.append(Spacer(1, 12))

# Median Value Imputation
code5 = """
df['age_median'] = df['age'].fillna(df['age'].median())
"""
content.append(Paragraph("3.2 Median Value Imputation", heading_style))
content.append(Preformatted(code5, style=code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This code fills missing values in the 'age' column with the median age, which is useful in the presence of outliers.", normal_style))
content.append(Spacer(1, 12))

# Mode Imputation
code6 = """
df['embarked'].unique()

mode_value=df[df['embarked'].notna()]['embarked'].mode()[0]

df['embarked_mode']=df['embarked'].fillna(mode_value)
"""
content.append(Paragraph("3.3 Mode Imputation for Categorical Values", heading_style))
content.append(Preformatted(code6, style=code_style))
# content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This code fills missing values in the 'embarked' column with the mode (most frequent value).", normal_style))
# content.append(Spacer(1, 12))

# Conclusion
content.append(Paragraph("4. Conclusion", heading_style))
content.append(Paragraph("Handling missing values is crucial for data analysis. Understanding the mechanisms behind missing data "
                         "and applying appropriate imputation techniques can significantly improve the quality of the dataset.", normal_style))


# Build the PDF
document.build(content)

print(f"PDF report '{pdf_file}' has been generated successfully.")