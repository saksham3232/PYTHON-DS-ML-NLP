from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
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
content.append(Paragraph("Flask Framework Complete Report", title_style))
content.append(Spacer(1, 0.2 * inch))

# Section 1: Overview of Flask Framework
content.append(Paragraph("Overview of Flask Framework", heading_style))
content.append(Paragraph("Definition: Flask is a complete web framework created using the Python programming language. It is primarily used for developing end-to-end web applications.", normal_style))
content.append(Paragraph("Purpose: Flask is particularly useful for data scientists and machine learning engineers who need to showcase their models through web applications.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 2: Key Components of Flask
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
User     Request
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
User     Response
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

# Section 3: Importing Flask and Creating an Application Instance
content.append(Paragraph("Importing Flask and Creating an Application Instance", heading_style))
content.append(Paragraph("To use Flask, you first need to import it and create an instance of the Flask class:", normal_style))
content.append(Spacer(1, 0.1 * inch))
code_snippet_import = """
from flask import Flask, render_template

app = Flask(__name__)
"""
content.append(Preformatted(code_snippet_import, code_style))
content.append(Spacer(1, 0.2 * inch))
content.append(Paragraph("This code imports the Flask class and the render_template function, which is used to render HTML templates. "
                          "An instance of the Flask class is created, which will be your WSGI application.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 4: Defining Routes
content.append(Paragraph("Defining Routes", heading_style))
content.append(Paragraph("You can define routes using decorators. Here are examples of defining routes for the home page and an index page:", normal_style))
content.append(Spacer(1, 0.1 * inch))
code_snippet_routes = """
@app.route('/')
def welcome():
    return '<html><H1>Welcome to the best flask course</H1></html>'

@app.route('/index')
def idx():
    return render_template('index.html')
"""
content.append(Preformatted(code_snippet_routes, code_style))
content.append(Spacer(1, 0.2 * inch))
content.append(Paragraph("The @app.route('/') decorator defines the home page route, which returns a simple HTML welcome message. "
                          "The @app.route('/index') decorator defines a route for the index page, which renders an HTML template named 'index.html'.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 5: About Page Route
content.append(Paragraph("About Page Route", heading_style))
content.append(Paragraph("You can also define additional routes for other pages. Here is an example of an about page route:", normal_style))
content.append(Spacer(1, 0.1 * inch))
code_snippet_about = """
@app.route('/about')
def about():
    return render_template('about.html')
"""
content.append(Preformatted(code_snippet_about, code_style))
content.append(Spacer(1, 0.2 * inch))
content.append(Paragraph("This code defines a route for the about page, which renders an HTML template named 'about.html'.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 6: Running the Application
content.append(Paragraph("Running the Application", heading_style))
content.append(Paragraph("Finally, you can run the application with the following code:", normal_style))
content.append(Spacer(1, 0.1 * inch))
code_snippet_run = """
if __name__ == '__main__':
    app.run(debug=True)
"""
content.append(Preformatted(code_snippet_run, code_style))
content.append(Spacer(1, 0.2 * inch))
content.append(Paragraph("This condition checks if the script is being run directly. If true, the app.run() method starts the Flask application. "
                          "The debug=True argument enables debug mode, which provides detailed error messages and automatically reloads the server when code changes are made.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 7: Summary of Key Functions
content.append(Paragraph("Summary of Key Functions", heading_style))
content.append(Paragraph("Flask: The main class used to create a Flask application instance.", normal_style))
content.append(Paragraph("render_template: A function used to render HTML templates.", normal_style))
content.append(Paragraph("@app.route(): A decorator used to bind a URL to a function, defining the routes of the application.", normal_style))
content.append(Paragraph("def function_name(): Defines a function that will be executed when the associated route is accessed.", normal_style))
content.append(Paragraph("return: Sends a response back to the client (web browser) when a route is accessed.", normal_style))
content.append(Paragraph("app.run(): Starts the Flask application server.", normal_style))
content.append(Spacer( 1, 0.2 * inch))

# Section 8: Conclusion
content.append(Paragraph("Conclusion", heading_style))
content.append(Paragraph("Flask is a powerful framework for building web applications, especially for those in data science and machine learning. Understanding WSGI and Jinja2 is crucial for effectively using Flask to create dynamic and interactive web applications. This report covers the basics of Flask web development, including how to create an application instance, define routes, and render HTML templates. Each function and decorator plays a crucial role in handling web requests and generating responses.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Build the PDF
document.build(content)

print(f"PDF report '{pdf_file}' generated successfully.")