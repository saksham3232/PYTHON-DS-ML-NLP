from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.units import inch

# Create a PDF document
pdf_file = "18-Flask_Complete_Report.pdf"
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
User       Request
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
User       Response
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
content.append(Spacer(1, 0.2 * inch))

# Section 8: Conclusion
content.append(Paragraph("Conclusion", heading_style))
content.append(Paragraph("Flask is a powerful framework for building web applications, especially for those in data science and machine learning. Understanding WSGI and Jinja2 is crucial for effectively using Flask to create dynamic and interactive web applications. This report covers the basics of Flask web development, including how to create an application instance, define routes, and render HTML templates. Each function and decorator plays a crucial role in handling web requests and generating responses.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 9: Introduction to Flask Web Development
content.append(Paragraph("Flask Web Development", title_style))
content.append(Spacer(1, 12))

# Section 10: Setting Up Flask
content.append(Paragraph("Setting Up Flask", heading_style))
content.append(Paragraph("To set up a Flask application, you need to install Flask first. You can do this using pip:", normal_style))
content.append(Spacer(1, 12))

# Code Snippet
code_snippet_1 = """pip install Flask"""
content.append(Paragraph(code_snippet_1, code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This command installs Flask and its dependencies.", normal_style))
content.append(Spacer(1, 12))

# Section 11: Creating a Simple Flask App
content.append(Paragraph("Creating a Simple Flask App", heading_style))
content.append(Paragraph("Here is a simple Flask application that returns 'Hello, World!':", normal_style))
content.append(Spacer(1, 12))

# Code Snippet
code_snippet_2 = """from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)"""
content.append(Preformatted(code_snippet_2, code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("In this code, we create a Flask application and define a route that returns "
                          "'Hello, World!' when accessed.", normal_style))
content.append(Spacer(1, 12))

# Section 12: Running the Application
content.append(Paragraph("Running the Application", heading_style))
content.append(Paragraph("To run the application, save the code in a file named 'app.py' and execute it:", normal_style))
content.append(Spacer(1, 12))

# Code Snippet
code_snippet_3 = """python app.py"""
content.append(Paragraph(code_snippet_3, code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This command starts the Flask development server, and you can access the app at "
                          "http://999.9.9.9:9999.", normal_style))
content.append(Spacer(1, 12))

# Section 13: Understanding Routes
content.append(Paragraph("Understanding Routes", heading_style))
content.append(Paragraph("In Flask, routes are defined using the @app.route decorator. This allows you to map "
                          "URLs to Python functions. For example:", normal_style))
content.append(Spacer(1, 12))

# Code Snippet
code_snippet_4 = """@app.route('/about')
def about():
    return render_template('about.html')"""
content.append(Preformatted(code_snippet_4, code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This code defines a route for the '/about' URL, which renders an 'about.html' template.", normal_style))
content.append(Spacer(1, 12))

# Section 14: GET and POST Methods
content.append(Paragraph("GET and POST Methods", heading_style))
content.append(Paragraph("In web development, GET and POST are two common HTTP methods used to send and receive data between a client and a server.", normal_style))
content.append(Spacer(1, 12))

# GET Method
content.append(Paragraph("GET Method:", heading_style))
content.append(Paragraph("1. The GET method is used to request data from a specified resource.", normal_style))
content.append(Paragraph("2. Data sent using the GET method is appended to the URL as query parameters.", normal_style))
content.append(Paragraph("3. It is generally used for retrieving data and should not have side effects (i.e., it should not change the state of the server).", normal_style))
content.append(Paragraph("4. Example: Accessing a URL like 'http://example.com/page?name=John' uses the GET method.", normal_style))
content.append(Spacer(1, 12))

# POST Method
content.append(Paragraph("POST Method:", heading_style))
content.append(Paragraph("1. The POST method is used to send data to a server to create or update a resource.", normal_style))
content.append(Paragraph("2. Data sent using the POST method is included in the body of the request, not in the URL.", normal_style))
content.append(Paragraph("3. It is generally used for submitting forms and can change the state of the server.", normal_style))
content.append(Paragraph("4. Example: Submitting a form with user data uses the POST method.", normal_style))
content.append(Spacer(1, 12))

# Differences between GET and POST
content.append(Paragraph("Differences between GET and POST:", heading_style))
content.append(Paragraph("1. Data Transmission: GET appends data to the URL, while POST sends data in the request body.", normal_style))
content.append(Paragraph("2. Data Length: GET has limitations on the amount of data that can be sent (URL length), while POST can send larger amounts of data.", normal_style))
content.append(Paragraph("3. Security: GET is less secure as data is visible in the URL, while POST is more secure as data is not exposed in the URL.", normal_style))
content.append(Paragraph("4. Use Cases: GET is used for retrieving data, while POST is used for submitting data.", normal_style))
content.append(Spacer(1, 12))

# Section 15: Complete Flask Application Example
content.append(Paragraph("Complete Flask Application Example", heading_style))
content.append(Paragraph("Here is the complete code for a simple Flask application:", normal_style))
content.append(Spacer(1, 12))

# Code Snippet
complete_code_snippet = """from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the Flask Course</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)"""
content.append(Preformatted(complete_code_snippet, code_style))
content.append(Spacer(1, 12))

# Explanation
content.append(Paragraph("This code creates a Flask application with multiple routes, including a welcome page, "
                          "an index page, an about page, and a form page that accepts user input.", normal_style))
content.append(Spacer(1, 12))

# Section 16: HTML Templates
content.append(Paragraph("HTML Templates", heading_style))
content.append(Paragraph("The following HTML templates are used in the Flask application:", normal_style))
content.append(Spacer(1, 12))

# HTML Template for index.html
content.append(Paragraph("index.html", heading_style))
index_html = """<html lang="en"><head>
    <meta charset="UTF-8">
    <title>Flask App</title>
</head>
<body>
    <h1>Welcome to My Flask App!</h1>
    <p>This is a simple web application built with Flask.</p>
</body></html>"""
content.append(Preformatted(index_html, code_style))
content.append(Spacer(1, 12))

# HTML Template for about.html
content.append(Paragraph("about.html", heading_style))
about_html = """<html lang="en"><head>
    <meta charset="UTF-8">
    <title>About</title>
</head>
<body>
    <h1>About</h1>
    <p>This is the about page of my Flask app.</p>


</body></html>"""
content.append(Preformatted(about_html, code_style))
content.append(Spacer(1, 12))

# HTML Template for form.html
content.append(Paragraph("form.html", heading_style))
form_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Form</title>
</head>
<body>
    <h1>Submit a Form</h1>
    <form action="/submit" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>
</body>
</html>"""
content.append(Preformatted(form_html, code_style))
content.append(Spacer(1, 12))



# Title
content.append(Paragraph("Flask Advanced Concepts Report", title_style))
content.append(Spacer(1, 0.2 * inch))

# Section 1: Introduction
content.append(Paragraph("Introduction", heading_style))
content.append(Paragraph("This report covers advanced concepts in Flask, including dynamic URL building, variable rules, and the Jinja2 template engine. "
                          "We will explore how to create a Flask application that utilizes these features effectively.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 2: Building URL Dynamically
content.append(Paragraph("Building URL Dynamically", heading_style))
content.append(Paragraph("In Flask, you can build URLs dynamically using the `url_for` function. This function generates a URL to the specified function based on the function name and any parameters you provide.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Code Snippet for Building URL Dynamically
code_snippet_url = """
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science) / 4
    else:
        return render_template('getresult.html')
    
    return redirect(url_for('successres', score=total_score))
"""
content.append(Preformatted(code_snippet_url, code_style))
content.append(Spacer(1, 0.2 * inch))

# Explanation for Building URL Dynamically
content.append(Paragraph("Explanation:", heading_style))
content.append(Paragraph("1. The `submit` function handles both GET and POST requests. When the form is submitted (POST), it calculates the average score from the input fields.", normal_style))
content.append(Paragraph("2. If the request method is GET, it renders a template named 'getresult.html'.", normal_style))
content.append(Paragraph("3. After calculating the total score, it redirects to the 'successres' route using `url_for`, passing the total score as a parameter.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 3: Variable Rule
content.append(Paragraph("Variable Rule", heading_style))
content.append(Paragraph("Flask allows you to define dynamic routes using variable rules. You can capture values from the URL and pass them to your view functions.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Code Snippet for Variable Rule
code_snippet_variable_rule = """
@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('result.html', results=res)
"""
content.append(Preformatted(code_snippet_variable_rule, code_style))
content.append(Spacer(1, 0.2 * inch))

# Explanation for Variable Rule
content.append(Paragraph("Explanation:", heading_style))
content.append(Paragraph("1. The `success` function is defined with a variable rule that captures an integer score from the URL.", normal_style))
content.append(Paragraph("2. It checks if the score is greater than or equal to 50 and sets the result to 'PASSED' or 'FAILED'.", normal_style))
content.append(Paragraph("3. Finally, it renders a template named 'result.html', passing the result as a variable.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 4: Jinja2 Template Engine
content.append(Paragraph("Jinja2 Template Engine", heading_style))
content.append(Paragraph("Jinja2 is a powerful template engine for Python that allows you to create dynamic HTML pages. It uses the following syntax:", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Jinja2 Syntax
content.append(Paragraph("Jinja2 Syntax:", heading_style))
content.append(Paragraph("1. {{ ... }}: Used to print output in HTML.", normal_style))
content.append(Paragraph("2. {% ... %}: Used for control structures like conditions and loops.", normal_style))
content.append(Paragraph("3. {# ... #}: Used for comments.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Code Snippet for Jinja2 Template Engine
code_snippet_jinja = """
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template('about.html')
"""
content.append(Preformatted(code_snippet_jinja, code_style))
content.append(Spacer(1, 0.2 * inch))

# Explanation for Jinja2 Template Engine
content.append(Paragraph("Explanation:", heading_style))
content.append(Paragraph("1. The `about` function renders a template named 'about.html'.", normal_style))
content.append(Paragraph("2. Jinja2 allows you to include dynamic content in your HTML templates, making it easy to create interactive web pages.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 5: Complete Flask Application Example
content.append(Paragraph("Complete Flask Application Example", heading_style))
content.append(Paragraph("Here is the complete code for a Flask application that demonstrates dynamic URL building and Jinja2 templates:", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Complete Code Snippet
complete_code_snippet = """from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('result.html', results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ''
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp = {'score': score, 'res': res}

    return render_template('result1.html', results=exp)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science) / 4
    else:
        return render_template('getresult.html')
    
    return redirect(url_for('successres', score=total_score))

if __name__ == '__main__':
    app.run(debug=True)
"""
content.append(Preformatted(complete_code_snippet, code_style))
content.append(Spacer(1, 0.2 * inch))

# Explanation for Complete Flask Application
content.append(Paragraph("Explanation:", heading_style))
content.append(Paragraph("1. The application starts by importing necessary modules from Flask.", normal_style))
content.append(Paragraph("2. The `welcome` function returns a simple HTML welcome message.", normal_style))
content.append(Paragraph("3. The `index` function renders the 'index.html' template.", normal_style))
content.append(Paragraph("4. The `about` function renders the 'about.html' template.", normal_style))
content.append(Paragraph("5. The `success` and `successres` functions handle dynamic routes and render results based on the score.", normal_style))
content.append(Paragraph("6. The `submit` function processes form data, calculates the average score, and redirects to the appropriate result page.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 6: HTML Templates
content.append(Paragraph("HTML Templates", heading_style))
content.append(Paragraph("The following HTML templates are used in the Flask application:", normal_style))
content.append(Spacer(1, 0.2 * inch))

# HTML Template for index.html
content.append(Paragraph("index.html", heading_style))
index_html = """<html lang="en"><head>
    <meta charset="UTF-8">
    <title>Flask App</title>
</head>
<body>
    <h1>Welcome to My Flask App!</h1>
    <p>This is a simple web application built with Flask.</p>
</body></html>"""
content.append(Preformatted(index_html, code_style))
content.append(Spacer(1, 0.2 * inch))

# HTML Template for about.html
content.append(Paragraph("about.html", heading_style))
about_html = """<html lang="en"><head>
    <meta charset="UTF-8">
    <title>About</title>
</head>
<body>
    <h1>About</h1>
    <p>This is the about page of my Flask app.</p>


</body></html>"""
content.append(Preformatted(about_html, code_style))
content.append(Spacer(1, 0.2 * inch))

# HTML Template for result.html
content.append(Paragraph("result.html", heading_style))
result_html = """<h1>
    Based on the marks, You have {{ results }}

    {% if results>=50 %}
    <h1>You have passed with marks {{ results }}</h1>
    {% else %}
    <h2>You have failed with marks {{ results }}</h2>
    {% endif %}
</h1>"""
content.append(Preformatted(result_html, code_style))
content.append(Spacer(1, 0.2 * inch))

# HTML Template for result1.html
content.append(Paragraph("result1.html", heading_style))
result1_html = """<html>
    <h2>Final Results</h2>
    <body>
        
        {% for key,value in results.items() %}
        {#This is the comment section #}
        <h1>{{ key }}</h1>
        <h2>{{ value }}</h2>

        {% endfor %}
    </body>
</html>"""
content.append(Preformatted(result1_html, code_style))
content.append(Spacer(1, 0.2 * inch))

# HTML Template for getresult.html
content.append(Paragraph("getresult.html", heading_style))
getresult_html = """<!DOCTYPE html>
<html lang="en">
<body>
    
    <h2>HTML FORMS</h2>

    <form action="/submit" method="post">
        <label for="Science">Science:</label><br>
        <input type="text" name="science" id="science" value="0"><br><br>
        <label for="Maths">Maths:</label><br>
        <input type="text" name="maths" id="maths" value="0"><br><br>
        <label for="C ">C:</label><br>
        <input type="text" id="c" name="c" value="0"><br><br>
        <label for="datascience">Data Science:</label><br>
        <input type="text" id="datascience" name="datascience" value="0"><br><br>
        <input type="submit" value="Submit">
    </form>

    <p>If you click the "Submit" button, the form-data will be sent to a page called "/submit".</p>
</body>
</html>"""
content.append(Preformatted(getresult_html, code_style))
content.append(Spacer(1, 0.2 * inch))


# Title
content.append(Paragraph("Flask To-Do List API Report", title_style))
content.append(Spacer(1, 0.2 * inch))

# Section 1: Overview of Flask Framework
content.append(Paragraph("1. Overview of Flask Framework", heading_style))
content.append(Paragraph("Flask is a micro web framework written in Python. It is designed to make it easy to build web applications quickly and with minimal code.", normal_style))
content.append(Paragraph("Flask is particularly useful for data scientists and machine learning engineers who need to showcase their models through web applications.", normal_style))
content.append(Paragraph("Flask is lightweight and modular, allowing developers to choose the components they need for their applications.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 2: Key Concepts
content.append(Paragraph("2. Key Concepts", heading_style))
content.append(Paragraph("- **Flask**: A micro web framework for Python that allows for the creation of web applications.", normal_style))
content.append(Paragraph("- **HTTP Methods**: The API utilizes various HTTP methods to interact with resources:", normal_style))
content.append(Paragraph("  - **GET**: Retrieve data from the server.", normal_style))
content.append(Paragraph("  - **POST**: Send data to the server to create a new resource.", normal_style))
content.append(Paragraph("  - **PUT**: Update an existing resource on the server.", normal_style))
content.append(Paragraph("  - **DELETE**: Remove a resource from the server.", normal_style))
content.append(Paragraph("- **JSON**: The API communicates using JSON (JavaScript Object Notation), a lightweight data interchange format.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 3: Code Explanation
content.append(Paragraph("3. Code Explanation", heading_style))

# Complete Code
content.append(Paragraph("3.1 Complete Code", heading_style))
complete_code = """
from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial Data in my to do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}    
]

@app.route('/')
def home():
    return 'Welcome To The Sample TO-DO List App'

# GET: Retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET: Retrieve a specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "item not found"})
    return jsonify(item)

# POST: Create a new task - API
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "item not found"})
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name": request.json['name'],
        'description': request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

# PUT: Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# DELETE: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"result": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
"""
content.append(Preformatted(complete_code, code_style))
content.append(Spacer(1, 0.2 * inch))

# Explanation of the Code
content.append(Paragraph("3.2 Explanation of the Code", heading_style))
explanation_text = (
    "This code implements a simple To-Do List API using Flask. It allows users to manage tasks "
    "with the following functionalities:<br/>"
    "- **Home Route**: Returns a welcome message.<br/>"
    "- **GET /items**: Retrieves all items in the to-do list.<br/>"
    "- **GET /items/<item_id>**: Retrieves a specific item by its ID.<br/>"
    "- **POST /items**: Creates a new task. The request must include a JSON body with a 'name' and optionally a 'description'.<br/>"
    "- **PUT /items/<item_id>**: Updates an existing item based on its ID.<br/>"
    "- **DELETE /items/<item_id>**: Deletes an item based on its ID.<br/>"
    "<br/>"
    "The API uses a list of dictionaries to store the tasks, where each task has an ID, name, and description. "
    "The ID is automatically incremented when a new task is created."
)
content.append(Paragraph(explanation_text, normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 4: Testing the API
content.append(Paragraph("4. Testing the API", heading_style))
testing_text = (
    "You can test the API using tools like Postman or curl. Here are some example requests:<br/>"
    "- **GET all items**: `GET http://999.9.9.9:9999/items`<br/>"
    "- **GET item by ID**: `GET http://999.9.9.9:9999/items/1`<br/>"
    "- **POST new item**: `POST http://999.9.9.9:9999/items` with JSON body `{ \"name\": \"Item 3\", \"description\": \"This is item 3\" }`<br/>"
    "- **PUT update item**: `PUT http://999.9.9.9:9999/items/1` with JSON body `{ \"name\": \"Updated Item 1\", \"description\": \"Updated description\" }`<br/>"
    "- **DELETE item**: `DELETE http://999.9.9.9:9999/items/1`<br/>"
)
content.append(Paragraph(testing_text, normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section 5: Conclusion
content.append(Paragraph("5. Conclusion", heading_style))
conclusion_text = (
    "This Flask To-Do List API demonstrates how to create a simple RESTful API that allows users to manage tasks. "
    "The use of HTTP methods and JSON for data interchange makes it a practical example of web service development. "
    "Flask's simplicity and flexibility make it an excellent choice for building web applications."
)
content.append(Paragraph(conclusion_text, normal_style))
content.append(Spacer(1, 0.2 * inch))


# Build the PDF
document.build(content)

print(f"PDF report '{pdf_file}' has been created successfully.")