# Crawler_Engine
This is a project on a web crawler which crawls title, web links attached in a given page. 

A simple Python program that fetches a webpage and prints:

- Page Title (without HTML tags)
- Page Body Text
- All URLs present on the page
## References:
### for learning command line
- https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments/4033743#4033743
### For Revising beutifulsoup4
- https://www.geeksforgeeks.org/python/implementing-web-scraping-python-beautiful-soup/
### for fetching the links 
- https://automatetheboringstuff.com/3e/chapter13.html
## Requirements

- Python 3
- requests
- beautifulsoup4

Install dependencies:

pip install requests beautifulsoup4

## Usage

Run the program from command line:

python main.py <URL>

Example:

python main.py https://example.com

## Output

- Page title
- Page text content
- List of all links found on the page
