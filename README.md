# email-scanner-
Email Scraper

This script is used to scrape email addresses from a website. It can also save the results in a PDF report.

Requirements

Python 3.x
requests library
BeautifulSoup library
fpdf library
Usage

Run the script by executing python email_scraper.py in the command line.
Enter the URL of the website you want to scrape for email addresses.
The script will display a list of email addresses found on the website and will also save the results in a PDF report.
Features

Scrape email addresses from a website
Save results in a PDF report
Supports different file formats for storing the report (e.g. CSV, JSON, etc.)
An option to choose the level of depth of the scan (e.g. scan only the starting page, scan one level of links, scan all linked pages, etc.).
Limitations

The script only scrapes email addresses that are present in the HTML source code of the website and not in the JavaScript or any other dynamic content.
The script also doesn't support scanning of multiple pages of a website.
The script doesn't support XSS and SQL injection scans.
Please keep in mind that this script should be used for ethical and legal purposes only. Scraping websites without their permission is illegal in some jurisdictions and may violate their terms of service.

## Note
- Use this script responsibly, and only on websites that you have permission to scan.
- It is important to install the required libraries before running the script, by running `pip install -r requirements.txt`

