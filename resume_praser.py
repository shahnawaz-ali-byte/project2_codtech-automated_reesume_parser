import re

resume_text = """
Name: anurag bhagat
Email: anuragbhagat@email.com
Phone: +91-000000000
Education: B.Tech in Computer Science
Skills: Python, Java, HTML, Machine Learning
Experience: 2 years at TCS
"""

# regular expressions
name = re.findall(r"Name:\s*(.*)", resume_text)[0]
email = re.findall(r"Email:\s*(.*)", resume_text)[0]
phone = re.findall(r"Phone:\s*(.*)", resume_text)[0]
education = re.findall(r"Education:\s*(.*)", resume_text)[0]
skills = re.findall(r"Skills:\s*(.*)", resume_text)[0]

# Output
print("Extracted Resume Info:")
print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Education:", education)
print("Skills:", skills)