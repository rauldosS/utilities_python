'''
    → Modules are .py file and serve to expand the standard functionality 
    of the language

    → All modules
        https://docs.python.org/3/py-modindex.html
'''

# declare import
from sys import platform as so
from random import randint

for i in range(10):
    print(randint(0, 10))


'''
    💡 install modules (pip)

    import pymyssql

    comands in terminal:
        → pip install pymyssql
        → pip uninstall pymyssql
'''

'''
    → Create own modules
'''

# import calculations (file calculations.py)
import calculations 
from calculations import PI

print(calculations.PI)
print(PI)

'''
    → Create own packages
'''

# import package sales
from sales.calculate_price import increase, reduction

price = 49.99
price_increase = increase(value=price, percentage=15)
price_reduction = reduction(value=price, percentage=15)

print(price_increase, price_reduction)
# 
# 
# 
# 