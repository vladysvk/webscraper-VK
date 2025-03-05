from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.ceneo.pl/")
print(html_text)