from utils import get_data
import validators

def main():
    array = []
    url = input('Enter the url for the Preppy Kitchen recipe(enter "q" to quit): ')
    
    if validators.url(url):
        print('valid URL')
        new_array, file_name = get_data(url, array)
        print(new_array)
        
    else:
        if (url.lower() == 'q'):
            print('Goodbye!')
        else:
            print('Invalid URL')
            main()
    

if __name__ == "__main__":
    main()
