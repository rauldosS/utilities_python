'''
    → Try, Except

    → Exception handling

    → Built-in Exceptions:
        https://docs.python.org/3/library/exceptions.html
'''

# declare (any error)
try:
    print(a)
except:
    print('Error')

# NameError, Exception
try:
    print(a)
except NameError as error:
    print('Error:', error)
except Exception as error:
    print('Unexpected Error:', error)

# Multiple errors
try:
    a = []
    a[1]
except (IndexError, KeyError) as error:
    print('Index or Key error:', error)
    
# else - In case where there is no error will be executed
# finally - Will always run
try:
    print('Success!')
except:
    print('Error')
else:
    print('Success!')
finally:
    print('Success!')

'''
    → Throwing your next exceptions
'''

# raise
def division(n1, n2):
    if n2 == 0:
        raise ValueError('n2 cannot be zero')
    return n1 / n2
    
# catch exception  
try:
    division(10, 0)
except ValueError as error:
    print(error)

'''
    → Using try and except as a conditional
'''

# 
def convert_number(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            # return default None
            pass

number = convert_number('5.5')

print(number)