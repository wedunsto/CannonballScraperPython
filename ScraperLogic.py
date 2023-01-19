"""
Objectives:
    Access website HTML
    Parse HTML for desired elements
"""

import requests
from bs4 import BeautifulSoup

class Parser:
    def __init__(self):
        self.results = dict() # Store the URL and names with key-pair values
        # URL to be parsed
        self.url = "https://www.smokingpipes.com/pipes/new/moonshine/?sortOpt=dateDesc&page=1"
        self.prefix = "https://www.smokingpipes.com" # Prefix for href URLs
        self.front_page = requests.get(self.url) # Fetch the HTML
        self.soup = BeautifulSoup(self.front_page.content, "html.parser")
        self.pipes = self.soup.find_all("div", {"class": "product"}) # Parse for divs with product class

    def parse(self): # Populate results dictionary
        for pipe in self.pipes:
            path = pipe.find_all('a', href=True)[1] # Store local path to pipe URLs
            identifier = path.find("img")['alt'] # Store pipe's name
            if 'Cannonball' in identifier:
                # Store absolute path to pipe URL and pipe name
                self.results[self.prefix+path['href']] = identifier