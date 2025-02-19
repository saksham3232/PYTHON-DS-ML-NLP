from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Create PDF document
doc = SimpleDocTemplate("PlayStore_Analysis_Report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []

# Custom styles
title_style = ParagraphStyle(
    name='Title',
    fontSize=18,
    leading=22,
    alignment=1,
    spaceAfter=18
)

section_style = ParagraphStyle(
    name='Section',
    fontSize=14,
    leading=18,
    spaceBefore=12,
    spaceAfter=12
)

code_style = ParagraphStyle(
    name='Code',
    fontName='Courier',
    fontSize=10,
    leading=12,
    leftIndent=12,
    spaceBefore=6,
    spaceAfter=6,
    backColor=colors.lightgrey
)

# Title
story.append(Paragraph("Google Play Store Apps Analysis Report", title_style))
story.append(Spacer(1, 12))

# Problem Statement
problem_statement = ("Today, 1.85 million different apps are available for users to download. "
                     "Android users have even more from which to choose, with 2.56 million available through the Google Play Store. "
                     "Our objective is to find the most popular category, the app with the largest number of installs, "
                     "the app with the largest size, etc.")
story.append(Paragraph("Problem Statement", getSampleStyleSheet()['Heading2']))
story.append(Paragraph(problem_statement, getSampleStyleSheet()['BodyText']))
story.append(Spacer(1, 12))

# Data Collection
data_collection = "The data consists of 20 columns and 10841 rows."
story.append(Paragraph("Data Collection", getSampleStyleSheet()['Heading2']))
story.append(Paragraph(data_collection, getSampleStyleSheet()['BodyText']))
story.append(Spacer(1, 12))

# Steps to Follow
story.append(Paragraph("Steps We Are Going to Follow", getSampleStyleSheet()['Heading2']))
steps = [
    "Data Cleaning",
    "Exploratory Data Analysis",
    "Feature Engineering"
]
for step in steps:
    story.append(Paragraph(f"- {step}", getSampleStyleSheet()['BodyText']))
story.append(Spacer(1, 12))

# Code Snippet: Importing Libraries and Loading Data
story.append(Paragraph("Code Snippet: Importing Libraries and Loading Data", getSampleStyleSheet()['Heading2']))
code1 = """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/
main/googleplaystore.csv')
df.head()
"""
story.append(Preformatted(code1, code_style))
story.append(Spacer(1, 12))

# Data Overview
story.append(Paragraph("Data Overview", getSampleStyleSheet()['Heading2']))
overview = ("The dataset has missing values and consists of various features such as App, Category, Rating, "
            "Reviews, Size, Installs, Type, Price, Content Rating, Genres, Last Updated, Current Ver, and Android Ver.")
story.append(Paragraph(overview, getSampleStyleSheet()['BodyText']))
story.append(Spacer(1, 12))

# Code Snippet: Data Cleaning
story.append(Paragraph("Code Snippet: Data Cleaning", getSampleStyleSheet()['Heading2']))
code2 = """
# Handling Missing Values
df.isnull().sum()

# Convert Reviews to Integer
df['Reviews'] = df['Reviews'].astype(int)

# Convert Size to Float
df['Size'] = df['Size'].str.replace('M', '000').str.replace('k', '').astype(float)

# Convert Installs and Price
df['Installs'] = df['Installs'].str.replace('+', '').str.replace(',', '').astype(int)
df['Price'] = df['Price'].str.replace('$', '').astype(float)
"""
story.append(Preformatted(code2, code_style))
story.append(Spacer(1, 12))

# Handling Last Update Feature
story.append(Paragraph("Handling Last Update Feature", getSampleStyleSheet()['Heading2']))
code3 = """
# Convert Last Updated to datetime
df['Last Updated'] = pd.to_datetime(df['Last Updated'])
df['Day'] = df['Last Updated'].dt.day
df['Month'] = df['Last Updated'].dt.month
df['Year'] = df['Last Updated'].dt.year
"""
story.append(Preformatted(code3, code_style))
story.append(Spacer(1, 12))

# EDA
story.append(Paragraph("Exploratory Data Analysis (EDA)", getSampleStyleSheet()['Heading2']))
eda_intro = ("In this section, we will explore the dataset to find insights such as the most popular app category, "
             "the app with the largest number of installs, and more.")
story.append(Paragraph(eda_intro, getSampleStyleSheet()['BodyText']))
story.append(Spacer(1, 12))

# Code Snippet: EDA
story.append(Paragraph("Code Snippet: EDA", getSampleStyleSheet()['Heading2']))
code4 = """
# Most Popular Category
df['Category'].value_counts().plot.pie(figsize=(15, 16), autopct='%1.1f%%')

# Top 10 App Categories
category = pd.DataFrame(df['Category'].value_counts())
category.rename(columns={'Category': "Count"}, inplace=True)

plt.figure(figsize=(15, 6))
sns.barplot(x=category.index[:10], y='Count', data=category[:10], palette='hls')
plt.title('Top 10 App Categories')
plt.xticks(rotation=90)
plt.show()
"""
story.append(Preformatted(code4, code_style))
story.append(Spacer(1, 12))

# Insights
insights = ("Insights from the EDA show that the Family category has the most number of apps, followed by Games and Tools. "
            "The Beauty category has the least number of apps.")
story.append(Paragraph("Insights", getSampleStyleSheet()['Heading2']))
story.append(Paragraph(insights, getSampleStyleSheet()['BodyText']))
story.append(Spacer(1, 12))

# Internal Assignments
internal_assignments = ("1. Which Category has the largest number of installations?\n"
                       "2. What are the Top 5 most installed Apps in Each popular Category?\n"
                       "3. How many apps are there on Google Play Store which get 5 ratings?")
story.append(Paragraph("Internal Assignments", getSampleStyleSheet()['Heading2']))
story.append(Paragraph(internal_assignments, getSampleStyleSheet()['BodyText']))
story.append(Spacer(1, 12))

# Code Snippet: Installations Analysis
story.append(Paragraph("Code Snippet: Installations Analysis", getSampleStyleSheet()['Heading2']))
code5 = """
# Which Category has the largest number of installations?
df_cat_installs = df.groupby(['Category'])['Installs']
.sum().sort_values(ascending=False).reset_index()

df_cat_installs.Installs = df_cat_installs.Installs / 
1000000000  # converting into billions

plt.figure(figsize=(14, 10))
sns.barplot(x='Installs', y='Category', data=df_cat_installs.head(10))
plt.xlabel('No. of Installations in Billions')
plt.title("Most Popular Categories in Play Store", size=20)
plt.show()
"""
story.append(Preformatted(code5, code_style))
story.append(Spacer(1, 12))

# Code Snippet: Top 5 Most Installed Apps
story.append(Paragraph("Code Snippet: Top 5 Most Installed Apps", getSampleStyleSheet()['Heading2']))
code6 = """
# Top 5 most installed Apps in Each popular Category
dfa = df.groupby(['Category', 'App'])['Installs'].sum().reset_index()
dfa = dfa.sort_values('Installs', ascending=False)
apps = ['GAME', 'COMMUNICATION', 'PRODUCTIVITY', 'SOCIAL']

plt.figure(figsize=(40, 30))
for i, app in enumerate(apps):
    df2 = dfa[dfa.Category == app]
    df3 = df2.head(5)
    plt.subplot(4, 2, i + 1)
    sns.barplot(data=df3, x='Installs', y='App')
    plt.xlabel('Installation in Millions')
    plt.title(app, size=20)

plt.tight_layout()
plt.subplots_adjust(hspace=.3)
plt.show()
"""
story.append(Preformatted(code6, code_style))
story.append(Spacer(1, 12))

# Code Snippet: 5 Rated Apps
story.append(Paragraph("Code Snippet: 5 Rated Apps", getSampleStyleSheet()['Heading2']))
code7 = """
# How many apps are there on Google Play Store which get 5 ratings?
rating = df.groupby(['Category', 'Installs', 'App'])['Rating']
.sum().sort_values(ascending=False).reset_index()
toprating_apps = rating[rating.Rating == 5.0]
print('Number of 5 rated apps:', toprating_apps.shape[0])
toprating_apps.head(1)
"""
story.append(Preformatted(code7, code_style))
# story.append(Spacer(1, 12))

# Key Insights Section
story.append(PageBreak())
story.append(Paragraph("<b> Key Insights</b>", section_style))
insights = [
    "1. Family category has the most apps (18%) followed by Games (11%).",
    "2. Game category leads in installations with ~35 billion installs.",
    "3. Subway Surfers is the most installed game with 1B+ installs.",
    "4. 271 apps have perfect 5-star ratings.",
    "5. Rating distribution shows most apps have 4-4.5 ratings.",
    "6. 92.6% of apps are free, while 7.4% are paid."
]

for insight in insights:
    story.append(Paragraph(insight, styles["Normal"]))
    story.append(Spacer(1, 6))

# Glossary Section
# story.append(PageBreak())
story.append(Paragraph("<b>Glossary</b>", section_style))
glossary_terms = {
    "App": "A software application designed to run on mobile devices.",
    "Category": "The classification of apps based on their functionality.",
    "Rating": "A score given to an app based on user reviews.",
    "Reviews": "The number of user feedback entries for an app.",
    "Size": "The storage space required by the app.",
    "Installs": "The total number of times the app has been downloaded.",
    "Type": "Indicates whether the app is free or paid.",
    "Price": "The cost of the app if it is paid.",
    "Content Rating": "The age group for which the app is appropriate.",
    "Genres": "The specific type of content the app provides.",
    "Last Updated": "The date when the app was last modified.",
    "Current Ver": "The current version of the app available.",
    "Android Ver": "The minimum Android version required to run the app."
}

for term, definition in glossary_terms.items():
    story.append(Paragraph(f"<b>{term}:</b> {definition}", styles["Normal"]))
    story.append(Spacer(1, 6))

# Conclusion
conclusion = ("In conclusion, the analysis of the Google Play Store dataset provides valuable insights into app categories, "
              "ratings, and installations. This information can be useful for developers and marketers in understanding trends and user preferences.")
story.append(Paragraph("Conclusion", getSampleStyleSheet()['Heading2']))
story.append(Paragraph(conclusion, getSampleStyleSheet()['BodyText']))
story.append(Spacer(1, 12))

# Build PDF
doc.build(story)
print("PDF report generated successfully!")