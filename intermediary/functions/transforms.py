# Using transforming functions: sorted, filter, map


def first_filter(x):
    if x % 2 == 0:
        return False
    return True

def second_filter(x):
    if x.isupper():
        return False
    return True

def squared(x):
    return x**2

def note_to_concept(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"

def main():
    # Defining sequences for us to use in this task
    numbers = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    letters = "abcDeFGHiJklmnoP"
    notes = (81, 89, 94, 78, 61, 66, 99, 74)

    # Use filter to remove items from a list
    odd = list(filter(first_filter, numbers))
    print(odd)

    # Use filter on a string
    lowercase = list(filter(second_filter, letters))
    print(lowercase)

    # Use map to create a new value sequence
    squares = list(map(squared, numbers))
    print(squares)

    # Use sorted and map to change notes to concept
    notes = sorted(notes)
    letters = list(map(note_to_concept, notes))
    print(letters)


if __name__ == "__main__":
    main()