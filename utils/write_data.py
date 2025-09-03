from pathlib import Path

def write_data(arr, file_name):
    file_path = Path(f'./txt_files/{file_name}.txt')
    
    if file_path.exists():
        print(f'\nTxt file of the {file_name} recipe already exist.\n')
    else:
        print(f'\nGenerating txt for {file_name} recipe...\n')
        for val in arr:
            with open(f'./txt_files/{file_name}.txt', 'a') as f:
                f.write(f'{val}\n')
                