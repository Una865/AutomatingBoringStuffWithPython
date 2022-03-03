import pyperclip
import webbrowser
import argparse

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

link = pyperclip.paste()
req = Request(link)
html_page = urlopen(req)

soup = BeautifulSoup(html_page,'lxml')
links = []

for link in soup.findAll('a'):   # 'a' is the indicator for links in html
    links.append(link.get('href'))

for el in links:
    webbrowser.open(el)
     
