import webbrowser
import requests
import bs4

print("Opening browser...")
# webbrowser.open('https://inventwithpython.com/')
print("Done")


# res = requests.get('https://outlier.ai/')
# print(type(res))
# print(res.status_code == requests.codes.ok)
# print(len(res.text))

# print(res.text[:])


# # >>>>>>   parsing HTMLL from bs4

# # import bs4
# res = requests.get('https://outlier.ai/')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(noStarchSoup))
# if noStarchSoup.title:
#     print(noStarchSoup.title.text)
# else:
#     print("no title for this website")

# .......


import requests
from bs4 import BeautifulSoup

URL = " https://pypi.org/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results_body = soup.find('body')
# for result in results_body :
print(results_body.prettify())

results_a_tag = results_body.find_all('a')
# print(results_a_tag)

for tag in results_a_tag:
        link_URL = tag.get("href")
        print(link_URL)
