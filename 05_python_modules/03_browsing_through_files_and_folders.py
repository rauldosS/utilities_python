import os

path_windows = r'C:programs/whatever'
path = input('Enter a path: ') # '/dev/python/utilities_python/05_python_modules/'
search = input('Enter a search: ') # '09'

counter = 0

def formatSize(size):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo:
        size = size
        text = 'B'
    elif size < mega:
        size /=kilo
        text = 'K'
    elif size < giga:
        size /= mega
        text = 'M'
    elif size < tera:
        size /= giga
        text = 'G'
    elif size < peta:
        size /= tera
        text = 'T'
    else:
        size /= peta
        text = 'P'
    
    size = round(size, 2)

    return f'{size}{text}'.replace('.', ',')

for root, directories, files in os.walk(path):
    for file in files:
        if search in file:
            try:
                full_path = os.path.join(root, file)
                name, extension = os.path.splitext(file)
                size = os.path.getsize(full_path)

                print('\nFile found:', file)
                print('Path:', full_path)
                print('Name:', name)
                print('Extension:', extension)
                print('Size:', formatSize(size))
            except PermissionError as e:
                print('No permissions')
            except FileNotFoundError as e:
                print('File not found')
            except Exception as e:
                print('Unknown error:', e)

            counter += 1

print(f'{counter} file(s) found')