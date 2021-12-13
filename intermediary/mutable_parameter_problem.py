'''
    → Mutable parameter problem

    → Mutable
        lists, dictionaries
    → Immutable
        Tuples, Strings, Numbers, True, False, None
'''

# The separate lists come together, that's the problem

# 💡 Solution

'''
    Mutable parameters must not be used in functions

    If necessary, pass an immutable value as default.
    In the example, None is passed to the list parameter.
'''

def clients_list(iteravel_clients, list=None):
     if list is None:
         list = []
     list.extend(iteravel_clients)
     return list


clients_list_1 = ['Manufacture']

clients1 = clients_list(['João', 'Maria', 'Eduardo'], clients_list_1)
clients2 = clients_list(['Marcos', 'Jonas', 'Zico'])
clients3 = clients_list(['José'])

print(clients1)
print(clients2)
print(clients3)