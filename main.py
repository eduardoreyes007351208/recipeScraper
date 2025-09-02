from utils import get_data

def main():
    array = []
    print("Hello from recipescraper!")
    new_array = get_data('https://preppykitchen.com/chicken-tetrazzini/#recipe', array)
    print(new_array)


if __name__ == "__main__":
    main()
