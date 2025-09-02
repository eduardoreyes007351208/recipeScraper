import requests
from bs4 import BeautifulSoup

def get_data(url):
    
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find('h2', class_='wprm-recipe-name').get_text()
    equipment = soup.find('div', class_='wprm-recipe-equipment-container').get_text(separator='\n', strip=True)
    ingredients = soup.find('div', class_='wprm-recipe-ingredients-container').get_text(separator='\n', strip=True)
    print(title, equipment, ingredients)
    
    
    