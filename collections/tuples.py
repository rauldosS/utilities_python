'''
    → Tuples cannot be changed (immutable)
    → Are accessible through the index

    → When to use?
        Tuples can be used when your items are pre-defined and usually do not need 
        to be changed, some examples: months of the year, commemorative dates, days 
        of the week, seasons, city names, etc. Its use is also recommended when 
        working with heterogeneous data, that is, with elements of different types.
'''

# 💡 declare
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9

print(numbers)


# 💡 modify
numbers = list(numbers)

numbers[2] = 10

numbers = tuple(numbers)
# 💡
# 💡
# 💡