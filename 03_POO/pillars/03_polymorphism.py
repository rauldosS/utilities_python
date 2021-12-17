'''
    → Overlap polymorphism

    → Polymorphism is the principle that allows classes derived from the same superclass to 
    have the same methods (with the same signature) but different behaviors.

    → Same signature = Same number of parameters
'''

# Example
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def speak(self, msg): pass

class B(A):
    def speak(self, msg):
        print(f'B is talking { msg }!')

class C(A):
    def speak(self, msg):
        print(f'C is talking { msg }!')

b = B()
c = C()

b.speak('Hello!')
c.speak('Hello!')
# 
# 
# 
# 
# 
# 