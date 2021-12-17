'''
    Considering two lists of integers or floats (list A and list B)
    Add the values in the lists returning a new list with the summed values:

    If one list is larger than the other, the sum will only consider the size 
    of the smallest one.

    Example:
    list_a = [1, 2, 3, 4, 5, 6, 7]
    list_b = [1, 2, 3, 4]
    
    ================== result
    sum_list = [2, 4, 6, 8]
'''

from itertools import count

numbers_a = [1, 2, 3, 4, 5, 6, 7]
numbers_b = [1, 2, 3, 4]

numbers = zip(
    numbers_a,
    numbers_b
)

sum_numbers = [number_a + number_b for number_a, number_b in numbers]

print(sum_numbers)