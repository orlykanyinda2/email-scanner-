import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

# Get the website URL from user input
url = input("Enter a website URL: ")
if not url.startswith("http"):
    url = "http://" + url

# Make a GET request to the website
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize list to store email addresses
emails = []

# Search for all anchor tags
for link in soup.find_all('a'):
    # Get the href attribute
    href = link.get('href')
    if href:
        # Check if the href is an email address
        if 'mailto:' in href:
            email = href.replace('mailto:', '')
            emails.append(email)

# Create a report
report = "Email addresses found on {}:\n\n{}".format(url, "\n".join(emails))

# Print the report
print(report)

# Create a PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=report, ln=1, align="C")
pdf.output("emails_on_" + url + ".pdf")

print("Report saved as pdf")
