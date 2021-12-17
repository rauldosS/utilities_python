"""
PEP 8 - Style Guide for Python Code

https://www.python.org/dev/peps/pep-0008/
"""


"""
    💡 Code structure and formatting

        💡 The import lines are at the top of the file, and each import must have its own line.
        💡 Use indentation consistently, prefer spaces over tabs
        💡 Use 4 spaces for each indentation level
        💡 Limit your lines to 79 characters (72 for docstrings/comments)

        💡 Class methods are separated by a single blank line

        💡 Do not use spaces between function calls, indexes, and named arguments
"""

"""
    💡 White Space Conventions
"""

"""💡                 Do it                                           Avoid it
                                                        
            function(list[1], {'key': 2})                function( list[ 1 ], { 'key': 2 } )

            function(param)                              function( param )

            dictionary['key'] = list[1]                  dictionary ['key'] = list [index]

            x = 1                                        x = 1
            y = 2                                        y = 2
            long_variable = 3                            long_variable = 3
            
            hypotenuse = x*x + y*y                       hypotenuse = x * x + y * y
            
            i = i + 1                                    I = I + 1
"""

'''
    💡 Fun Facts About Naming Conventions!

    As you saw in the previous lesson, we use certain conventions for naming variables, functions, 
    classes, and so on. These conventions have a name that we can use to refer to how we are 
    naming certain objects in our program: PascalCase, camelCase, and snake_case.

    💡 PascalCase:
        Means that all words start with a capital letter and nothing is used to separate them, like in: 
        MyClass, Class, MyObject, MyVeryCoolProgram. This is the convention used for classes in Python;

    💡 camelCase:
        the only difference from camelCase to PascalCase is the first letter. 
        In camelCase the first letter will always be lowercase and the rest of the words must 
        start with a capital letter. As in: myFunction,SumFunction, etc... This cast isn't 
        used in Python (although I confuse the two and sometimes end up calling camelCase 
        PascalCase or vice versa, but now you know the difference);

    💡 snake_case:
        This is the pattern used in Python to define anything that isn't a class. 
        All letters will be lowercase and separated by an underline, as in: my_variable, 
        legal_function, sum.

    The defaults used in Python are: snake_case for anything and PascalCase for classes.
'''

"""
    💡 Coding Style Example
"""

# each import must have its own line
import sys
import os

# two blank lines separate classes from other functions
class MyClass:
    def __init__(self):
        self.description = "My Class"

    # inside a class, we use a blank line between methods
    def my_method(self, arg1):
        pass


def main():
    # comments that use more than one line, must be limited to 72
    # characters per line
    instance = MyClass()
    print(instance.description)
    instance.descricao = "Jess's class"
    print(instance.description)


if __name__ == "__main__":
    main()