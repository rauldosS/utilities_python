# Using the Counter class
from collections import Counter


def main():
    # A list of students in class A
    class_a = [
        "Bárbara",
        "John",
        "Carlos",
        "Dario",
        "Priscilla",
        "Ana" "Kevin",
        "John",
        "Marina",
        "Bianca",
        "Gustavo",
        "Fernanda",
    ]

    # A list of students in class B
    class_b = [
        "Hiro",
        "Bruno",
        "Claudia",
        "Débora",
        "Fernanda",
        "Gabriela",
        "Leticia",
        "João",
        "Jairo",
        "Samuel",
        "Taciana",
        "Gabriel",
    ]

    # Create a Counter for classes A and B
    a = Counter(class_a)
    b = Counter(class_b)

    # How many students in class A are named John?
    print(a["John"])

    # How many students are in class A?
    print(sum(a.values()), "students in class A")

    # Combine the two classes
    a.update(class_b)
    print(sum(a.values()), "students in class B")

    # What are the 3 most common names in both classes?
    print(a.most_common(3))

    # Separate the two classes and show the most common class name to
    a.subtract(class_b)
    print(a.most_common(3))

    # What is the intersection of names between the two classes?
    print(a & b)

if __name__ == "__main__":
    main()