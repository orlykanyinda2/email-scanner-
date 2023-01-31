import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

# Get the base URL from user input
base_url = input("Enter a website URL: ")
if not base_url.startswith("http"):
    base_url = "http://" + base_url

# Get the number of pages to scan from user input
num_pages = int(input("Enter the number of pages to scan: "))

# Initialize list to store email addresses
emails = []

# Loop through each page
for i in range(1, num_pages + 1):
    # Construct the full URL
    url = base_url + "/page" + str(i)

    # Make a GET request to the website
    response = requests.get(url)

    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

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
report = "Email addresses found on {}:\n\n{}".format(base_url, "\n".join(emails))

# Print the report
print(report)

# Create a PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=report, ln=1, align="C")
pdf.output("emails_on_" + base_url + ".pdf")

print("Report saved as pdf")
