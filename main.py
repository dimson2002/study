import requests
from bs4 import BeautifulSoup

URL = 'https://magistratura.fa.ru/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
           'accept': '*/*'}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='d-content__block')
    stud = []
    for item in items:
        stud.append({
            'Факультет': item.find('div', class_='d-subject__title').get_text(strip=True),
            'Направление': item.find('div', class_='d-subject__group-txt').get_text(strip=True)
        })
    print(stud)
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()


