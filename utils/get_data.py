import requests
from bs4 import BeautifulSoup

def get_data(url, arr):
    
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    title = soup.find('h2', class_='wprm-recipe-name').get_text()
    file_name = soup.find('h2', class_='wprm-recipe-name').get_text().lower().replace(' ', '_')
    equipment = soup.find('ul', class_='wprm-recipe-equipment')
    ingredients = soup.find_all('ul', class_='wprm-recipe-ingredients')
    instructions = soup.find_all('ul', class_='wprm-recipe-instructions')
    
    arr.append(title)
    arr.append('Equipment:')
    for child in equipment:
        arr.append(child.get_text())
    arr.append('Ingredients:')
    for child in ingredients:
        for c in child.children:
            arr.append(c.get_text())
    arr.append('Instructions')
    for child in instructions:
        for c in child.children:
            arr.append(c.get_text())
        
    return arr, file_name