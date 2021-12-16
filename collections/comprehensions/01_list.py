# Using list comprehensions


def main():
    # Defining two lists of odd and even numbers
    pairs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # Use map() and filter() to limit list items
    square_pairs = list(
        map(lambda n: n ** 2, filter(lambda n: n > 4 and n < 16, pairs))
    )
    print(square_pairs)

    # Create a new list from a preexisting list
    square_pairs = [n ** 2 for n in pairs]
    print(square_pairs)

    # Use predicate to limit list items
    odd_square = [n ** 2 for n in odd if n > 3 and n < 17]
    print(odd_square)


if __name__ == "__main__":
    main()