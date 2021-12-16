# Customizing string representations of classes


class Person:
    def __init__(self):
        # first name
        self.firstname = "Jessica"
        # last name (last name)
        self.lastname = "Temporal"
        self.age = 25

    # Use __repr__ to create a string that is useful for debugging
    def __repr__(self):
        text = "<Person Class - name: {0}, surname: {1}, age{2}>"
        return text.format(self.firstname, self.lastname, self.age)

    # Use __str__ to create a human-friendly string
    def __str__(self):
        text = "Person {0} {1} is {2} years old."
        return text.format(self.firstname, self.lastname, self.age)

    # Use bytes to convert the string into a bytes object
    def __bytes__(self):
        data = [self.firstname, self.lastname, self.age]
        to_bytes = "Person:{0}:{1}:{2}".format(*data)
        return to_bytes.encode("utf-8")


def main():
    # Creating an instance of Person
    person = Person()

    # Using Python's built-in functions to impersonate the person
    # in a string
    print(repr(person))
    print(str(person))
    print("Format: {0}".format(person))
    print(bytes(person))


if __name__ == "__main__":
    main()