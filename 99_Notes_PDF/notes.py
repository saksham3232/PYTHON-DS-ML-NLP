from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted

# Create a PDF document
pdf_file = "17-Memory_Management_Report.pdf"
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
content.append(Paragraph("Python Memory Management", title_style))
content.append(Spacer(1, 12))

# Section: Introduction
content.append(Paragraph("Introduction", heading_style))
content.append(Paragraph("Memory management in Python involves a combination of automatic garbage collection, reference counting, and various internal optimizations to efficiently manage memory allocation and deallocation. Understanding these mechanisms can help developers write more efficient and robust applications. This report will explore the key concepts of memory management in Python, including how memory is allocated and deallocated, the role of reference counting, and the importance of garbage collection.", normal_style))
content.append(Spacer(1, 12))

# Section: Key Concepts
content.append(Paragraph("Key Concepts in Python Memory Management", heading_style))
content.append(Paragraph("This section covers the fundamental concepts that underpin memory management in Python. It includes how memory is allocated and deallocated, the role of reference counting, and the importance of garbage collection in managing memory effectively.", normal_style))
content.append(Spacer(1, 12))

# Memory Allocation and Deallocation
content.append(Paragraph("Memory Allocation and Deallocation", heading_style))
content.append(Paragraph("Python manages memory automatically, allocating and deallocating memory as needed. When an object is created, Python allocates memory for it, and when it is no longer needed, the memory is freed. This automatic management helps prevent memory leaks and makes programming easier. Python uses a private heap space to store all its objects and data structures, which is managed by the memory manager. The memory manager handles the allocation of memory for Python objects and ensures that memory is used efficiently.", normal_style))
content.append(Spacer(1, 12))

# Reference Counting
content.append(Paragraph("Reference Counting", heading_style))
content.append(Paragraph("Reference counting is the primary method Python uses to manage memory. Each object maintains a count of references pointing to it. When the reference count drops to zero, the memory occupied by the object is deallocated. This mechanism is efficient but can lead to issues with circular references, where two or more objects reference each other, preventing their reference counts from reaching zero. Python's built-in garbage collector helps mitigate this issue by identifying and collecting these unreachable objects.", normal_style))
code_snippet_ref_count = """
import sys

a = []
# 2 (one for reference from 'a' and one from getrefcount())
print(sys.getrefcount(a))  # Output: 2
b = a
print(sys.getrefcount(b))  # Output: 3
del b
print(sys.getrefcount(a))  # Output: 2
"""
content.append(Preformatted(code_snippet_ref_count, code_style))
content.append(Spacer(1, 12))

# Garbage Collection
content.append(Paragraph("Garbage Collection", heading_style))
content.append(Paragraph("Python includes a cyclic garbage collector to handle reference cycles. Reference cycles occur when objects reference each other, preventing their reference counts from reaching zero. The garbage collector periodically checks for these cycles and cleans them up, ensuring that memory is freed appropriately. The garbage collector uses a technique called generational garbage collection, which categorizes objects by their lifespan and collects them based on their age, optimizing the collection process.", normal_style))
code_snippet_gc = """
import gc

# Enable garbage collection
gc.enable()
gc.collect()  # Manually trigger garbage collection

# Get garbage collection stats
print(gc.get_stats())
"""
content.append(Preformatted(code_snippet_gc, code_style))
content.append(Spacer(1, 12))

# Memory Management Best Practices
content.append(Paragraph("Memory Management Best Practices", heading_style))
content.append(Paragraph("To write efficient Python code, it's essential to follow best practices for memory management. This section outlines several strategies that can help developers optimize memory usage and avoid common pitfalls. By adhering to these practices, developers can ensure that their applications run smoothly and efficiently, minimizing memory-related issues.", normal_style))
best_practices = [
    "Use Local Variables: Local variables have a shorter lifespan and are freed sooner than global variables, reducing memory usage and improving performance.",
    "Avoid Circular References: Circular references can lead to memory leaks if not properly managed, as they prevent reference counts from reaching zero. Use weak references where appropriate.",
    "Use Generators: Generators produce items one at a time and only keep one item in memory at a time, making them memory efficient. This is particularly useful for processing large datasets.",
    "Explicitly Delete Objects: Use the del statement to delete variables and objects explicitly when they are no longer needed, helping to free up memory.",
    "Profile Memory Usage: Use memory profiling tools like tracemalloc and memory_profiler to identify memory leaks and optimize memory usage. Regular profiling can help catch issues early."
]
for practice in best_practices:
    content.append(Paragraph(f"- {practice}", normal_style))

