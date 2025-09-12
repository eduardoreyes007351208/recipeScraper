# import libraries needed for module
from pathlib import Path

# define function/module and define parameters 'arr' and 'file_name'
def write_data(arr, file_name):
    
    # get the current directory the user is at when calling the program
    # and checks to see if there currently exists a file with the same
    # file_name
    current_dir = Path.cwd()
    file_path = Path(f'{current_dir}/{file_name}.txt')
         
    # if the path to file exists, alert user that there already is
    # a txt file for that recipe
    if file_path.exists():
        print(f'\nTxt file of the {file_name} recipe already exist.\n')
     
    else:
        # if the path doesn't exists, create a new txt file with the
        # file_name and write the data from the array appended with the
        # recipe data
        for val in arr:
            with open(f'{file_name}.txt', 'a') as f:
                f.write(f'{val}\n')
                    