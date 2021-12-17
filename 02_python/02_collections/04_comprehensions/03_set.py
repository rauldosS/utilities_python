# Using set comprehensions


def main():
    # Defining a list of temperatures
    celsius_temps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # Create a set with temperatures in Fahrenheit
    # Tip: Formula to convert to Fahrenheit -> (t * 9/5) + 32
    fahrenheit_list = [(t * 9 / 5) + 32 for t in celsius_temps]
    fahrenheit_set = {(t * 9 / 5) + 32 for t in celsius_temps}
    print(fahrenheit_list)
    print(fahrenheit_set)

    # Create a set from a string
    sentence = "The first Brazilian podcast on data science"
    letters = {c.upper() for c in sentence if not c.isspace()}
    print(letters)


if __name__ == "__main__":
    main()
