from utils import get_data, write_data
import validators

def main():
    array = []
    url = input('Enter the url for the Preppy Kitchen recipe(enter "q" to quit): ')
    
    if validators.url(url):
        
        new_array, file_name = get_data(url, array)
        write_data(new_array, file_name)
        main()
        
    else:
        if (url.lower() == 'q'):
            print('\nGoodbye!\n')
        else:
            print('Invalid URL')
            main()
    

if __name__ == "__main__":
    main()
