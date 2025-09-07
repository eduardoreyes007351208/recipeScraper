from utils import get_data, write_data
import validators

def main():
    array = []
    url = input('Enter the url for the Preppy Kitchen recipe(enter "q" to quit): ')
    
    if validators.url(url):
        
        new_array, file_name = get_data(url, array)
        
        if len(new_array) < 4:
            print(f'I was not able to get the recipe from {url}')
            main()
        else:
            write_data(new_array, file_name)
            main()
        
    else:
        if (url.lower() == 'q'):
            print('\nGoodbye!\n')
        else:
            print('\nInvalid URL\n')
            main()
    

if __name__ == "__main__":
    main()
