from reportlab.lib import colors  # Importing colors module for color definitions
from reportlab.lib.pagesizes import letter  # Importing letter page size
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  # Importing styles for text formatting
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted  # Importing classes for document creation
import sys  # Importing sys module for system-specific parameters
from reportlab.lib.units import inch

# Create a PDF document
pdf_file = "16-Concurrency_UseCase.pdf"  # Name of the PDF file to be created
document = SimpleDocTemplate(pdf_file, pagesize=letter)  # Create a SimpleDocTemplate object with letter page size

# Styles
styles = getSampleStyleSheet()  # Get default styles
styles.add(ParagraphStyle(name='CodeStyle', fontName='Courier', fontSize=10, textColor=colors.black))  # Add a custom style for code

# Content
content = []  # Initialize a list to hold the content of the PDF

# Title
content.append(Paragraph("Multithreading and Multiprocessing in Python", styles['Title']))  # Add the title
content.append(Spacer(1, 0.2 * inch))  # Add space after the title

# Section 1: Multithreading for I/O-bound Tasks
content.append(Paragraph("1. Multithreading for I/O-bound Tasks", styles['Heading2']))  # Add section heading
content.append(Spacer(1, 0.1 * inch))  # Add space after the heading
content.append(Paragraph("Web scraping often involves making numerous network requests to fetch web pages. "
                         "These tasks are I/O-bound because they spend a lot of time waiting for responses from servers. "
                         "Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently.", 
                         styles['Normal']))  # Add explanation text
content.append(Spacer(1, 0.1 * inch))  # Add space after the explanation

# Code Snippet for Multithreading
multithreading_code = '''
import threading  # Importing threading module for thread management
import requests  # Importing requests library for making HTTP requests
from bs4 import BeautifulSoup  # Importing BeautifulSoup for HTML parsing

urls = [  # List of URLs to scrape
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_content(url):  # Function to fetch content from a URL
    response = requests.get(url)  # Making an HTTP GET request
    soup = BeautifulSoup(response.content, 'html.parser')  # Parsing the HTML content
    print(f"Fetched {len(soup.text)} characters from {url}")  # Printing the number of characters fetched

threads = []  # List to hold thread objects

for url in urls:  # Iterating over each URL
    thread = threading.Thread(target=fetch_content, args=(url,))  # Creating a new thread
    threads.append(thread)  # Adding thread to the list
    thread.start()  # Starting the thread

for thread in threads:  # Joining all threads
    thread.join()  # Waiting for each thread to finish

print('All Web Pages Fetched')  # Indicating that all web pages have been fetched
'''
content.append(Paragraph("Code Snippet:", styles['Normal']))  # Add label for code snippet
content.append(Spacer(1, 0.1 * inch))  # Add space before code snippet
content.append(Preformatted(multithreading_code, styles['CodeStyle']))  # Add the code snippet with preformatted style
content.append(Spacer(1, 0.2 * inch))  # Add space after the code snippet

# Section 2: Multiprocessing for CPU-bound Tasks
content.append(Paragraph("2. Multiprocessing for CPU-bound Tasks", styles['Heading2']))  # Add section heading
content.append(Spacer(1, 0.1 * inch))  # Add space after the heading
content.append(Paragraph("Factorial calculations, especially for large numbers, involve significant computational work. "
                         "Multiprocessing can be used to distribute the workload across multiple CPU cores, improving performance.", 
                         styles['Normal']))  # Add explanation text
content.append(Spacer(1, 0.1 * inch))  # Add space after the explanation

# Code Snippet for Multiprocessing
multiprocessing_code = '''
import multiprocessing  # Importing multiprocessing module for process management
import math  # Importing math module for mathematical functions
import sys  # Importing sys module for system-specific parameters
import time  # Importing time module for time-related functions

sys.set_int_max_str_digits(100000)  # Setting maximum digits for integer conversion to avoid overflow errors

def compute_factorial(number):  # Function to compute factorial of a number
    print(f"Computing factorial of {number}")  # Indicating which factorial is being computed
    result = math.factorial(number)  # Calculating factorial
    print(f"Factorial of {number} is {result}")  # Printing the result
    return result  # Returning the computed factorial

if __name__ == "__main__":  # Checking if the script is run directly
    numbers = [5000, 6000, 7000, 8000]  # List of numbers for which factorial will be computed

    start_time = time.time()  # Recording start time

    with multiprocessing.Pool() as pool:  # Creating a pool of worker processes
        results = pool.map(compute_factorial, numbers)  # Distributing the computation across processes

    end_time = time.time()  # Recording end time

    print(f"Results: {results}")  # Printing the results of the computations
    print(f"Time taken: {end_time - start_time} seconds")  # Printing the time taken for computations
'''
content.append(Paragraph("Code Snippet:", styles['Normal']))  # Add label for code snippet
content.append(Spacer(1, 0.1 * inch))  # Add space before code snippet
content.append(Preformatted(multiprocessing_code, styles['CodeStyle']))  # Add the code snippet with preformatted style
content.append(Spacer(1, 0.2 * inch))  # Add space after the code snippet

# Finalizing the PDF
document.build(content)  # Build the PDF document with the content list
print(f"{pdf_file} has been created successfully.")  # Print a success message indicating the PDF creation