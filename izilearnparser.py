import pickle
import requests
from bs4 import BeautifulSoup
from lxml import html


# должен парсить, но оно этого не делает

SEARCH_URL = "https://izilearn.ru/index.php?r=acmp%2Findex&AcmpSearch%5Bname%5D=&AcmpSearch%5Bnumber%5D="
missing = pickle.load(open("missing_solutions", "rb"))

print(missing)

response = requests.get(SEARCH_URL+"135")
tree = html.fromstring(response.content)

print(tree.xpath("/html/body/div[1]/div/div[2]/div/div[4]/table/tbody/tr/td[1]/a"))