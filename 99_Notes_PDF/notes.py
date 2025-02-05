from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import pandas as pd

# Create a PDF document
pdf_file = "data_reading_report.pdf"
document = SimpleDocTemplate(pdf_file, pagesize=letter)

# Create a list to hold the content
content = []

# Define styles
styles = getSampleStyleSheet()
normal_style = styles['Normal']
heading_style = styles['Heading1']
code_style = ParagraphStyle(name='CodeStyle', fontName='Courier', fontSize=10, textColor=colors.black)
output_style = ParagraphStyle(name='OutputStyle', fontName='Courier', fontSize=10, textColor=colors.green)

# Title
content.append(Paragraph("Reading Data From Different Sources", heading_style))
content.append(Spacer(1, 12))

# Section 1: JSON Data
content.append(Paragraph("1. Reading JSON Data", heading_style))
content.append(Spacer(1, 12))
json_code = '''import pandas as pd
from io import StringIO

Data = '{"employee_name": "James", "email": "james@gmail.com", "job_profile": [{"title1":"Team Lead", "title2":"Sr. Developer"}]}'
df = pd.read_json(StringIO(Data))
df'''
content.append(Paragraph("Code:", normal_style))
content.append(Paragraph(json_code.replace('\n', '<br />'), code_style))  # Replace newlines with HTML line breaks
content.append(Spacer(1, 12))
content.append(Paragraph("Output:", normal_style))
output_json = '''  employee_name            email                                        job_profile
0         James  james@gmail.com  [{'title1': 'Team Lead', 'title2': 'Sr. Developer'}]'''
content.append(Paragraph(output_json.replace('\n', '<br />'), output_style))  # Replace newlines with HTML line breaks
content.append(Spacer(1, 12))

# Definition and Syntax for pd.read_json
content.append(Paragraph("Definition: Reads a JSON string or file and converts it into a DataFrame.", normal_style))
content.append(Paragraph("Syntax: pd.read_json(path_or_buf, orient=None, ...)", normal_style))
content.append(Spacer(1, 12))

# Section 2: CSV Data
content.append(Paragraph("2. Reading CSV Data from a URL", heading_style))
content.append(Spacer(1, 12))
csv_code = '''df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
df.head()'''
content.append(Paragraph("Code:", normal_style))
content.append(Paragraph(csv_code.replace('\n', '<br />'), code_style))  # Replace newlines with HTML line breaks
content.append(Spacer(1, 12))
content.append(Paragraph("Output:", normal_style))
output_csv = '''   0     1     2     3     4    5     6     7     8     9     10    11    12    13
0  1  14.23  1.71  2.43  15.6  127  2.80  3.06  0.28  2.29  5.64  1.04  3.92  1065
1  1  13.20  1.78  2.14  11.2  100  2.65  2.76  0.26  1.28  4.38  1.05  3.40  1050
2  1  13.16  2.36  2.67  18.6  101  2.80  3.24  0.30  2.81  5.68  1.03  3.17  1185
3  1  14.37  1.95  2.50  16.8  113  3.85  3.49  0.24  2.18  7.80  0.86  3.45  1480
4  1  13.24  2.59  2.87  21.0  118  2.80  2.69  0.39  1.82  4.32  1.04  2.93   735'''
content.append(Paragraph(output_csv.replace('\n', '<br />'), output_style))  # Replace newlines with HTML line breaks
content.append(Spacer(1, 12))

# Definition and Syntax for pd.read_csv
content.append(Paragraph("Definition: Reads a comma-separated values (CSV) file into a DataFrame.", normal_style))
content.append(Paragraph("Syntax: pd.read_csv(filepath_or_buffer, sep=',', ...)", normal_style))
content.append(Spacer(1, 12))

# Section 3: HTML Data
content.append(Paragraph("3. Reading HTML Tables from a URL", heading_style))
content.append(Spacer(1, 12))
html_code = '''url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"
df = pd.read_html(url)'''
content.append(Paragraph("Code:", normal_style))
content.append(Paragraph(html_code.replace('\n', '<br />'), code_style))  # Replace newlines with HTML line breaks
content.append(Spacer(1, 12))
content.append(Paragraph("Output:", normal_style))
output_html = '''                                Bank Name                City      State   Cert  \
0                     Pulaski Savings Bank             Chicago  Illinois  28611   
1              The First National Bank of Lindsay              Lindsay   Oklahoma  4134   
2  Republic First Bank dba Republic Bank         Philadelphia  Pennsylvania  27332   
3                          Citizens Bank              Sac City       Iowa   8758   
4                  Heartland Tri-State Bank             Elkhart     Kansas  25851   

                     Acquiring Institution     Closing Date   Fund  
0                             Millennium Bank  January 17, 2025  10548  
1                     First Bank & Trust Co., Duncan, OK  October 18, 2024  10547  
2                     Fulton Bank, National Association   April 26, 2024  10546  
3                     Iowa Trust & Savings Bank   November 3, 2023  10545  
4                     Dream First Bank, N.A.   July 28, 2023  10544  '''
content.append(Paragraph(output_html.replace('\n', '<br />'), output_style))  # Replace newlines with HTML line breaks
content.append(Spacer(1, 12))

# Definition and Syntax for pd.read_html
content.append(Paragraph("Definition: Reads HTML tables from a specified URL or file and returns a list of DataFrames.", normal_style))
content.append(Paragraph("Syntax: pd.read_html(io, match=None, ...)", normal_style))
content.append(Spacer(1, 12))

# Section 4: Excel Data
content.append(Paragraph("4. Reading Excel Data", heading_style))
content.append(Spacer(1, 12))
excel_code = '''df_excel = pd.read_excel('data.xlsx')
df_excel'''
content.append(Paragraph("Code:", normal_style))
content.append(Paragraph(excel_code.replace('\n', '<br />'), code_style))  # Replace newlines with HTML line breaks
content.append(Spacer(1, 12))
content.append(Paragraph("Output:", normal_style))
output_excel = '''      Name  Age
0   Krish   32
1    Jack   34
2   John   31'''
content.append(Paragraph(output_excel.replace('\n', '<br />'), output_style))  # Replace newlines with HTML line breaks
content.append(Spacer(1, 12))

# Definition and Syntax for pd.read_excel
content.append(Paragraph("Definition: Reads an Excel file into a DataFrame.", normal_style))
content.append(Paragraph("Syntax: pd.read_excel(io, sheet_name=0, ...)", normal_style))
content.append(Spacer(1, 12))

# Section 5: Pickle Data
content.append(Paragraph("5. Reading Pickle Data", heading_style))
content.append(Spacer(1, 12))
pickle_code = '''df_excel.to_pickle('df_excel')
pd.read_pickle('df_excel')'''
content.append(Paragraph("Code:", normal_style))
content.append(Paragraph(pickle_code.replace('\n', '<br />'), code_style))  # Replace newlines with HTML line breaks
content.append(Spacer(1, 12))
content.append(Paragraph("Output:", normal_style))
output_pickle = '''      Name  Age
0   Krish   32
1    Jack   34
2   John   31'''
content.append(Paragraph(output_pickle.replace('\n', '<br />'), output_style))  # Replace newlines with HTML line breaks
content.append(Spacer(1, 12))

# Definition and Syntax for pd.to_pickle and pd.read_pickle
content.append(Paragraph("Definition: Saves a DataFrame to a pickle file and reads it back.", normal_style))
content.append(Paragraph("Syntax: df.to_pickle(path) and pd.read_pickle(path)", normal_style))
content.append(Spacer(1, 12))

# Build the PDF
document.build(content)

print(f"PDF report '{pdf_file}' has been generated successfully.")