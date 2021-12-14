# 💡 Simple inheritance
# 💡 What attributes are common in the client and student class

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


# 💡 