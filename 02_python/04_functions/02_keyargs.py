# Use of named arguments


# Use only named arguments to ensure code clarity
def my_function(arg1, arg2, *, suppress_exceptions=False):
    print(arg1, arg2, suppress_exceptions)

def main():
    # Try calling the function without the argument name
    # my_function(1, 2, True)
    my_function(1, 2, suppress_exceptions=True)

if __name__ == "__main__":
    main()