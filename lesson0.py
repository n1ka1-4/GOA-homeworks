import os

folder_path = '.'

for folder in os.listdir(folder_path):
    if folder.startswith('day'):
        number_part = folder[3:]
        if number_part.isdigit():
            new_name = f"day{int(number_part):03d}"
            if folder != new_name:
                print(f"Renaming {folder} to {new_name}")
                os.rename(os.path.join(folder_path, folder), os.path.join(folder_path, new_name))
