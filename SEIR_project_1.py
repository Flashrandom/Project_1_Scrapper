
import requests
import bs4

from bs4 import BeautifulSoup
# Source - https://stackoverflow.com/a/4033743

class Simple_Engine:
        def __init__(self,URL_link):
                self.url_link = url_link
                      
        def Scrap(self):
                # URL = "https://outlier.ai/"
                page = requests.get(self.url_link)
                soup = BeautifulSoup(page.content, "html.parser")
                
                results_body = soup.find('body')
                print(results_body.text,end="\n")
        
                results_a_tag = results_body.find_all('a')
        
                for tag in results_a_tag:       ##Source - https://automatetheboringstuff.com/3e/chapter13.html
                        link_URL = tag.get("href")
                        print(link_URL)



import sys       # Source - https://stackoverflow.com/a/70833
obj = Simple_Engine(sys.argv[1])
print(obj.Scrap())


