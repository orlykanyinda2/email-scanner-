Email Scraper

This script is a simple web scraper that extracts email addresses from a given website. The script takes in a website URL as input and makes a GET request to the website to retrieve its HTML. The HTML is then parsed using the BeautifulSoup library, and the script searches for all anchor tags. If an anchor tag contains an href attribute that starts with "mailto:", the script extracts the email address and adds it to a list of email addresses.

Requirements

Python 3.x
requests library
BeautifulSoup library
fpdf library
Usage

Clone the repository
Open a terminal and navigate to the directory containing the script
Run the command python email_scraper.py
Enter the website URL when prompted
The script will display the list of email addresses found on the website and also save a PDF report of the email addresses found on the website
Additional Features

The script also allows you to save the report in different formats like CSV, JSON
The script also allows you to choose the level of depth of the scan.
Note

The script is designed to only extract email addresses from the website and does not perform any XSS or SQL injection scans.
Support

If you have any issues or questions about this script, please open an issue on the repository or contact me via email.