# Use of variable arguments


# Define a function that takes variable arguments
def addition(*args):
    return sum(args)

# Function with a positional argument
# def addition(base, *args):
# return sum(args)

def main():
    # Pass different arguments to the addition() method
    print(addition(5, 10, 15, 20))
    print(addition(1, 2, 3))

    # Pass a list to the addition() method
    numbers = [5, 10, 15, 20]
    print(addition(*numbers))

if __name__ == "__main__":
    main()


    multiplication_lambda = lambda x, y: x > y

    print(multiplication_lambda(2, 2))