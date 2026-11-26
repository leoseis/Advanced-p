"""
ADVANCED PYTHON TEACHING GUIDE: WEB SCRAPING WITH BEAUTIFUL SOUP
Simplified notes, practical examples, classroom task, and objective test.

INSTALL IN THE VS CODE TERMINAL:
    python -m pip install requests beautifulsoup4

Use scraping responsibly. Respect website terms, robots.txt guidance, rate
limits, privacy, and applicable laws. Do not bypass login or access controls.
"""

# 1. WHAT IS WEB SCRAPING?
"""
Web scraping means using code to collect information from a webpage.
Example: a page lists books and prices. A Python program can extract the
book titles and prices instead of requiring a person to copy them manually.
"""

# 2. REQUESTS VS BEAUTIFUL SOUP
"""
Requests downloads a webpage's HTML.
Beautiful Soup parses that HTML so Python can search for headings, paragraphs,
links, prices, and other elements.

Simple workflow:
Python -> Requests downloads HTML -> Beautiful Soup parses HTML -> extract data
"""

# 3. UNDERSTAND HTML
"""
Example:
    <h1>Book Store</h1>
    <p class="price">5000 naira</p>
    <a href="https://example.com/books">View books</a>

h1 is a heading, p is a paragraph, class identifies a group of elements,
a is a link, and href is the link destination.
"""

# 4. INSTALLATION
"""
Run this in the VS Code terminal, not inside Python:
    python -m pip install requests beautifulsoup4
"""

# 5. FIRST EXAMPLE: PARSE HTML WITHOUT THE INTERNET
from bs4 import BeautifulSoup

html_example = """
<html>
    <head><title>Book Store</title></head>
    <body>
        <h1>Welcome to My Book Store</h1>
        <p class="description">Books for learners.</p>
        <p class="price">Price: 5000 naira</p>
        <a href="https://example.com/books">View books</a>
    </body>
</html>
"""

soup = BeautifulSoup(html_example, "html.parser")

print("Title:", soup.title.get_text(strip=True))
print("Heading:", soup.find("h1").get_text(strip=True))
print("Description:", soup.find("p", class_="description").get_text(strip=True))
print("Price:", soup.find("p", class_="price").get_text(strip=True))

"""
Explanation:
- BeautifulSoup(html_example, "html.parser") parses the HTML.
- find("h1") finds the first h1 element.
- class_="description" searches by class. Python uses class_ because class
  is a reserved Python keyword.
- get_text(strip=True) extracts text and trims surrounding whitespace.
"""

# 6. find() AND find_all()
html_books = """
<html><body>
    <p class="book">Python Basics</p>
    <p class="book">Learning Django</p>
    <p class="book">Web Development</p>
</body></html>
"""

soup = BeautifulSoup(html_books, "html.parser")
first_book = soup.find("p", class_="book")
all_books = soup.find_all("p", class_="book")

print("First book:", first_book.get_text(strip=True))
print("All books:")
for book in all_books:
    print(book.get_text(strip=True))

"""
find() returns the first matching element.
find_all() returns all matching elements as a list.
"""

# 7. FIND BY ID
id_html = '<h1 id="page-title">Latest Articles</h1>'
soup = BeautifulSoup(id_html, "html.parser")
heading = soup.find(id="page-title")

if heading:
    print("Heading:", heading.get_text(strip=True))
else:
    print("Heading not found.")

# 8. EXTRACT LINKS
link_html = """
<a href="https://example.com/python">Python</a>
<a href="https://example.com/django">Django</a>
<a href="/contact">Contact</a>
"""
soup = BeautifulSoup(link_html, "html.parser")

for link in soup.find_all("a"):
    print(link.get_text(strip=True), "->", link.get("href"))

"""
a is the link tag. href contains the destination. A URL beginning with /
is relative; urllib.parse.urljoin() can combine it with the site's base URL.
"""

