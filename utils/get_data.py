import requests
from bs4 import BeautifulSoup
import json

def get_data(url, arr):
    
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #title = soup.find('h2', class_='wprm-recipe-name').get_text()
    #file_name = soup.find('h2', class_='wprm-recipe-name').get_text().lower().replace(' ', '_')
    #equipment = soup.find('ul', class_='wprm-recipe-equipment')
    #ingredients = soup.find_all('ul', class_='wprm-recipe-ingredients')
    #nstructions = soup.find_all('ul', class_='wprm-recipe-instructions')
    complete_data = soup.find('script', type='application/ld+json').get_text()
    group_array = json.loads(complete_data)
    title = ''
    equipment_list = ''
    ingredient_list = ''
    instruction_list = ''
    
    if isinstance(group_array, dict):
        graph_list = group_array.get('@graph', [])
        if graph_list:
            for items in graph_list:
                types = items.get('@type')
                if types == 'Recipe':
                    recipe = items
                    title = recipe.get('name')
                    ingredient_list = recipe.get('recipeIngredient')
                    instruction_list = recipe.get('recipeInstructions')
        else:
            types = group_array.get('@type')
            if types == 'Recipe':
                recipe = group_array
                title = recipe.get('name')
                ingredient_list = recipe.get('recipeIngredient')
                instruction_list = recipe.get('recipeInstructions')
    else:
        print(False)
        data = group_array[0]
        title = data.get('name')
        ingredient_list = data.get('recipeIngredient')
        instruction_list = data.get('recipeInstructions')
        
    print(f"{title}\n, {ingredient_list}\n, {instruction_list}")
                    
    
   # arr.append(title)
   # arr.append('Equipment:')
   # for child in equipment:
   #     arr.append(child.get_text())
   # arr.append('Ingredients:')
   # for child in ingredients:
   #     for c in child.children:
   #         arr.append(c.get_text())
   # arr.append('Instructions')
   # for child in instructions:
   #     for c in child.children:
   #         arr.append(f'• {c.get_text()}')
    file_name = ''     
    return arr, file_name

# try and add just @type == 'Recipe' if website has no @graph - ER 9/3/2025
def practice():
    user_input = input('Enter the url for the Preppy Kitchen recipe(enter "q" to quit): ')
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0'}
    page = requests.get(user_input, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    fullInfo = soup.find('script', type='application/ld+json').get_text()
    group_array = json.loads(fullInfo)
    #graph_list = group_array.get('@graph', [])
    if isinstance(group_array, dict):
        graph_list = group_array.get('@graph', [])
        if graph_list:
            for items in graph_list:
                types = items.get('@type')
                if types == 'Recipe':
                    recipe = items
                    print(recipe.get('recipeIngredient'))
        else:
            types = group_array.get('@type')
            if types == 'Recipe':
                recipe = group_array
                print(recipe.get('recipeIngredient'))
    else:
        print(False)
        data = group_array[0]
        print(data.get('recipeIngredient'))
        
        
    #graph_list = group_array.get('@graph', [])
    
    practice()
if __name__ == '__main__':
    practice()
