# import libraries and modules for main.pu
from .utils import get_data, write_data
import validators
import argparse

from fastapi import FastAPI, HTTPException, Response

api = FastAPI()

# GET pdf 
@api.get('/get_pdf')
def get_pdf(url: str):
    # define array to contain data from get_data
    array = []
    
    # check to see the url argument from user is a valid url
    if validators.url(url):
        
        new_array, file_name, title = get_data(url, array)
        if len(new_array) < 4:
            raise HTTPException(status_code=404, detail='Recipe not found')
            
        else:
            pdf_bytes = bytes(write_data(new_array, title))
            return Response(
                content=pdf_bytes,
                media_type='application/pdf',
                headers={'Content-Disposition': f'attachment; filename={file_name}.pdf'}
            )

# define the main functions
def main():
    # define array to contain data from get_data
    array = []
    # parser that parses arguments received from the user when called as a package, url
    parser = argparse.ArgumentParser(description='Scrape cooking recipe from a website and write to a txt file.')
    parser.add_argument('url', help='URL for the recipe page.')
    url = parser.parse_args()
    print(f'Scraping the recipe from {url.url}')
    
    # check to see the url argument from user is a valid url
    if validators.url(url.url):
        
        new_array, file_name = get_data(url.url, array)
        
        if len(new_array) < 4:
            print(f'I was not able to get the recipe from {url.url}')
            
        else:
            write_data(new_array, file_name)
            
      
    else:
        # check to see if the invalid url is a 'q' to quit or other 
        # invalid url that lets user know input was invalid
        if (url.lower() == 'q'):
            print('\nGoodbye!\n')
        else:
            print('\nInvalid URL\n')
            
    

if __name__ == "__main__":
    main()
