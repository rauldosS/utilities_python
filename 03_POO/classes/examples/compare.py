# Using magic methods to compare objects to each other


class Person():
    def __init__(self, firstname, lastname, level, years_worked):
        self.firstname = firstname
        self.lastname = lastname
        self.level = level
        self.seniority = years_worked

    # Implement comparisons using each person's level
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level


def main():
    # Defining people
    department = []
    department.append(Person("Túlio", "Toledo", 5, 9))
    department.append(Person("John", "Junior", 4, 12))
    department.append(Person("Jessica", "Temporal", 6, 6))
    department.append(Person("Rebekah", "Robinson", 5, 13))
    department.append(Person("Thiago", "Tavares", 5, 12))

    # Finding out who is more senior
    print(bool(department[0] > department[2]))
    print(bool(department[4] < department[3]))

    # Organizing people by seniority
    people = sorted(department)
    
    for person in people:
        print(person.firstname)

if __name__ == "__main__":
    main()