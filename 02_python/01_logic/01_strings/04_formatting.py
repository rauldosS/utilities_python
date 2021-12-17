'''

:s - Text (string)
:d - Integers (int)
:f - Floating point numbers (float)
:.(NUMBER)f - Number of decimal places (float)
:(CHARACTER)(> or < or ^)(QUANTITY)(TYPE - s, d or f)

> - Left
< - right
^ - Center

'''

number = 1

print(f'{number:0>10}')
# 0000000001

name = 'Raul'
name.ljust(10, '#') # Fill the rest with the character
name.lower()
name.upper()
name.title()