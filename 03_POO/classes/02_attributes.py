'''
    → Class attributes
        → They are variable of class

        → Whether the value of the class variable in all instances will be changed too
'''

# declare
class People:
    planet = 'Earth'

raul = People()

# change value through class
People.planet = 'Other planet'

# change value through instance
# If a class variable is changed through an instance, the variable will be created in the 
# instance, that is, the value of the class variable is not actually changed.
raul.planet = 'Lastter'