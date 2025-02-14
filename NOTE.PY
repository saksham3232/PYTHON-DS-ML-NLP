from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
import pandas as pd
import seaborn as sns
import numpy as np

# Create a PDF document
pdf_file = "22-Data_Analysis_Report.pdf"
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
content.append(Paragraph("Data Analysis Report: Missing Values and Imbalanced Datasets", title_style))

# Introduction
content.append(Paragraph("This report covers two important topics in data analysis: "
                         "missing values in datasets and techniques for handling imbalanced datasets. "
                         "We will explore examples using the Titanic dataset and synthetic datasets.", normal_style))
content.append(Spacer(1, 12))

# Section 1: Missing Values in Datasets
content.append(Paragraph("1. Missing Values in Datasets", heading_style))
content.append(Paragraph("Missing values occur in datasets when some information is not stored for a variable. "
                         "There are three main mechanisms:", normal_style))
content.append(Spacer(1, 12))

# MCAR
content.append(Paragraph("1.1 Missing Completely at Random (MCAR)", heading_style))
content.append(Paragraph("Missing completely at random (MCAR) is a type of missing data mechanism in which the probability of a value being missing is unrelated to both the observed data and the missing data. In other words, if the data is MCAR, the missing values are randomly distributed throughout the dataset, and there is no systematic reason for why they are missing."
"For example, in a survey about the prevalence of a certain disease, the missing data might be MCAR if the survey participants with missing values for certain questions were selected randomly and their missing responses are not related to their disease status or any other variables measured in the survey.", normal_style))
content.append(Spacer(1, 12))

# MAR
content.append(Paragraph("1.2 Missing at Random (MAR)", heading_style))
content.append(Paragraph("Missing at Random (MAR) is a type of missing data mechanism in which the probability of a value being missing depends only on the observed data, but not on the missing data itself. In other words, if the data is MAR, the missing values are systematically related to the observed data, but not to the missing data. Here are a few examples of missing at random:"

"Income data: Suppose you are collecting income data from a group of people, but some participants choose not to report their income. If the decision to report or not report income is related to the participant's age or gender, but not to their income level, then the data is missing at random."

"Medical data: Suppose you are collecting medical data on patients, including their blood pressure, but some patients do not report their blood pressure. If the patients who do not report their blood pressure are more likely to be younger or have healthier lifestyles, but the missingness is not related to their actual blood pressure values, then the data is missing at random.", normal_style))
content.append(Spacer(1, 12))

# MNAR
content.append(Paragraph("1.3 Missing Not at Random (MNAR)", heading_style))
content.append(Paragraph("It is a type of missing data mechanism where the probability of missing values depends on the value of the missing data itself. In other words, if the data is MNAR, the missingness is not random and is dependent on unobserved or unmeasured factors that are associated with the missing values."

"For example, suppose you are collecting data on the income and job satisfaction of employees in a company. If employees who are less satisfied with their jobs are more likely to refuse to report their income, then the data is not missing at random. In this case, the missingness is dependent on job satisfaction, which is not directly observed or measured.", normal_style))
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

mode_value = df[df['embarked'].notna()]['embarked'].mode()[0]

df['embarked_mode'] = df['embarked'].fillna(mode_value)
"""
content.append(Paragraph("3.3 Mode Imputation for Categorical Values", heading_style))
content.append(Preformatted(code6, style=code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This code fills missing values in the 'embarked' column with the mode (most frequent value).", normal_style))
content.append(Spacer(1, 12))

# Section 4: Handling Imbalanced Datasets
content.append(Paragraph("4. Handling Imbalanced Datasets", heading_style))
content.append(Paragraph("Imbalanced datasets can lead to biased models. We will explore techniques for handling such datasets, specifically focusing on upsampling and downsampling methods.", normal_style))
content.append(Spacer(1, 12))

# Section: Creating an Imbalanced Dataset
content.append(Paragraph("4.1 Creating an Imbalanced Dataset", heading_style))
content.append(Paragraph("We start by creating a synthetic dataset with two classes, where one class is significantly larger than the other.", normal_style))
content.append(Spacer(1, 12))

# Code Snippet
code7 = """
import numpy as np
import pandas as pd

# Set the random seed for reproductivity
np.random.seed(123)

# Create a dataframe with two classes
n_samples = 1000
class_0_ratio = 0.9
n_class_0 = int(n_samples * class_0_ratio)
n_class_1 = n_samples - n_class_0

class_0 = pd.DataFrame({
    'feature_1' : np.random.normal(loc=0, scale=1, size=n_class_0),
    'feature_2' : np.random.normal(loc=0, scale=1, size=n_class_0),
    'target' : [0] * n_class_0
})

class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=2, scale=1, size=n_class_1),
    'feature_2': np.random.normal(loc=2, scale=1, size=n_class_1),
    'target': [1] * n_class_1
})

