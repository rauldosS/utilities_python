'''
    → count
'''

import os
import shutil

original_path = '/dev/python/utilities_python/05_python_modules/media'
new_path = '/dev/python/utilities_python/05_python_modules/media1'

# create folder
try:
    os.mkdir(new_path)
except FileExistsError as e:
    print(f'Folder {new_path} already exists!')

for root, dirs, files in os.walk(original_path):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_path, file)

        # Moving files
        shutil.move(old_file_path, new_file_path)
        print(f'File {file} successfully moved!')

        # Copy files txt
        if '.txt' in file:
            shutil.move(old_file_path, new_file_path)
            print(f'File {file} successfully copied!')

# Delete
for root, dirs, files in os.walk(new_path):
    for file in files:
        new_file_path = os.path.join(new_path, file)

        if '.txt' in file:
            os.remove(new_file_path)
            print(f'File {file} successfully deleted!')