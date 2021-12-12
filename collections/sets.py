'''
    → Sets are collections of unordered elements that do not allow duplicate items, that is, 
    their elements are unique.
    
    → Sets cannot be changed (immutable)
    → Not ordered
    → Does not accept duplicate elements

    → When to use?
        It is recommended to use this type of collection when we want to work with single 
        elements. We can also use sets when there is a need to perform mathematical 
        operations with elements from different sets. Remember that because a set is 
        unordered, the elements can be in a different order each time the code runs.
'''

# 💡 declare
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

s1 = set()

# 💡 add
s1.add(1)

# 💡 discard
s1.discard(1)

# 💡 update - iterate over the value
s1.update('Python') # result = {'P', 'y', 't', 'h', 'o', 'n'}

# 💡 union
s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

s3 = s1 | s2

# 💡 intersection & - all elements present in both sets
s3 = s1 & s2

# 💡 difference '-' - elements only on the left set
s3 = s1 - s2
s3 = s2 - s1

# 💡 symmetric_difference ^ - elements that are in both sets, but not both
s3 = s1 ^ s2

# 💡 
# 💡 