'''
    → Encapsulation

    → Grouping data with the methods that operate on that data or restricting direct 
    access to some of the components of an object.
'''

# In others languages

'''
    Private: The access level of a private modifier is only within the class. 
    It cannot be accessed from outside the class.

    Default: The access level of a default modifier is only within the package. 
    It cannot be accessed from outside the package. If you do not specify any access level, 
    it will be the default.

    Protected: The access level of a protected modifier is within the package and outside 
    the package through child class. If you do not make the child class, it cannot be 
    accessed from outside the package.

    Public: The access level of a public modifier is everywhere. It can be accessed 
    from within the class, outside the class, within the package and outside the package.
'''

# In Python

'''
    → There are no access modifications in Python.

    → There is a convention.

    _ protected
    __ private

    _
        → If the attribute contains an underscore character in front of its name, 
        it is recommended that this attribute not be accessed outside of the class.
        → Can be called as Protected at the convention.

    __
        → If the attribute contains two underscore characters in front of its name, 
        it is strongly recommended that this attribute not be accessed outside of the class.
        → Can be called as Private at the convention.
'''

class DataBase:
    def __init__(self):
        self.__datas = {}

    @property
    def dadas(self):
        return self.__datas

    def insertClient(self, id, name):
        if 'clients' not in self.__datas:
            self.__datas['clients'] = { id: name }
        else:
            self.__datas['clients'].update({ id: name })

    def get_clients(self):
        for id, name in self.__datas['clients'].items():
            print(id, name)

    def delete_client(self, id):
        del self.__datas['clients'][id]

data_base = DataBase()

data_base.insertClient(1, 'Raul')
data_base.insertClient(2, 'André')
data_base.insertClient(3, 'Luana')

print(data_base.delete_client(2))
print(data_base.get_clients())

print('getter value attribute:', data_base.dadas)
print('real value attribute:', data_base._DataBase__datas)

# 
# 
# 
# 