content.append(Spacer(1, 12))

# Handled Circular Reference Example
content.append(Paragraph("Handled Circular Reference Example", heading_style))
content.append(Paragraph("This example demonstrates how circular references can occur and how Python's garbage collector can handle them. By creating two objects that reference each other, we can see how the garbage collector cleans up these references when they are no longer needed. This is an important aspect of memory management, as it helps prevent memory leaks in applications.", normal_style))
code_snippet_circular_ref = """
import gc

class MyObject:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created.")
    
    def __del__(self):
        print(f"Object {self.name} deleted")

# Create circular reference
obj1 = MyObject('obj1')
obj2 = MyObject('obj2')
obj1.ref = obj2
obj2.ref = obj1

del obj1
del obj2

# Manually trigger the garbage collection
gc.collect()
"""
content.append(Preformatted(code_snippet_circular_ref, code_style))
content.append(Spacer(1, 12))

# Generators for Memory Efficiency Example
content.append(Paragraph("Generators for Memory Efficiency Example", heading_style))
content.append(Paragraph("Generators are a powerful feature in Python that allow you to produce items one at a time, using memory efficiently. This example illustrates how to create and use a generator to iterate over a large range of numbers without consuming a lot of memory. Generators are particularly useful when working with large datasets or streams of data, as they yield items on-the-fly rather than storing them all in memory at once, which can significantly reduce memory consumption.", normal_style))
code_snippet_generators = """
# Generators allow you to produce items one at a time, using memory efficiently.
def generate_numbers(n):
    for i in range(n):
        yield i

# Using the generator
for num in generate_numbers(10000):
    print(num)
    if num > 10:
        break
"""
content.append(Preformatted(code_snippet_generators, code_style))
content.append(Spacer(1, 12))

# Profiling Memory Usage with tracemalloc
content.append(Paragraph("Profiling Memory Usage with tracemalloc", heading_style))
content.append(Paragraph("The tracemalloc module is a built-in tool in Python that helps you track memory allocations. This example shows how to use tracemalloc to take a snapshot of memory usage and analyze it, which can be invaluable for identifying memory leaks and optimizing performance. By monitoring memory allocations, developers can gain insights into their application's memory usage patterns and make informed decisions to improve efficiency.", normal_style))
code_snippet_tracemalloc = """
import tracemalloc

def create_list():
    return [i for i in range(10000)]

def main():
    tracemalloc.start()

    create_list()

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print('[TOP 10]')
    for stats in top_stats[:10]:
        print(stats)

main()
"""
content.append(Preformatted(code_snippet_tracemalloc, code_style))
content.append(Spacer(1, 12))

# Conclusion
content.append(Paragraph("Conclusion", heading_style))
content.append(Paragraph("Understanding memory management in Python is crucial for writing efficient and robust applications. By leveraging the built-in mechanisms and following best practices, developers can optimize their code and prevent memory-related issues. This report has provided an overview of key concepts, practical examples, and best practices that can help developers effectively manage memory in their Python applications.", normal_style))
content.append(Spacer(1, 12))

# Key Descriptions of Functions
content.append(Spacer(1, 12))
content.append(Paragraph("Key Descriptions of Functions", heading_style))
content.append(Paragraph("This section provides brief descriptions of key functions used in memory management, helping developers understand their purpose and usage. These functions are essential for monitoring and controlling memory usage in Python applications.", normal_style))
key_descriptions = [
    "sys.getrefcount(object): Returns the reference count of the object. This count includes the temporary reference created by this function call, which can be useful for debugging reference issues.",
    "gc.enable(): Enables automatic garbage collection, allowing Python to reclaim memory from unreachable objects. This is typically enabled by default.",
    "gc.collect(): Forces a garbage collection of unreachable objects, which can be useful for manual memory management, especially in long-running applications.",
    "gc.get_stats(): Returns statistics about the garbage collector's activity, helping developers monitor its performance and effectiveness in reclaiming memory.",
    "tracemalloc.start(): Starts tracing memory allocations, allowing developers to analyze memory usage over time and identify potential leaks.",
    "tracemalloc.take_snapshot(): Takes a snapshot of the current memory allocations, which can be compared to previous snapshots to identify changes in memory usage.",
    "snapshot.statistics('lineno'): Returns statistics about memory usage grouped by line number, helping identify memory-intensive code and optimize it."
]
for desc in key_descriptions:
    content.append(Paragraph(f"- {desc}", normal_style))

# Build the PDF
document.build(content)