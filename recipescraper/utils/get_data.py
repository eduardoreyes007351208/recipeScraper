# import libraries for this module
import requests
from bs4 import BeautifulSoup
import json

# define the funtion/module and define the parameters "url" and "arr"
def get_data(url, arr):
    
    # define variables: 
    # page which requests the content from a website url
    # soup which uses BeautifulSoup to parse through html content
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # look for script tag in the data that has a type='application/ld+json',
    # which gets the metadata containing recipe content and load it as json
    complete_data = soup.find('script', type='application/ld+json').get_text().strip()
    group_array = json.loads(complete_data)
    # define variables to contain title, ingredients, and instructions
    title = ''
    ingredient_list = ''
    instruction_list = ''
    
    # checks to see if the data from the website is in a dictionary or list
    if isinstance(group_array, dict):
        
        # check to see if the dictionary has a type of @graph
        graph_list = group_array.get('@graph', [])
        if graph_list:
            
            # iterate through the data and check for type == 'Recipe'
            for items in graph_list:
                types = items.get('@type')
                if types == 'Recipe':
                    
                    # if type is 'Recipe', get the title, ingredients, and instructions
                    # and save to variables from earlier
                    recipe = items
                    title = recipe.get('name')
                    ingredient_list = recipe.get('recipeIngredient')
                    instruction_list = recipe.get('recipeInstructions')
        else:
            
            # if there is no graph, then just find the type of 'Recipe'
            # and save the title, ingredients, and instructions, no need to
            # iterate a graph since there is none
            types = group_array.get('@type')
            if types == 'Recipe':
                recipe = group_array
                title = recipe.get('name')
                ingredient_list = recipe.get('recipeIngredient')
                instruction_list = recipe.get('recipeInstructions')
    else:
        
        # the data is a list and get the title, ingredients, and instructions
        data = group_array[0]
        title = data.get('name')
        ingredient_list = data.get('recipeIngredient')
        instruction_list = data.get('recipeInstructions')
        
    # to get the file name for txt file, just get the recipe title and
    # lowercase all letters, and replace whitespaces with underscore
    file_name = title.lower().replace(' ', '_')
    
    # append the recipe title to array parameter
    arr.append(title)
    
    # iterate through the ingredients list and append
    # each ingredient to the array
    arr.append('\nIngredients:')
    for i, item in enumerate(ingredient_list, start=1):
        arr.append(f'{i}. {item}')
        
    # iterate through the instructions list and append
    # each instruction to the array
    arr.append('\nInstructions:')
    for section in instruction_list:
        sec_name = section.get('name')
        arr.append(f'{sec_name}')
        
        
        steps = section.get('itemListElement', [])
        for i, step in enumerate(steps, start=1):
            arr.append(f'{i}. {step.get('text')}')
            
    # return the appended array and the lowercase file name            
    return arr, file_name