df = pd.concat([class_0, class_1]).reset_index(drop=True)
"""
content.append(Paragraph("Code Snippet: Create Imbalanced Dataset", heading_style))
content.append(Preformatted(code7, style=code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("In this code, we create a dataset with 1000 samples, where 900 belong to class 0 and 100 belong to class 1. "
                         "The features are generated using a normal distribution.", normal_style))
content.append(Spacer(1, 12))

# Section: Checking Class Distribution
content.append(Paragraph("4.2 Checking Class Distribution", heading_style))
content.append(Paragraph("We can check the distribution of the classes in our dataset.", normal_style))
content.append(Spacer(1, 12))

# Code Snippet
code8 = """
df['target'].value_counts()
"""
content.append(Paragraph("Code Snippet: Check Class Distribution", heading_style))
content.append(Preformatted(code8, style=code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This code snippet shows the distribution of the target classes in the dataset, confirming the imbalance.", normal_style))
content.append(Spacer(1, 12))

# Section: Upsampling
content.append(Paragraph("4.3 Upsampling", heading_style))
content.append(Paragraph("Upsampling involves increasing the number of instances in the minority class to balance the dataset.", normal_style))
content.append(Spacer(1, 12))

# Code Snippet
code9 = """
from sklearn.utils import resample

df_minority = df[df['target'] == 1]
df_majority = df[df['target'] == 0]

df_minority_upsampled = resample(df_minority, replace=True, 
                                 n_samples=len(df_majority), 
                                 random_state=42)

df_upsampled = pd.concat([df_majority, df_minority_upsampled])
df_upsampled['target'].value_counts()
"""
content.append(Paragraph("Code Snippet: Upsampling", heading_style))
content.append(Preformatted(code9, style=code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("In this code, we use the `resample` function from `sklearn.utils` to upsample the minority class. "
                         "We then concatenate the upsampled minority class with the majority class to create a balanced dataset.", normal_style))
content.append(Spacer(1, 12))

# Section: Downsampling
content.append(Paragraph("4.4 Downsampling", heading_style))
content.append(Paragraph("Downsampling involves reducing the number of instances in the majority class to balance the dataset.", normal_style))
content.append(Spacer(1, 12))

# Code Snippet
code10 = """
df_majority_downsampled = resample(df_majority, replace=False,
                                   n_samples=len(df_minority),
                                   random_state=42)

df_downsampled = pd.concat([df_minority, df_majority_downsampled])
df_downsampled['target'].value_counts()
"""
content.append(Paragraph("Code Snippet: Downsampling", heading_style))
content.append(Preformatted(code10, style=code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This code snippet demonstrates how to downsample the majority class. We again use the `resample` function, "
                         "but this time we set `replace=False` to ensure we are not sampling with replacement.", normal_style))
content.append(Spacer(1, 12))

# Conclusion
content.append(Paragraph("5. Conclusion", heading_style))
content.append(Paragraph("Handling missing values and imbalanced datasets is crucial for effective data analysis and model training. "
                         "Understanding the mechanisms behind missing data and applying appropriate techniques for imbalanced datasets can significantly improve the quality of the analysis.", normal_style))
content.append(Spacer(1, 12))

# Glossary Section
content.append(Paragraph("Glossary", title_style))
glossary_terms = {
    "Missing Values": "Data entries that are not recorded or are absent in a dataset.",
    "Imbalanced Dataset": "A dataset where the classes are not represented equally, leading to potential bias in model training.",
    "Upsampling": "A technique used to increase the number of instances in the minority class to achieve a balanced dataset.",
    "Downsampling": "A method that reduces the number of instances in the majority class to balance the dataset.",
    "Synthetic Dataset": "A dataset created artificially, often used for testing and validation purposes.",
    "Resampling": "The process of randomly selecting samples from a dataset to create a new dataset, which can be done with or without replacement.",
    "Class Distribution": "The proportion of different classes within a dataset, which is crucial for understanding the balance of the dataset."
}

for term, definition in glossary_terms.items():
    content.append(Paragraph(f"<b>{term}:</b> {definition}", normal_style))
    content.append(Spacer(1, 6))

# Title
title_style = ParagraphStyle(name='Title', fontSize=24, spaceAfter=20)
content.append(Paragraph("SMOTE (Synthetic Minority Over-sampling Technique)", title_style))

# Introduction
intro_style = getSampleStyleSheet()['BodyText']
content.append(Paragraph("This report covers the SMOTE technique, which is used in machine learning to address imbalanced datasets. "
                         "SMOTE generates synthetic instances of the minority class by interpolating between existing instances.", intro_style))
content.append(Spacer(1, 12))

# Section 1: Generating a Sample Dataset
content.append(Paragraph("1. Generating a Sample Dataset", title_style))
content.append(Paragraph("We will first create a synthetic dataset using the `make_classification` function from the `sklearn.datasets` module.", intro_style))
content.append(Spacer(1, 12))

# Code snippet for generating the dataset
code1 = """
from sklearn.datasets import make_classification
X, Y = make_classification(n_samples=1000, n_redundant=0, n_features=2,
                           n_clusters_per_class=1, weights=[0.90],
                           random_state=12)
