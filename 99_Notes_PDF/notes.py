from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted

# Create a PDF document
pdf_file = "11-python_logging_guide.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Define styles
styles = getSampleStyleSheet()
normal_style = styles['Normal']
code_style = ParagraphStyle(
    'CodeStyle',
    parent=normal_style,
    fontName='Courier',
    fontSize=10,
    textColor=colors.black,
    spaceAfter=12,
)

# Content to be added to the PDF
content = []

# Title
content.append(Paragraph("Python Logging", styles['Title']))
content.append(Spacer(1, 12))

# Introduction
content.append(Paragraph("Logging is a crucial aspect of any application, providing a way to track events, errors, and operational information. Python's built-in logging module offers a flexible framework for emitting log messages from Python programs. In this lesson, we will cover the basics of logging, including how to configure logging, log levels, and best practices for using logging in Python applications.", normal_style))
content.append(Spacer(1, 12))

# Configuring Logging
content.append(Paragraph("Configuring Logging", styles['Heading2']))
configuring_logging_code = """\
import logging

# Configure the basic logging settings
logging.basicConfig(level=logging.DEBUG)

# Log messages with different severity levels
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
"""
content.append(Preformatted(configuring_logging_code, code_style))
content.append(Paragraph("This code configures the logging module to display messages of level DEBUG and higher.", normal_style))
content.append(Paragraph("Key Definition: logging.basicConfig(**kwargs) - Configures the logging module with the specified parameters.", normal_style))
content.append(Spacer(1, 12))

# Log Levels
content.append(Paragraph("Log Levels", styles['Heading2']))
content.append(Paragraph("Python's logging module has several log levels indicating the severity of events. The default levels are:", normal_style))
content.append(Spacer(1, 12))

# Log Levels Table
content.append(Paragraph("Level       Description", styles['Heading3']))
content.append(Paragraph("DEBUG       Detailed information, typically of interest only when diagnosing problems.", normal_style))
content.append(Paragraph("INFO        Confirmation that things are working as expected.", normal_style))
content.append(Paragraph("WARNING     An indication that something unexpected happened.", normal_style))
content.append(Paragraph("ERROR       Due to a more serious problem, the software has not been able to perform some function.", normal_style))
content.append(Paragraph("CRITICAL    A very serious error, indicating that the program itself may be unable to continue running.", normal_style))
content.append(Spacer(1, 12))

# Logging to a File
content.append(Paragraph("Logging to a File", styles['Heading2']))
logging_to_file_code = """\
import logging

# Configure logging to a file
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Log messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
"""
content.append(Preformatted(logging_to_file_code, code_style))
content.append(Paragraph("This configuration logs messages to a file named 'app.log' with a specific format.", normal_style))
content.append(Paragraph("Key Definition: logging.basicConfig(filename='app.log', ...) - Configures logging to output to a specified file.", normal_style))
content.append(Spacer(1, 12))

# Logging with Multiple Loggers
content.append(Paragraph("Logging with Multiple Loggers", styles['Heading2']))
multiple_loggers_code = """\
import logging

# create a logger for module1
logger1 = logging.getLogger('module1')
logger1.setLevel(logging.DEBUG)

# create a logger for module2
logger2 = logging.getLogger('module2')
logger2.setLevel(logging.WARNING)

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='% Y-%m-%d %H:%M:%S'
)

# log messages with different loggers
logger1.debug('This is a debug message for module1')
logger1.critical('This is a critical message for logger1')
logger2.warning('This is a warning message for module2')
logger2.error('This is an error message')
"""
content.append(Preformatted(multiple_loggers_code, code_style))
content.append(Paragraph("This example demonstrates how to create and use multiple loggers for different modules in your application.", normal_style))
content.append(Paragraph("Key Definition: logging.getLogger(name) - Retrieves a logger with the specified name.", normal_style))
content.append(Spacer(1, 12))

# Conclusion
content.append(Paragraph("Conclusion", styles['Heading2']))
content.append(Paragraph("Logging is an essential part of application development, allowing developers to monitor and debug their applications effectively.", normal_style))
content.append(Spacer(1, 12))


# Build the PDF
document.build(content)

print(f"PDF document '{pdf_file}' created successfully.")