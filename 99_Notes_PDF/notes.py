# First, ensure you have the required libraries installed
# You can install them using pip if you haven't already
# pip install reportlab seaborn matplotlib numpy

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Preformatted
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create a PDF document
pdf_file = "five_number_summary_report.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)
styles = getSampleStyleSheet()

# Define a new style for code snippets
code_style = ParagraphStyle(
    name='CodeStyle',
    fontName='Courier',
    fontSize=10,
    textColor=colors.black,
    spaceAfter=12,
    leftIndent=12,
    rightIndent=12,
    bulletFontName='Courier',
    bulletFontSize=10,
    bulletColor=colors.black,
)

# Function to create a box plot and save it as an image
def create_box_plot(data, filename):
    plt.figure(figsize=(8, 4))
    sns.boxplot(data)
    plt.title("Box Plot of Marks")
    plt.savefig(filename)
    plt.close()

# Data for the report
lst_marks = [45, 32, 56, 75, 89, 54, 32, 89, 90, 87, 67, 54, 45, 98, 99, 67, 74]

# Create box plot for the first dataset
create_box_plot(lst_marks, "box_plot_1.png")

# Create a second dataset with outliers
lst_marks_with_outliers = [-100, -200, 45, 32, 56, 75, 89, 54, 32, 89, 90, 87, 67, 54, 45, 98, 99, 67, 74, 150, 170, 180]
create_box_plot(lst_marks_with_outliers, "box_plot_2.png")

# Prepare content for the PDF
content = []

# Title
content.append(Paragraph("Five Number Summary and Box Plot Report", styles['Title']))
content.append(Spacer(1, 12))

# Introduction
content.append(Paragraph("This report covers the five-number summary and box plots for a given dataset of marks.", styles['Normal']))
content.append(Spacer(1, 12))

# Section: Five Number Summary
content.append(Paragraph("Five Number Summary", styles['Heading2']))
content.append(Spacer(1, 12))

# Code snippet for five-number summary
code_snippet_1 = """
import numpy as np
lst_marks = [45, 32, 56, 75, 89, 54, 32, 89, 90, 87, 67, 54, 45, 98, 99, 67, 74]
minimum, Q1, median, Q3, maximum = np.quantile(lst_marks, [0, 0.25, 0.50, 0.75, 1.0])
IQR = Q3 - Q1
lower_fence = Q1 - 1.5 * IQR
higher_fence = Q3 + 1.5 * IQR
"""
content.append(Preformatted(code_snippet_1, code_style))
content.append(Spacer(1, 12))

# Explanation of the five-number summary
content.append(Paragraph("The five-number summary consists of the minimum, first quartile (Q1), median, third quartile (Q3), and maximum values of the dataset. "
                         "These statistics provide a quick overview of the distribution of the data.", styles['Normal']))
content.append(Spacer(1, 12))

# Output of the five-number summary
minimum, Q1, median, Q3, maximum = np.quantile(lst_marks, [0, 0.25, 0.50, 0.75, 1.0])
content.append(Paragraph("The five-number summary for the dataset is as follows:", styles['Normal']))
content.append(Paragraph(f"Minimum: {minimum}", styles['Normal']))
content.append(Paragraph(f"Q1: {Q1}", styles['Normal']))
content.append(Paragraph(f"Median: {median}", styles['Normal']))
content.append(Paragraph(f"Q3: {Q3}", styles['Normal']))
content.append( Paragraph(f"Maximum: {maximum}", styles['Normal']))
content.append(Spacer(1, 12))

# Section: Box Plot
content.append(Paragraph("Box Plot", styles['Heading2']))
content.append(Spacer(1, 12))

# Code snippet for box plot
code_snippet_2 = """
import seaborn as sns
lst_marks_with_outliers = [-100, -200, 45, 32, 56, 75, 89, 54, 32, 89, 90, 87, 67, 54, 45, 98, 99, 67, 74, 150, 170, 180]
sns.boxplot(lst_marks_with_outliers)
"""
content.append(Preformatted(code_snippet_2, code_style))
content.append(Spacer(1, 12))

# Explanation of the box plot
content.append(Paragraph("A box plot visually represents the five-number summary of the dataset. It displays the minimum, Q1, median, Q3, and maximum values, "
                         "along with any potential outliers. The box represents the interquartile range (IQR), and the line inside the box indicates the median.", styles['Normal']))
content.append(Spacer(1, 12))

# Adding the first box plot image
content.append(Paragraph("Box Plot of Marks (without outliers):", styles['Normal']))
content.append(Image("box_plot_1.png", width=400, height=200))
content.append(Spacer(1, 12))

# Adding the second box plot image
content.append(Paragraph("Box Plot of Marks (with outliers):", styles['Normal']))
content.append(Image("box_plot_2.png", width=400, height=200))
# content.append(Spacer(1, 12))

# Conclusion
content.append(Paragraph("Conclusion", styles['Heading2']))
content.append(Spacer(1, 12))
content.append(Paragraph("This report provided an overview of the five-number summary and box plots for a dataset of marks. "
                         "These tools are essential for understanding the distribution and identifying outliers in the data.", styles['Normal']))
# content.append(Spacer(1, 12))


# Glossary Section
content.append(Paragraph("Glossary", styles['Heading2']))
content.append(Spacer(1, 12))
content.append(Paragraph("1. Five Number Summary: A descriptive statistic that provides information about a dataset's minimum, first quartile (Q1), median, third quartile (Q3), and maximum.", styles['Normal']))
content.append(Paragraph("2. Box Plot: A graphical representation of the five-number summary that displays the distribution of data based on a five-number summary.", styles['Normal']))
content.append(Paragraph("3. Outlier: A data point that differs significantly from other observations in the dataset.", styles['Normal']))
content.append(Paragraph("4. Interquartile Range (IQR): A measure of statistical dispersion, calculated as the difference between the third quartile (Q3) and the first quartile (Q1).", styles['Normal']))
# content.append(Spacer(1, 12))

# Build the PDF
document.build(content)

print("PDF report generated successfully: five_number_summary_report.pdf")