'''
    → Creating exceptions
'''

class itsWrong(Exception):
    pass

def test():
    raise itsWrong('Error!')

try:
    test()
except itsWrong as error:
    print(f'Erro: { error }')