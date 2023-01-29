README
Introduction
This code is a website scanner that searches for email addresses on a given website. It allows the user to specify the level of scanning (1-3) and generates a report of all the email addresses found. The report is both printed to the console and saved as a PDF file.

Dependencies
This code requires the following python packages to be installed:

requests
bs4 (BeautifulSoup)
fpdf
Usage
Enter a website URL: The code prompts the user to enter a website URL. The URL must start with either "http" or "https". If the user does not specify "http" or "https", the code will add "http://" to the beginning of the URL.

Enter the level of scan (1-3): The user is prompted to enter the level of scan (1-3). If the user enters an invalid value, the code defaults to level 1.

Output
The code generates a report of all the email addresses found on the website. The report is printed to the console and saved as a PDF file with the name "emails_on_[URL].pdf".

Implementation of Scan Levels
The code implements the chosen scan level as follows:

Level 1: Only the starting page is scanned.
Level 2: One level of links is scanned.
Level 3: All linked pages are scanned.
Conclusion
This code provides a quick and easy way to search for email addresses on a website. By allowing the user to specify the level of scanning, the code can be customized to fit the specific needs of the user. The generated report makes it easy to see all the email addresses found on the website, and the saved PDF file provides a permanent record of the results.
