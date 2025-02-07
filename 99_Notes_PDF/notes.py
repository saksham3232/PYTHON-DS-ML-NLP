from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def create_pdf_report(pdf_file):
    """Create a PDF report on Python Logging."""
    document = SimpleDocTemplate(pdf_file, pagesize=letter)
    content = []

    # Define styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    heading_style = styles['Heading1']
    normal_style = styles['BodyText']
    code_style = ParagraphStyle(name='Code', fontName='Courier', fontSize=10, textColor=colors.black)

    # Title
    content.append(Paragraph("Python Logging", title_style))
    content.append(Spacer(1, 12))

    # Introduction
    content.append(Paragraph("Logging is a crucial aspect of any application, providing a way to track events, errors, and operational information. Python's built-in logging module offers a flexible framework for emitting log messages from Python programs. In this lesson, we will cover the basics of logging, including how to configure logging, log levels, and best practices for using logging in Python applications.", normal_style))
    content.append(Spacer(1, 12))

    # Section: Configuring Logging
    content.append(Paragraph("Configuring Logging", heading_style))
    content.append(Paragraph("To configure logging in Python, you can use the built-in logging module. Here is an example of basic configuration:", normal_style))
    
    # Code snippet for basic logging configuration
    code_snippet_1 = [
        "import logging",
        "",
        "# Configure the basic logging settings",
        "logging.basicConfig(level=logging.DEBUG)",
        "",
        "# Log messages with different severity levels",
        "logging.debug('This is a debug message')",
        "logging.info('This is an info message')",
        "logging.warning('This is a warning message')",
        "logging.error('This is an error message')",
        "logging.critical('This is a critical message')"
    ]
    
    for line in code_snippet_1:
        content.append(Paragraph(line, code_style))
    
    content.append(Spacer(1, 12))
    content.append(Paragraph("This code configures the logging module to display messages of level DEBUG and higher.", normal_style))
    content.append(Spacer(1, 12))

    # Section: Log Levels
    content.append(Paragraph("Log Levels", heading_style))
    content.append(Paragraph("Python's logging module has several log levels indicating the severity of events. The default levels are:", normal_style))
    
    # Log levels table
    log_levels = [
        ("Level", "Description"),
        ("DEBUG", "Detailed information, typically of interest only when diagnosing problems."),
        ("INFO", "Confirmation that things are working as expected."),
        ("WARNING", "An indication that something unexpected happened."),
        ("ERROR", "Due to a more serious problem, the software has not been able to perform some function."),
        ("CRITICAL", "A very serious error, indicating that the program itself may be unable to continue running.")
    ]
    
    table = Table(log_levels)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    content.append(table)
    content.append(Spacer(1, 12))

    # Section: Logging to a File
    content.append(Paragraph("Logging to a File", heading_style))
    content.append(Paragraph("You can also log messages to a file by configuring the logging module as follows:", normal_style))
    
    # Code snippet for logging to a file
    code_snippet_2 = [
        "import logging",
        "",
        "# Configure logging to a file",
        "logging.basicConfig(",
        "    filename='app.log',",
        "    filemode='w',",
        "    level=logging.DEBUG,",
        "    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',",
        "    datefmt='%Y-%m-%d %H:%M:%S'",
        ")",
        "",
        "# Log messages",
        "logging.debug('This is a debug message')",
        "logging.info('This is an info message')",
        "logging.warning('This is a warning message')",
        "logging.error('This is an error message')",
        "logging.critical('This is a critical message')"
    ]
    
    for line in code_snippet_2:
        content.append(Paragraph(line, code_style))
    
    content.append(Spacer(1, 12))
    content.append(Paragraph("This configuration logs messages to a file named 'app.log' with a specific format.", normal_style))
    content.append(Spacer(1, 12))

    # Conclusion
    content.append(Paragraph("Conclusion", heading_style))
    content.append(Paragraph("Logging is an essential part of application development, allowing developers to monitor and debug their applications effectively.", normal_style))
    content.append(Spacer(1, 12))

    # Build the PDF
    document.build(content)

# Generate the PDF report
pdf_file = "11-python_logging_report.pdf"
create_pdf_report(pdf_file)

print(f"PDF report '{pdf_file}' has been generated successfully.")