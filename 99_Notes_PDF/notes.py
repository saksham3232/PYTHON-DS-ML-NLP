from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
import os

# Create a PDF document
pdf_file = "14-Multi-threading_and_Multi-processing_Report.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a list to hold the content
content = []

# Define styles
styles = getSampleStyleSheet()
title_style = styles['Title']
heading_style = styles['Heading1']
normal_style = styles['BodyText']
code_style = ParagraphStyle(name='Code', fontName='Courier', fontSize=10, textColor=colors.black)

# Title
content.append(Paragraph("Multi-threading and Multi-processing in Python", title_style))
content.append(Spacer(1, 12))

# Introduction
content.append(Paragraph("This report covers the concepts of multi-threading and multi-processing in Python, "
                         "including code examples and explanations.", normal_style))
content.append(Spacer(1, 12))

# Section 1: Multi-threading
content.append(Paragraph("1. Multi-threading", heading_style))
content.append(Spacer(1, 12))

# Code snippet for multi-threading
multi_threading_code = """\
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter:{letter}")

# create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t=time.time()

# start the thread
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

finished_time = time.time() - t
print(finished_time)
"""

# Append code with proper indentation
content.append(Preformatted(multi_threading_code, code_style))
content.append(Spacer(1, 12))

# Explanation of multi-threading
content.append(Paragraph("In this code, we create two threads: one for printing numbers and another for printing letters. "
                         "Each thread sleeps for a specified time to simulate I/O-bound tasks. The use of threads allows "
                         "the program to perform these tasks concurrently, improving throughput.", normal_style))
content.append(Spacer(1, 12))

# Built-in Function Definitions
content.append(Paragraph("Built-in Function Definitions:", heading_style))
content.append(Spacer(1, 12))
content.append(Paragraph("1. <code>start()</code>: This method is called on a thread object to start the thread's activity. "
                         "It invokes the run() method in a separate thread of control.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("2. <code>join()</code>: This method is called on a thread object to block the calling thread until the thread whose join() method is called is terminated.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("3. <code>sleep(seconds)</code>: This function from the <code>time</code> module suspends execution for the given number of seconds. "
                         "It is used to simulate a delay in the execution of the program.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("4. <code>print()</code>: This built-in function outputs the specified message to the console or other standard output device.", normal_style))
content.append(Spacer(1, 12))

# Section 2: Multi-processing
content.append(Paragraph("2. Multi-processing", heading_style))
content.append(Spacer(1, 12))

# Code snippet for multi-processing
multi_processing_code = """\
import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")

if __name__ == '__main__':
    # create 2 processes
    p1=multiprocessing.Process(target=square_numbers)
    p2=multiprocessing.Process(target=cube_numbers)
    t=time.time()

    # start the process
    p 1.start()
    p2.start()

    # Wait for the process to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)
"""

# Append code with proper indentation
content.append(Preformatted(multi_processing_code, code_style))
content.append(Spacer(1, 12))

# Explanation of multi-processing
content.append(Paragraph("In this code, we create two processes: one for calculating squares and another for cubes. "
                         "Each process runs independently, allowing for parallel execution on multiple CPU cores. "
                         "This is particularly useful for CPU-bound tasks.", normal_style))
content.append(Spacer(1, 12))

# Built-in Function Definitions
content.append(Paragraph("Built-in Function Definitions:", heading_style))
content.append(Spacer(1, 12))
content.append(Paragraph("1. <code>Process()</code>: This class from the <code>multiprocessing</code> module is used to create a new process. "
                         "It takes a target function as an argument to specify what the process should execute.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("2. <code>start()</code>: Similar to the threading module, this method starts the process's activity, invoking the target function in a separate process.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("3. <code>join()</code>: This method blocks the calling thread until the process whose join() method is called is terminated.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("4. <code>sleep(seconds)</code>: This function from the <code>time</code> module suspends execution for the given number of seconds, used to simulate delays.", normal_style))
content.append(Spacer(1, 12))
content.append(Paragraph("5. <code>print()</code>: This built-in function outputs the specified message to the console or other standard output device.", normal_style))
content.append(Spacer(1, 12))

# Conclusion
content.append(Paragraph("In conclusion, multi-threading is suitable for I/O-bound tasks, while multi-processing is "
                         "ideal for CPU-bound tasks. Understanding these concepts can help optimize performance in Python applications.", normal_style))
content.append(Spacer(1, 12))


# Build the PDF
document.build(content)

print(f"PDF report '{pdf_file}' has been generated successfully.")