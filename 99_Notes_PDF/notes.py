from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted

# Create a PDF document
pdf_file = "19-Streamlit_Report.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a list to hold the content
content = []

# Define styles
styles = getSampleStyleSheet()
normal_style = styles['Normal']  # Style for normal text
heading_style = styles['Heading1']  # Style for main headings
code_style = ParagraphStyle(name='CodeStyle', fontName='Courier', fontSize=10, textColor=colors.black)  # Style for code snippets

# Title
content.append(Paragraph("Streamlit: A Framework for Building Data Applications", heading_style))
content.append(Spacer(1, 12))  # Adds vertical space after the title

# Introduction
content.append(Paragraph("Streamlit is an open-source app framework for Machine Learning and Data Science projects. "
                         "It allows you to create beautiful web applications for your machine learning and data science projects "
                         "with simple Python scripts. Streamlit is designed to make it easy to build and share data applications, "
                         "enabling data scientists and machine learning engineers to showcase their work without needing extensive web development skills.", normal_style))
content.append(Spacer(1, 12))  # Adds space after the introduction

# Section 1: Installation
content.append(Paragraph("1. Installation", heading_style))  # Adds a section heading
content.append(Paragraph("To install Streamlit, you can use pip. Run the following command in your terminal:", normal_style))
content.append(Spacer(1, 12))  # Adds space before the code snippet
content.append(Preformatted("pip install streamlit", code_style))  # Displays the installation command in a preformatted style
content.append(Spacer(1, 12))  # Adds space after the code snippet

# Section 2: Creating a Simple App
content.append(Paragraph("2. Creating a Simple App", heading_style))  # Adds a section heading
content.append(Paragraph("Here is a simple example of a Streamlit application that displays a title and a dataframe:", normal_style))
content.append(Spacer(1, 12))  # Adds space before the code snippet
content.append(Preformatted(
    "import streamlit as st\n"
    "import pandas as pd\n"
    "import numpy as np\n\n"
    "# Title of the application\n"
    "st.title('Hello Streamlit')\n\n"
    "# Display a Simple text\n"
    "st.write('This is a simple text')\n\n"
    "# Create a simple dataframe\n"
    "df = pd.DataFrame({\n"
    "    'First Column': [1, 2, 3, 4],\n"
    "    'Second Column': [10, 20, 30, 40]\n"
    "})\n\n"
    "# Display the dataframe\n"
    "st.write('Here is the dataframe')\n"
    "st.write(df)\n\n"
    "# Create a line chart\n"
    "chart_data = pd.DataFrame(\n"
    "    np.random.randn(20, 3), columns=['a','b','c']\n"
    ")\n\n"
    "st.line_chart(chart_data)", code_style))  # Displays the code for a simple Streamlit app
content.append(Spacer(1, 12))  # Adds space after the code snippet
content.append(Paragraph("In this example, we import Streamlit and pandas, create a simple dataframe, and display it along with a line chart. "
                         "The line chart visualizes random data, demonstrating how easily Streamlit integrates data visualization into applications.", normal_style))
content.append(Spacer(1, 12))  # Adds space after the explanation

# Section 3: User Input
content.append(Paragraph("3. User Input", heading_style))  # Adds a section heading
content.append(Paragraph("Streamlit allows you to capture user input easily. Here is an example:", normal_style))
content.append(Spacer(1, 12))  # Adds space before the code snippet
content.append(Preformatted(
    "import streamlit as st\n"
    "import pandas as pd\n\n"
    "st.title('Streamlit Text Input')\n\n"
    "name = st.text_input('Enter Your Name:') \n"
    "if name:\n"
    "    st.write(f'Hello, {name}')\n\n"
    "age = st.slider('Select Your Age:', 0, 100, 25)\n"
    "st.write(f'Your age is {age}.')\n\n"
    "options = ['Python', 'Java', 'C++', 'JavaScript']\n"
    "choice = st.selectbox('Choose Your Favourite Language:', options)\n"
    "st.write(f'You Selected {choice}')\n\n"
    "data = {\n"
    "    'Name': ['John', 'Jane', 'Jake', 'Jill'],\n"
    "    'Age': [28, 24, 35, 40],\n"
    "    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']\n"
    "}\n\n"
    "df = pd.DataFrame(data)\n"
    "df.to_csv('sampledata.csv')\n"
    "st.write(df)\n\n"
    "uploaded_file = st.file_uploader('Choose a CSV File', type='csv')\n\n"
    "if uploaded_file is not None:\n"
    "    df = pd.read_csv(uploaded_file)\n"
    "    st.write(df)", code_style))  # Displays the code for capturing user input
content.append(Spacer(1, 12))  # Adds space after the code snippet
content.append(Paragraph("This code snippet captures user input for name, age, and favorite programming language, "
                         "displays a dataframe, and allows file uploads. Streamlit's interactive widgets make it easy to create dynamic applications that respond to user input.", normal_style))
content.append(Spacer(1, 12))  # Adds space after the explanation

# Section 4: File Upload
content.append(Paragraph("4. File Upload", heading_style))  # Adds a section heading
content.append(Paragraph("You can also allow users to upload files. Here is how you can do it:", normal_style))
content.append(Spacer(1, 12))  # Adds space before the code snippet
content.append(Preformatted(
    "uploaded_file = st.file_uploader('Choose a CSV File', type='csv')\n"
    "if uploaded_file is not None:\n"
    "    df = pd.read_csv(uploaded_file)\n"
    "    st.write(df)", code_style))  # Displays the code for file upload functionality
content.append(Spacer(1, 12))  # Adds space after the code snippet
content.append(Paragraph("This snippet allows users to upload a CSV file and displays its contents. "
                         "File upload functionality is essential for applications that require user data input, making Streamlit versatile for various use cases.", normal_style))
content.append(Spacer(1, 12))  # Adds space after the explanation

# Section 5: Customization and Theming
content.append(Paragraph("5. Customization and Theming", heading_style))  # Adds a section heading
content.append(Paragraph("Streamlit provides options for customizing the appearance of your application. You can change the layout, colors, and even add custom CSS styles. "
                         "For example, you can set the page title and icon using the following commands:", normal_style))
content.append(Spacer(1, 12))  # Adds space before the code snippet
content.append(Preformatted(
    "st.set_page_config(page_title='My Streamlit App', page_icon=':shark:', layout='wide')", code_style))  # Displays the code for setting page configuration
content.append(Spacer(1, 12))  # Adds space after the code snippet
content.append(Paragraph("This command sets the title and icon of the page and allows for a wide layout, enhancing the user experience.", normal_style))
content.append(Spacer(1, 12))  # Adds space after the explanation

# Conclusion
content.append(Paragraph("Conclusion", heading_style))  # Adds a conclusion heading
content.append(Paragraph("Streamlit is a powerful tool for building interactive data applications with minimal effort. "
                         "With its simple API, you can create complex applications that can visualize data, capture user input, "
                         "and much more. Its ease of use and flexibility make it an excellent choice for data scientists and developers alike.", normal_style))
content.append(Spacer(1, 12))  # Adds space after the conclusion

# References
content.append(Paragraph("References", heading_style))  # Adds a references heading
content.append(Paragraph("For more information, visit the official Streamlit documentation: "
                         "<a href='https://docs.streamlit.io'>Streamlit Documentation</a>", normal_style))

# Build the PDF
document.build(content)  # Generates the PDF document with the content

print(f"PDF report '{pdf_file}' has been generated successfully with enhanced details.")  # Confirmation message after PDF generation