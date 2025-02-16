from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
import pandas as pd

# Create a PDF document
pdf_file = "Target_Guided_Ordinal_Encoding_Report.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a list to hold the content
content = []

# Define styles
styles = getSampleStyleSheet()
normal_style = styles['Normal']
heading_style = styles['Heading1']
code_style = ParagraphStyle(name='CodeStyle', fontName='Courier', fontSize=10, textColor=colors.black)

# Title
content.append(Paragraph("Target Guided Ordinal Encoding", heading_style))
content.append(Spacer(1, 12))

# Introduction
content.append(Paragraph("This report covers the concept of Target Guided Ordinal Encoding, "
                         "a technique used to encode categorical variables based on their relationship "
                         "with the target variable. This encoding technique is particularly useful when "
                         "dealing with categorical variables that have a large number of unique categories.", normal_style))
content.append(Spacer(1, 12))

# Section 1: Sample DataFrame Creation
content.append(Paragraph("1. Sample DataFrame Creation", heading_style))
content.append(Spacer(1, 12))
code_snippet_1 = """
import pandas as pd

# create a sample dataframe with a categorical variable and a target variable
df = pd.DataFrame({
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'New York', 'Paris'],
    'price': [200, 150, 300, 250, 180, 320]
})
df
"""
content.append(Preformatted(code_snippet_1, code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("In this section, we create a sample DataFrame with a categorical variable 'city' "
                         "and a target variable 'price'. This DataFrame will be used to demonstrate the encoding technique.", normal_style))
content.append(Spacer(1, 12))

# Section 2: Mean Price Calculation
content.append(Paragraph("2. Mean Price Calculation", heading_style))
content.append(Spacer(1, 12))
code_snippet_2 = """
mean_price = df.groupby('city')['price'].mean().to_dict()
mean_price
"""
content.append(Preformatted(code_snippet_2, code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("Here, we calculate the mean price for each city using the groupby method and convert it to a dictionary.", normal_style))
content.append(Spacer(1, 12))

# Section 3: Encoding the Categorical Variable
content.append(Paragraph("3. Encoding the Categorical Variable", heading_style))
content.append(Spacer(1, 12))
code_snippet_3 = """
df['city_encoded'] = df['city'].map(mean_price)
df[['price', 'city_encoded']]
"""
content.append(Preformatted(code_snippet_3, code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("In this step, we replace each category in the 'city' column with its corresponding mean price, "
                         "creating a new column 'city_encoded'. This establishes a monotonic relationship between the categorical variable and the target variable.", normal_style))
content.append(Spacer(1, 12))

# Section 4: Example with Seaborn Dataset
content.append(Paragraph("4. Example with Seaborn Dataset", heading_style))
content.append(Spacer(1, 12))
code_snippet_4 = """
import seaborn as sns
df = sns.load_dataset('tips')
mean_bill = df.groupby('time')['total_bill'].mean().to_dict()
df['time_encoded'] = df['time'].map(mean_bill)
df[['time', 'time_encoded']]
"""
content.append(Preformatted(code_snippet_4, code_style))
content.append(Spacer(1, 12))
content.append(Paragraph("In this section, we use the 'tips' dataset from the seaborn library to demonstrate the encoding technique. "
                         "We calculate the mean total bill for each time of day and create a new encoded column.", normal_style))
content.append(Spacer(1, 12))

# Conclusion
content.append(Paragraph("Conclusion", heading_style))
content.append(Spacer(1, 12))
content.append(Paragraph("Target Guided Ordinal Encoding is a powerful technique for encoding categorical variables, "
                         "especially when dealing with high cardinality. By establishing a relationship between the categorical variable and the target variable, "
                         "we can improve the predictive power of our machine learning models.", normal_style))
content.append(Spacer(1, 12))


# Glossary
content.append(Paragraph("Glossary", heading_style))
content.append(Spacer(1, 12))
content.append(Paragraph("1. **Target Variable**: The variable that we are trying to predict or explain in a model.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("2. **Categorical Variable**: A variable that can take on one of a limited, and usually fixed, number of possible values, assigning each individual or other unit of observation to a particular group or nominal category.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("3. **Mean**: The average value of a set of numbers, calculated by dividing the sum of the values by the number of values.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("4. **Monotonic Relationship**: A relationship that is either entirely non-increasing or non-decreasing, meaning that as one variable increases, the other variable either only increases or only decreases.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("5. **Encoding**: The process of converting categorical data into a numerical format that can be provided to machine learning algorithms.", normal_style))

# Build the PDF
document.build(content)

print("PDF report generated successfully!")