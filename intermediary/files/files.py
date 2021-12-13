'''
    → Manipulate files

    → Always close the file

    → Docs python
        https://docs.python.org/3/library/functions.html#open
'''

# 💡 position cursor at beginning of file
def seek(file):
    file.seek(0, 0)

# 💡 create & open with Context manager
with open('text.txt', 'w+') as file:
    # 💡 write
    file.write('line 1\n')
    file.write('line 2\n')
    file.write('line 3')

    # 💡 read file
    seek(file)
    print(file.read())
    print('')

    # 💡 read lines
    seek(file)
    print(file.readline(), end='')
    print(file.readline(), end='')
    print(file.readline(), end='')
    print('')

    seek(file)
    for line in file.readlines():
        print(line, end='')

# 💡 json
import json
people = {
    1: {
        'name': 'Raul',
        'age': 22
    },
    2: {
        'name': 'Lau',
        'age': 32
    },
}

# convert dict to json
json.dumps(people, indent=True) 

# write/create file with json
with open('text.txt', 'w+') as file:
    file.write(json.dumps(people, indent=True))

# read file with json
with open('text.txt', 'r') as file:
    json.loads(file.read())

# 💡 delete files
import os

os.remove('text.txt')

'''
    Mode & Description
	
    r
        Opens a file for reading only. The file pointer is placed at the 
        beginning of the file. This is the default mode.

    rb
        Opens a file for reading only in binary format. The file pointer is 
        placed at the beginning of the file. This is the default mode.

    r+
        Opens a file for both reading and writing. The file pointer placed 
        at the beginning of the file.

    rb+
        Opens a file for both reading and writing in binary format. The 
        file pointer placed at the beginning of the file.

    w
        Opens a file for writing only. Overwrites the file if the file 
        exists. If the file does not exist, creates a new file for writing.

    wb
        Opens a file for writing only in binary format. Overwrites the 
        file if the file exists. If the file does not exist, creates a new 
        file for writing.

    w+
        Opens a file for both writing and reading. Overwrites the 
        existing file if the file exists. If the file does not exist, 
        creates a new file for reading and writing.

    wb+
        Opens a file for both writing and reading in binary format. 
        Overwrites the existing file if the file exists. If the file 
        does not exist, creates a new file for reading and writing.

    a
        Opens a file for appending. The file pointer is at the end 
        of the file if the file exists. That is, the file is in the 
        append mode. If the file does not exist, it creates a new 
        file for writing.

    ab
        Opens a file for appending in binary format. The file 
        pointer is at the end of the file if the file exists. 
        That is, the file is in the append mode. If the file 
        does not exist, it creates a new file for writing.

    a+
        Opens a file for both appending and reading. The file 
        pointer is at the end of the file if the file exists. 
        The file opens in the append mode. If the file does 
        not exist, it creates a new file for reading and writing.

    ab+
        Opens a file for both appending and reading in binary format. 
        The file pointer is at the end of the file if the file exists. 
        The file opens in the append mode. If the file does not exist, 
        it creates a new file for reading and writing.
'''

'''
    Attribute & Description

    file.closed
        Returns true if file is closed, false otherwise.

    file.mode
        Returns access mode with which file was opened.

    file.name
        Returns name of the file.
'''