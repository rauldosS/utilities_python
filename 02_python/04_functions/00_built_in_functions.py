# Getting to know built-in functions


def main():
    # Use any() and all() to test for boolean values
    list = [1, 2, 3, 0, 5, 6]

    # The any function will return true if any value in the list
    # be true
    print(any(list))

    # The all function will return true only if all values of the
    # list are true
    print(all(list))

    # The min and max functions return the minimum and maximum values
    # respectively
    print("minimum:", min(list))
    print("max:", max(list))

    # Use sum() to sum all values in the list
    print("sum: ", sum(list))


if __name__ == "__main__":
    main()
