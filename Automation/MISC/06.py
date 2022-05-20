from clearConsole import clearConsole
from bs4 import BeautifulSoup
import requests
url = "http://quotes.toscrape.com/"
clearConsole()

response  = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)

print("done")