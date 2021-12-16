'''
    → Context manager
'''

# 💡 Opening and closing file natively

'''
    When we are going to use a file we can forget to close it, 
    for this reason python has a context manager that performs 
    this task for us.
'''
with open('abc.txt', 'w') as file:
    file.write('Anything!')

# 💡 Create with Class
class File:
    def __init__(self, file, mode):
        print('Opening file!')
        self.file = open(file, mode)

    def __enter__(self):
        print('Returning file!')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Closing file!')
        self.file.close()

        # Exception handling

        return True

with File('abc.txt', 'w') as file:
    file.write('Anything!')

# 💡 Create with contextlib
from contextlib import contextmanager

@contextmanager
def openFile(file, mode):
    try:
        print('Opening file!')
        file = open(file, mode)

        # 💡 turn into a context manager
        yield file
    finally:
        print('Closing file!')
        file.close()

with openFile('abc.txt', 'w') as file:
    file.write('Anything!')