# Using iterator functions like enumerate, zip, iter, next

def main():
    # Define the weekday list in Portuguese and English
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    days_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # Use the iter function to create an iterator over a list
    iterator_days = iter(days)
    print(next(iterator_days))  # Sun
    print(next(iterator_days))  # sec
    print(next(iterator_days))  # Have

    # Use a function to iterate over a file
    with open("data.txt", "r") as fp:
        for line in iter(fp.readline, ""):
            print(line)

    # Use traditional iteration (range) over the days list
    for m in range(len(days)):
        print(m + 1, days[m])

    # Using the enumerate function reduces the amount of code and
    # give a counter
    for i, m in enumerate(days, start=1):
        print(i, m)

    # Use the zip function to combine lists
    for m in zip(days, days_en):
        print(m)

    # Combine zip with enumerate to format the result
    for i, m in enumerate(zip(days, days_en), start=1):
        print(i, m[0], "=", m[1], "in English")

if __name__ == "__main__":
    main()