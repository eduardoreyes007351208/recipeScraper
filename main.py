from utils import get_data

def main():
    array = []
    url = input('Enter the url for the Preppy Kitchen recipe: ')
    new_array = get_data(url, array)
    
    print(new_array)


if __name__ == "__main__":
    main()
