import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle

# Create a PDF document
pdf_file = "Seaborn_Data_Visualization_Report.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a list to hold the content
content = []

# Title
title_style = ParagraphStyle(name='Title', fontSize=24, spaceAfter=20)
content.append(Paragraph("Data Visualization with Seaborn", title_style))

# Introduction Section
content.append(Paragraph("Introduction", style=getSampleStyleSheet()['Heading2']))
content.append(Paragraph("Seaborn is a Python visualization library based on Matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics. "
                         "Seaborn helps in creating complex visualizations with just a few lines of code. In this lesson, we will cover the basics of Seaborn, including creating various types of plots and customizing them.", 
                         style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# Data Source Section
content.append(Paragraph("Data Source: Tips Dataset", style=getSampleStyleSheet()['Heading2']))
content.append(Paragraph("The 'tips' dataset is included in the Seaborn library and contains information about restaurant tips. "
                         "It includes the following columns:", style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# Data Description
data_description = [
    ("Column", "Description"),
    ("total_bill", "Total bill (in USD)"),
    ("tip", "Tip amount (in USD)"),
    ("sex", "Gender of the person paying the bill (Male/Female)"),
    ("smoker", "Whether the person is a smoker (Yes/No)"),
    ("day", "Day of the week (Sun, Sat, Thur, Fri)"),
    ("time", "Time of day (Lunch/Dinner)"),
    ("size", "Size of the party (number of people)")
]

# Create a table for data description
table_data = [[Paragraph(col, getSampleStyleSheet()['Heading3']) for col in data_description[0]]]
for row in data_description[1:]:
    table_data.append([Paragraph(item, getSampleStyleSheet()['BodyText']) for item in row])

table = Table(table_data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))

content.append(table)
content.append(Spacer(1, 12))

# Load dataset
tips = sns.load_dataset('tips')

# Scatter Plot
plt.figure()
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title('Scatter Plot of Total Bill VS Tip')
plt.savefig('scatter_plot.png')
plt.close()

# Add Scatter Plot Image and Code
content.append(Paragraph("Scatter Plot", style=getSampleStyleSheet()['Heading2']))
content.append(Image('scatter_plot.png', width=400, height=300))
content.append(Spacer(1, 12))
content.append(Paragraph("Code:", style=getSampleStyleSheet()['Heading3']))
content.append(Paragraph("sns.scatterplot(x='total_bill', y='tip', data=tips)", style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))
content.append(Paragraph("Key Definition: A scatter plot displays values for typically two variables for a set of data. Each point represents an observation in the dataset.", style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# Line Plot
plt.figure()
sns.lineplot(x='size', y='total_bill', data=tips)
plt.title('Line Plot of Total Bill VS Size')
plt.savefig('line_plot.png')
plt.close()

# Add Line Plot Image and Code
content.append(Paragraph("Line Plot", style=getSampleStyleSheet()['Heading2']))
content.append(Image('line_plot.png', width=400, height=300))
content.append(Spacer(1, 12))
content.append(Paragraph("Code:", style=getSampleStyleSheet()['Heading3']))
content.append(Paragraph("sns.lineplot(x='size', y='total_bill', data=tips)", style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))
content.append(Paragraph("Key Definition: A line plot is used to display information as a series of data points called 'markers' connected by straight line segments.", style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# Bar Plot
plt.figure()
sns.barplot(x='day', y='total_bill', data=tips)
plt.title('Bar Plot of Total Bill VS Day')
plt.savefig('bar_plot.png')
plt.close()

# Add Bar Plot Image and Code
content.append(Paragraph("Bar Plot", style=getSampleStyleSheet()['Heading2']))
content.append(Image('bar_plot.png', width=400, height=300))
content.append(Spacer(1, 12))
content.append(Paragraph("Code:", style=getSampleStyleSheet()['Heading3']))
content.append(Paragraph("sns.barplot(x='day', y='total_bill', data=tips)", style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))
content.append(Paragraph("Key Definition: A bar plot is a chart that presents categorical data with rectangular bars. The lengths of the bars are proportional to the values they represent.", style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# Box Plot
plt.figure()
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Box Plot of Total Bill by Day')
plt.savefig('box_plot.png')
plt.close()

# Add Box Plot Image and Code
content.append(Paragraph("Box Plot", style=getSampleStyleSheet()['Heading2']))
content.append(Image('box_plot.png', width=400, height=300))
content.append(Spacer(1, 12))
content.append(Paragraph("Code:", style=getSampleStyleSheet()['Heading3']))
content.append(Paragraph("sns.boxplot(x='day', y='total_bill', data=tips)", style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))
content.append(Paragraph("Key Definition: A box plot (or whisker plot) displays the distribution of data based on a five-number summary ('minimum', first quartile (Q1), median, third quartile (Q3), and 'maximum').", style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# Violin Plot
plt.figure()
sns.violinplot(x='day', y='total_bill', data=tips)
plt.title('Violin Plot of Total Bill by Day')
plt.savefig('violin_plot.png')
plt.close()

# Add Violin Plot Image and Code
content.append(Paragraph("Violin Plot", style=getSampleStyleSheet()['Heading2']))
content.append(Image('violin_plot.png', width=400, height=300))
content.append(Spacer(1, 12))
content.append(Paragraph("Code:", style=getSampleStyleSheet()['Heading3']))
content.append(Paragraph("sns.violinplot(x='day', y='total_bill', data=tips)", style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))
content.append(Paragraph("Key Definition: A violin plot is similar to a box plot, but it also shows the probability density of the data at different values, which is useful for visualizing the distribution of the data.", style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# Histogram
plt.figure()
sns.histplot(tips['total_bill'], bins=30, kde=False)
plt.title('Histogram of Total Bill')
plt.savefig('histogram.png')
plt.close()

# Add Histogram Image and Code
content.append(Paragraph("Histogram", style=getSampleStyleSheet()['Heading2']))
content.append(Image('histogram.png', width=400, height=300))
content.append(Spacer(1, 12))
content.append(Paragraph("Code:", style=getSampleStyleSheet()['Heading3']))
content.append(Paragraph("sns.histplot(tips['total_bill'], bins=30, kde=False)", style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))
content.append(Paragraph("Key Definition: A histogram is a graphical representation of the distribution of numerical data, showing the number of data points that fall within a specified range of values (bins).", style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# KDE Plot
plt.figure()
sns.kdeplot(tips['total_bill'], fill=True)
plt.title('KDE Plot of Total Bill')
plt.savefig('kde_plot.png')
plt.close()

# Add KDE Plot Image and Code
content.append(Paragraph("KDE Plot", style=getSampleStyleSheet()['Heading2']))
content.append(Image('kde_plot.png', width=400, height=300))
content.append(Spacer(1, 12))
content.append(Paragraph("Code:", style=getSampleStyleSheet()['Heading3']))
content.append(Paragraph("sns.kdeplot(tips['total_bill'], fill=True)", style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))
content.append(Paragraph("Key Definition: A Kernel Density Estimate (KDE) plot is a way to estimate the probability density function of a random variable, providing a smooth curve that represents the distribution of the data.", style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# Pair Plot
sns.pairplot(tips)
plt.savefig('pair_plot.png')
plt.close()

# Add Pair Plot Image and Code
content.append (Paragraph("Pair Plot", style=getSampleStyleSheet()['Heading2']))
content.append(Image('pair_plot.png', width=400, height=300))
content.append(Spacer(1, 12))
content.append(Paragraph("Code:", style=getSampleStyleSheet()['Heading3']))
content.append(Paragraph("sns.pairplot(tips)", style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))
content.append(Paragraph("Key Definition: A pair plot is a matrix of scatter plots that shows the relationships between multiple variables in a dataset, allowing for easy visualization of correlations.", style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# Heat Map
corr = tips[['total_bill', 'tip', 'size']].corr()
plt.figure()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heat Map of Correlations')
plt.savefig('heatmap.png')
plt.close()

# Add Heat Map Image and Code
content.append(Paragraph("Heat Map", style=getSampleStyleSheet()['Heading2']))
content.append(Image('heatmap.png', width=400, height=300))
content.append(Spacer(1, 12))
content.append(Paragraph("Code:", style=getSampleStyleSheet()['Heading3']))
content.append(Paragraph("corr=tips[['total_bill','tip','size']].corr()\nsns.heatmap(corr, annot=True, cmap='coolwarm')", style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))
content.append(Paragraph("Key Definition: A heat map is a data visualization technique that shows the magnitude of a phenomenon as color in two dimensions, allowing for easy identification of patterns and correlations.", style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# Load sales data
sales_df = pd.read_csv('C:\\Users\\saksh\\OneDrive\\Desktop\\DS ML NLP\\12_Data_Analysis_With_Python\\sales_data.csv')

# Plot total sales by product
plt.figure(figsize=(10, 6))
sns.barplot(x='Product Category', y='Total Revenue', data=sales_df, estimator=sum)
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.savefig('total_sales_by_product.png')
plt.close()

# Add Total Sales by Product Image and Code
content.append(Paragraph("Total Sales by Product", style=getSampleStyleSheet()['Heading2']))
content.append(Image('total_sales_by_product.png', width=400, height=300))
content.append(Spacer(1, 12))
content.append(Paragraph("Code:", style=getSampleStyleSheet()['Heading3']))
content.append(Paragraph('''
plt.figure(figsize=(10,6))
sns.barplot(x='Product Category',y='Total Revenue',data=sales_df,estimator=sum)
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()
''', style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))
content.append(Paragraph("Key Definition: This bar plot shows the total sales revenue for each product category, providing insights into which categories are performing best.", style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# Plot total sales by region
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Total Revenue', data=sales_df, estimator=sum)
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.savefig('total_sales_by_region.png')
plt.close()

# Add Total Sales by Region Image and Code
content.append(Paragraph("Total Sales by Region", style=getSampleStyleSheet()['Heading2']))
content.append(Image('total_sales_by_region.png', width=400, height=300))
content.append(Spacer(1, 12))
content.append(Paragraph("Code:", style=getSampleStyleSheet()['Heading3']))
content.append(Paragraph('''
plt.figure(figsize=(10,6))
sns.barplot(x='Region',y='Total Revenue',data=sales_df,estimator=sum)
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()
''', style=getSampleStyleSheet()['Code']))
content.append(Spacer(1, 12))
content.append(Paragraph("Key Definition: This bar plot illustrates the total sales revenue across different regions, highlighting regional performance.", style=getSampleStyleSheet()['BodyText']))
content.append(Spacer(1, 12))

# Build the PDF
document.build(content)

# Notify user
print(f"PDF report '{pdf_file}' has been generated successfully.")