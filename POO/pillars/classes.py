# 💡 Simple inheritance
# 💡 What attributes are common in the client and student class

from datetime import datetime

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.name_class = self.__class__.__name__

    def speak(self):
        print(f'{ self.name  } talking!')

class Client(People):
    def buy(self):
        print(f'{ self.name } is buying!')

class Student(People):
    def study(self):
        print(f'{ self.name } is studying!')

class ClientVIP(People):
    # 💡 method overlay (__init__)
    def __init__(self, name, age, surname):
        super().__init__(name, age)
        self.surname = surname

    # 💡 method overlay (speak)
    def speak(self):
        # 💡 super executes the first "speak" function found (client in this case)
        super().speak()

        # 💡 Execute method of specific class
        People.speak(self)
        Client.speak(self)

        print(f'{ self.name } { self.surname } talking!')

# 💡 Multiple inheritance

''' 
    💡 Diamond problem

    If a class inherits from two classes, there can be a conflict of implementations.
    Inheritance will be applied from left to right.

    → Class A
    → Class B
    → Class C(A, B)
'''

# 💡 Mixins Class

# 💡 Electronic
class Electronic:
    def __init__(self, name):
        self._name = name
        self._turned_on = False

    def turnOn(self):
        if self._turned_on:
            return
        self._turned_on = True

    def turnOff(self):
        if not self._turned_on:
            return
        self._turned_on = False

# 💡 Log system
class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(f'{ msg }\n')

    def logInfo(self, msg):
        self.write(f'Info: { msg } - { datetime.now() }')

    def logError(self, msg):
        self.write(f'Info: { msg } - { datetime.now() }')

# 💡 Subclass of Electronic
class Smartphone(Electronic, LogMixin):
    def __init__(self, name):
        super().__init__(name)
        self._online = False

    def connect(self):
        if not self._turned_on:
            self.logInfo(f'{ self._name } not connected!')
            return
        
        if self._online:
            self.logError(f'{ self._name } is already connected!')
            return

        self.logInfo(f'{ self._name } is connected!')
        self._online = True

    def disconnect(self):
        if not self._online:
            self.logInfo(f'{ self._name } not connected!')
            return
        self._online = False
    
smartphone = Smartphone('MI 9')

smartphone.connect()

smartphone.turnOn()
smartphone.connect()

# 💡 
# 💡 
# 💡 