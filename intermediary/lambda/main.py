# Using lambdas as one-line functions


def celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32

def fahrenheit_para_celsius(temp):
    return (temp - 32) * 5 / 9

def main():
    temp_in_celsius = [0, 12, 34, 100]
    temp_in_fahrenheit = [32, 65, 100, 212]

    # Use regular functions to convert temps
    print(list(map(fahrenheit_para_celsius, temp_in_fahrenheit)))
    print(list(map(celsius_to_fahrenheit, temp_in_celsius)))

    # Use lambdas to accomplish the same thing
    print(list(map(lambda t: (t - 32) * 5 / 9, temp_in_fahrenheit)))
    print(list(map(lambda t: (t * 9 / 5) + 32, temp_in_celsius)))

if __name__ == "__main__":
    main()