# 9. DOWNLOAD A WEBPAGE WITH REQUESTS
import requests

url = "https://books.toscrape.com/"

try:
    response = requests.get(
        url,
        timeout=15,
        headers={"User-Agent": "EducationalPythonScraper/1.0"},
    )
    response.raise_for_status()
    print("Status code:", response.status_code)
    print("HTML length:", len(response.text), "characters")
except requests.exceptions.RequestException as error:
    print("Could not download webpage:", error)

"""
requests.get(url) sends an HTTP GET request.
timeout=15 prevents waiting forever.
status_code shows the HTTP status; 200 commonly means success.
raise_for_status() raises an error for an unsuccessful HTTP response.
response.text contains the HTML as text.
"""

# 10. PARSE THE DOWNLOADED PAGE
try:
    response = requests.get("https://books.toscrape.com/", timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.title:
        print("Page title:", soup.title.get_text(strip=True))
    else:
        print("No page title found.")
except requests.exceptions.RequestException as error:
    print("Request failed:", error)

# 11. PRACTICAL SCRAPER: BOOK TITLES AND PRICES
"""
Books to Scrape is a practice website. This example reads the first page only.
Website HTML can change, so selectors may need to be updated in future.
"""
try:
    response = requests.get("https://books.toscrape.com/", timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    print("Books found:", len(books))
    for book in books:
        heading_tag = book.find("h3")
        title_link = heading_tag.find("a") if heading_tag else None
        price_tag = book.find("p", class_="price_color")

        title = title_link.get("title", "Title not found") if title_link else "Title not found"
        price = price_tag.get_text(strip=True) if price_tag else "Price not found"

        print("Title:", title)
        print("Price:", price)
        print("-" * 30)
except requests.exceptions.RequestException as error:
    print("Request failed:", error)

# 12. CSS SELECTORS
"""
select() finds all elements matching a CSS selector.
select_one() finds the first matching element.
Examples:
    soup.select("h1")                 all h1 headings
    soup.select_one("#page-title")    element with id page-title
    soup.select(".book")              all elements with class book
"""
selector_html = """
<h1 id="page-title">Books</h1>
<p class="book">Python Basics</p>
<p class="book">Django Basics</p>
"""
soup = BeautifulSoup(selector_html, "html.parser")
print("By ID:", soup.select_one("#page-title").get_text(strip=True))
for item in soup.select(".book"):
    print("Book:", item.get_text(strip=True))

# 13. SAVE DATA TO CSV
import csv

book_records = [
    {"title": "Python Basics", "price": "5000"},
    {"title": "Learning Django", "price": "6500"},
]

with open("books.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["title", "price"])
    writer.writeheader()
    writer.writerows(book_records)

print("Saved records to books.csv")

"""
DictWriter writes dictionaries into a CSV file.
writeheader() writes the column names; writerows() writes the records.
"""

# 14. BASIC ERROR HANDLING
def download_page(page_url):
    try:
        page_response = requests.get(page_url, timeout=15)
        page_response.raise_for_status()
        return BeautifulSoup(page_response.text, "html.parser")
    except requests.exceptions.RequestException as error:
        print("Unable to download page:", error)
        return None

"""
Check that find() returned an element before calling get_text().
If the page's HTML changes, your selector may no longer match.
"""

# 15. IMPORTANT LIMITATIONS AND RESPONSIBLE SCRAPING
"""
Beautiful Soup parses HTML; it does not download the page by itself.
Requests may not see content inserted by JavaScript after the page loads.
A browser automation tool such as Selenium may be needed for permitted tasks.
Respect website terms, robots.txt guidance, rate limits, and privacy.
Do not scrape private or access-controlled information or bypass restrictions.
"""

# 16. PRACTICAL CLASSROOM EXERCISE
"""
PROJECT: BOOK INFORMATION COLLECTOR

Students should:
1. Download https://books.toscrape.com/ with Requests.
2. Check the response status.
3. Parse the HTML with Beautiful Soup.
4. Find article elements with class product_pod.
5. Extract each book's title and price.
6. Print the results neatly.
7. Save the results to books_scraped.csv.
8. Handle request errors and missing elements.

Extension: extract each book's relative link and use
urllib.parse.urljoin() to build its full URL.
"""

# 17. COMMON ERRORS
"""
ModuleNotFoundError: No module named 'bs4'
    python -m pip install beautifulsoup4

ModuleNotFoundError: No module named 'requests'
    python -m pip install requests

find() returns None:
    Check the tag, class, ID, spelling, and actual HTML before extracting text.

Request timeout:
    Check the internet connection and try later. Keep a timeout in requests.

No results:
    Inspect the current HTML and confirm your selectors still match.
"""

# 18. LESSON SUMMARY
"""
- Web scraping collects webpage information using code.
- Requests downloads HTML.
- Beautiful Soup parses HTML.
- find() finds the first match; find_all() finds all matches.
- get_text(strip=True) extracts readable text.
- get("href") extracts a link destination.
- select() and select_one() use CSS selectors.
- csv can save extracted data.
- Always handle errors and scrape responsibly.
"""

# 19. OBJECTIVE TEST: 15 QUESTIONS
"""
Choose ONE answer (A, B, C, or D). Each question is 1 mark.

1. What is web scraping?
A. Styling a website
B. Using code to collect webpage information
C. Turning off the internet
D. Creating a virtual environment

2. Which library commonly downloads webpage content?
A. Requests
B. Turtle
C. Tkinter
D. Random

3. What is Beautiful Soup mainly used for?
A. Parsing and searching HTML
B. Creating passwords
C. Editing images
D. Starting a server

4. Which command installs Requests and Beautiful Soup?
A. python -m pip install requests beautifulsoup4
B. python install web
C. pip start scraping
D. python -m install html

5. What does HTML describe?
A. The structure of webpage content
B. Only Python variables
C. Battery level
D. A database password

6. What does requests.get(url) normally do?
A. Sends an HTTP GET request
B. Deletes a website
C. Creates a class
D. Installs Beautiful Soup

7. What does response.status_code show?
A. HTTP response status
B. Number of Python files
C. Computer password
D. Number of variables

8. What does BeautifulSoup(html, "html.parser") do?
A. Parses HTML so it can be searched
B. Downloads Python
C. Saves Excel
D. Opens a terminal

9. Which method returns the first matching element?
A. find()
B. find_all()
C. write()
D. sendall()

10. Which method returns all matching elements?
A. connect()
B. find_all()
C. input()
D. close()

11. What does get_text(strip=True) do?
A. Extracts text and trims surrounding whitespace
B. Deletes the webpage
C. Downloads a picture
D. Changes HTML into CSS

12. Which HTML attribute usually contains a link destination?
A. href
B. class
C. color
D. font

13. Why do we use class_="book" in Beautiful Soup?
A. class is a reserved Python keyword
B. It speeds up the website
C. It installs Requests
D. It creates a CSV file

14. Why might Requests not find content visible in a browser?
A. The content may be added by JavaScript after loading
B. Python cannot store text
C. HTML has no elements
D. CSV files cannot contain words

15. Which is responsible scraping?
A. Send as many requests as possible
B. Bypass login restrictions
C. Respect website rules and avoid excessive requests
D. Collect private information without permission
"""

# 20. TEACHER'S ANSWER KEY
"""
Hide this section before giving the test to students.

1. B
2. A
3. A
4. A
5. A
6. A
7. A
8. A
9. A
10. B
11. A
12. A
13. A
14. A
15. C
"""

if __name__ == "__main__":
    print("\nWEB SCRAPING WITH BEAUTIFUL SOUP TEACHING GUIDE")
    print("Install dependencies: python -m pip install requests beautifulsoup4")
