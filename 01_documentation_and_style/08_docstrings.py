# Using docstrings to document methods


def my_function(arg1, arg2=None):
    """My function that does a print

    Params:
        arg1: first argument. Whatever you want to spend.
        arg2: second argument. Default: None. Whatever makes you happy.
    """
    print(arg1, arg2)

def main():
    print(my_function.__doc__)

if __name__ == "__main__":
    main()