import pandas as pd
df1 = pd.DataFrame(X, columns=['f1', 'f2'])
df2 = pd.DataFrame(Y, columns=['target'])
final_df = pd.concat([df1, df2], axis=1)
final_df.head()
"""
content.append(Paragraph("Code Snippet: Generate Sample Dataset", heading_style))
content.append(Preformatted(code1, style=code_style))
content.append(Spacer(1, 12))

# Explanation of the dataset generation
content.append(Paragraph("In this code, we generate a dataset with 1000 samples, where 90% belong to one class (majority) and 10% to another (minority). "
                         "The features are stored in a DataFrame, and we can visualize the first few rows using `head()`.", intro_style))
content.append(Spacer(1, 12))

# Section 2: Visualizing the Dataset
content.append(Paragraph("2. Visualizing the Dataset", title_style))
content.append(Paragraph("Next, we visualize the dataset to understand the class distribution.", intro_style))
content.append(Spacer(1, 12))

# Code snippet for visualizing the dataset
code2 = """
import matplotlib.pyplot as plt
plt.scatter(final_df['f1'], final_df['f2'], c=final_df['target'])
plt.title('Original Dataset Visualization')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
"""
content.append(Paragraph("Code Snippet: Visualize Dataset", heading_style))
content.append(Preformatted(code2, style=code_style))
content.append(Spacer(1, 12))

# Explanation of the visualization
content.append(Paragraph("The scatter plot above shows the distribution of the two classes in the feature space. "
                         "The majority class (0) is represented by one color, while the minority class (1) is represented by another.", intro_style))
content.append(Spacer(1, 12))

# Section 3: Applying SMOTE
content.append(Paragraph("3. Applying SMOTE", title_style))
content.append(Paragraph("To address the class imbalance, we will apply the SMOTE technique using the `imblearn` library.", intro_style))
content.append(Spacer(1, 12))

# Code snippet for applying SMOTE
code3 = """
!pip install imblearn
from imblearn.over_sampling import SMOTE

# Transform the dataset
oversample = SMOTE()
X, Y = oversample.fit_resample(final_df[['f1', 'f2']], final_df['target'])
X.shape, Y.shape
"""
content.append(Paragraph("Code Snippet: Apply SMOTE", heading_style))
content.append(Preformatted(code3, style=code_style))
content.append(Spacer(1, 12))

# Explanation of SMOTE application
content.append(Paragraph("In this code, we first install the `imblearn` library if it is not already installed. "
                         "Then, we apply SMOTE to the dataset, which generates synthetic samples for the minority class, "
                         "resulting in a balanced dataset with equal instances of both classes.", intro_style))
content.append(Spacer(1, 12))

# Section  4: Visualizing the Oversampled Dataset
content.append(Paragraph("4. Visualizing the Oversampled Dataset", title_style))
content.append(Paragraph("After applying SMOTE, we can visualize the new dataset to confirm that the classes are now balanced.", intro_style))
content.append(Spacer(1, 12))

# Code snippet for visualizing the oversampled dataset
code4 = """
df1 = pd.DataFrame(X, columns=['f1', 'f2'])
df2 = pd.DataFrame(Y, columns=['target'])
oversample_df = pd.concat([df1, df2], axis=1)
plt.scatter(oversample_df['f1'], oversample_df['f2'], c=oversample_df['target'])
plt.title('Oversampled Dataset Visualization')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
"""
content.append(Paragraph("Code Snippet: Visualize Oversampled Dataset", heading_style))
content.append(Preformatted(code4, style=code_style))
content.append(Spacer(1, 12))

# Explanation of the oversampled dataset visualization
content.append(Paragraph("The scatter plot above illustrates the oversampled dataset, where both classes are now represented equally. "
                         "This balance is crucial for training machine learning models effectively.", intro_style))
content.append(Spacer(1, 12))

# Conclusion
content.append(Paragraph("Conclusion", title_style))
content.append(Paragraph("In this report, we explored the SMOTE technique for handling imbalanced datasets. "
                         "We generated a synthetic dataset, visualized it, applied SMOTE to balance the classes, and visualized the results. "
                         "This technique is essential for improving the performance of machine learning models on imbalanced data.", intro_style))
content.append(Spacer(1, 12))

content.append(Paragraph("SMOTE Glossary", title_style))
smote_glossary_terms = {
    "SMOTE": "Synthetic Minority Over-sampling Technique, a method to generate synthetic samples for the minority class in imbalanced datasets.",
    "Synthetic Sample": "An artificially created instance that is generated based on existing instances in the minority class.",
    "Interpolation": "A method used in SMOTE to create new samples by combining features of existing samples.",
    "Minority Class": "The class in a dataset that has fewer instances compared to the majority class.",
    "Majority Class": "The class in a dataset that has more instances compared to the minority class."
}
for term, definition in smote_glossary_terms.items():
    content.append(Paragraph(f"<b>{term}:</b> {definition}", normal_style))
    content.append(Spacer(1, 6))
# Build the PDF
document.build(content)

print("PDF report generated successfully.")