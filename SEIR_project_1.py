
import requests
import bs4

from bs4 import BeautifulSoup
# Source - https://stackoverflow.com/a/4033743

class Crawler_Engine:
        def __init__(self,URL_link):
                self.URL_link = URL_link
                      
        def crawler(self):
                # URL = "https://outlier.ai/"
                page = requests.get(self.URL_link)
                soup = BeautifulSoup(page.content, "html.parser")
                
                results_body = soup.find('body')
                print(results_body.text,end="\n")

                results_a_tag = results_body.find_all('a')

                for tag in results_a_tag:
                        link_URL = tag.get("href")
                        print(link_URL)

# Source - https://stackoverflow.com/a/70833

import sys
obj = Crawler_Engine(sys.argv[1])
print(obj.crawler())
