from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.lib.units import inch

# Create a PDF document
pdf_file = "18-Flask_Framework.pdf"
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
content.append(Paragraph("Flask Framework Introduction Notes", title_style))
content.append(Spacer(1, 0.2 * inch))

# Overview of Flask Framework
content.append(Paragraph("Overview of Flask Framework", heading_style))
content.append(Paragraph("Definition: Flask is a complete web framework created using the Python programming language. It is primarily used for developing end-to-end web applications.", normal_style))
content.append(Paragraph("Purpose: Flask is particularly useful for data scientists and machine learning engineers who need to showcase their models through web applications.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Key Components of Flask
content.append(Paragraph("Key Components of Flask", heading_style))

# WSGI (Web Server Gateway Interface)
content.append(Paragraph("WSGI (Web Server Gateway Interface)", heading_style))
content.append(Paragraph("Definition: WSGI is a protocol that facilitates communication between the web server and the web application.", normal_style))
content.append(Paragraph("Functionality:", normal_style))
content.append(Paragraph("1. When a user sends a request (e.g., accessing a homepage), the request is received by the web server.", normal_style))
content.append(Paragraph("2. The web server uses WSGI to redirect the request to the Flask web application.", normal_style))
content.append(Paragraph("3. The web application processes the request and sends a response back to the web server, which then delivers it to the user.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# WSGI Diagram (Preformatted)
content.append(Paragraph("Diagram: WSGI Communication Flow", heading_style))
wsgi_diagram_ascii = """
1. WSGI->
User   Request
    |
    v
+-----------+
| Web Server|
+-----------+
    |
    v
+-----------+
|   WSGI   |
+-----------+
    |
    v
+-----------+
| Flask App |
+-----------+
    |
    v
User   Response
"""
content.append(Preformatted(wsgi_diagram_ascii, code_style))
content.append(Spacer(1, 0.2 * inch))

# Jinja2 Template Engine
content.append(Paragraph("Jinja2 Template Engine", heading_style))
content.append(Paragraph("Definition: Jinja2 is a web template engine that combines web templates with data sources to create dynamic web pages.", normal_style))
content.append(Paragraph("Functionality:", normal_style))
content.append(Paragraph("1. Jinja2 allows developers to create templates that can be populated with data from various sources (e.g., SQL databases, CSV files, machine learning models).", normal_style))
content.append(Paragraph("2. This enables the creation of dynamic web pages that can change based on user input or data retrieved from a data source.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Jinja2 Diagram (Preformatted)
content.append(Paragraph("Diagram: Jinja2 Template Engine Flow", heading_style))
jinja_diagram_ascii = """
2. JINJA2->
+-----------+
| Web Page  |
| (Template)|
+-----------+
    |
    v
+-----------+
| Data Source|
| (e.g., DB) |
+-----------+
    |
    v
+-----------+
| Jinja2    |
| Template   |
+-----------+
    |
    v
Dynamic Web Page
"""
content.append(Preformatted(jinja_diagram_ascii, code_style))
content.append(Spacer(1, 0.2 * inch))

# Practical Applications
content.append(Paragraph("Practical Applications", heading_style))
content.append(Paragraph("Flask is essential for creating web applications that interact with machine learning models. For example:", normal_style))
content.append(Paragraph("- Image Classification: A web page with an upload button allows users to upload images, which are then processed by a machine learning model to classify the image (e.g., dog or cat).", normal_style))
content.append(Paragraph("- User Authentication: A login form that authenticates users against a database.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Conclusion
content.append(Paragraph("Conclusion", heading_style))
content.append(Paragraph("Flask is a powerful framework for building web applications, especially for those in data science and machine learning. Understanding WSGI and Jinja2 is crucial for effectively using Flask to create dynamic and interactive web applications.", normal_style))

# Build the PDF
document.build(content)

print(f"PDF report '{pdf_file}' has been generated successfully.")