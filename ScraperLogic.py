"""
Objectives:
    Access website HTML
    Parse HTML for desired elements
"""

import requests

url = "https://www.smokingpipes.com/pipes/new/moonshine/?sortOpt=dateDesc&page=1"
front_page = requests.get(url)
print(front_page.text)