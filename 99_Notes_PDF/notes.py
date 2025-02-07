from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch  # Import inch here
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Create a PDF document
pdf_file = "13-program_process_thread.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a list to hold the content
content = []

# Define styles
styles = getSampleStyleSheet()
normal_style = styles['Normal']
heading_style = styles['Heading1']

# Title
content.append(Paragraph("Understanding Programs, Processes, and Threads", heading_style))
content.append(Spacer(1, 0.2 * inch))

# Introduction
content.append(Paragraph("This document provides an in-depth overview of programs, processes, and threads in computing, which are fundamental concepts in software development and operating systems.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Section: What is a Program?
content.append(Paragraph("What is a Program?", heading_style))
content.append(Paragraph("A program is a sequence of instructions written in a programming language that tells a computer how to perform a specific task. Programs can range from simple scripts that automate small tasks to complex applications that manage large systems. They are executed by the computer's processor, which interprets the instructions and performs the specified operations. Examples of programming languages include Python, Java, C++, and JavaScript. Programs are typically stored in files with specific extensions, such as .py for Python or .java for Java.", normal_style))
content.append(Spacer(1, 0.1 * inch))

# Section: What is a Process?
content.append(Paragraph("What is a Process?", heading_style))
content.append(Paragraph("A process is an instance of a program that is being executed. When a program is run, the operating system creates a process that includes the program's code, its current activity, and the resources it needs to execute. Each process has its own memory space, which means that one process cannot directly access the memory of another process. This isolation helps prevent errors and security issues. Processes are managed by the operating system, which allocates resources such as CPU time and memory to each process. Each process has a unique Process ID (PID) that the operating system uses to track it.", normal_style))
content.append(Spacer(1, 0.1 * inch))

# Section: What is a Thread?
content.append(Paragraph("What is a Thread?", heading_style))
content.append(Paragraph("A thread is the smallest unit of execution within a process. A process can contain multiple threads, which share the same memory space but can execute independently. Threads are used to perform tasks concurrently, allowing for more efficient use of resources. For example, a web browser may use multiple threads to load different parts of a webpage simultaneously. Threads have their own stack and registers, but they share the code segment, data segment, and heap memory of the process. This shared memory allows for efficient communication between threads but also requires careful management to avoid issues such as race conditions.", normal_style))
content.append(Spacer(1, 0.1 * inch))

# Section: Single-Threaded Process
content.append(Paragraph("Single-Threaded Process", heading_style))
content.append(Paragraph("In a single-threaded process, there is only one thread of execution. This means that tasks are performed sequentially, one after the other. While this approach is simpler and easier to manage, it can lead to inefficiencies, especially if a task takes a long time to complete. For example, if a single-threaded application is performing a time-consuming operation, it may become unresponsive to user input until the operation is finished. Single-threaded processes are often easier to debug and maintain, but they may not fully utilize the capabilities of modern multi-core processors.", normal_style))
content.append(Spacer(1, 0.1 * inch))

# Section: Multi-Threaded Process
content.append(Paragraph("Multi-Threaded Process", heading_style))
content.append(Paragraph("In a multi-threaded process, multiple threads can execute concurrently. This allows for more efficient use of CPU resources, as multiple tasks can be performed at the same time. For example, a multi-threaded application can handle user input while simultaneously performing background calculations. However, managing multiple threads can introduce complexity, such as the need for synchronization to prevent data corruption when threads access shared resources. Common synchronization mechanisms include mutexes, semaphores, and condition variables. Multi-threading can improve the responsiveness of applications, especially in user interfaces, where tasks like loading data can occur in the background while the user continues to interact with the application.", normal_style))
content.append(Spacer(1, 0.1 * inch))

# Section: Examples
content.append(Paragraph("Examples of Processes and Threads", heading_style))
content.append(Paragraph("1. Opening a web browser (e.g., Google Chrome) creates a process. Each tab in the browser may run as a separate thread, allowing for concurrent loading of web pages. This means that if one tab is loading a resource, the other tabs remain responsive to user actions.", normal_style))
content.append(Paragraph("2. A text editor may run a spell checker in a separate thread while allowing the user to continue typing in the main thread. This ensures that the application remains responsive while performing background tasks.", normal_style))
content.append(Spacer(1, 0.2 * inch))

# Final notes
content.append(Paragraph("In the next section, we will explore practical applications of multithreading and multiprocessing in Python, including how to implement these concepts in real-world applications.", normal_style))

# Build the PDF
document.build(content)

print(f"PDF generated successfully: {pdf_file}")