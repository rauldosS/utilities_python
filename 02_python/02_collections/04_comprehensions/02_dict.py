# Using dict comprehensions


def main():
    # Defining a list of temperatures
    temps = [0, 12, 34, 100]

    # Use a comprehension to build a dictionary
    # Tip: Formula to convert to Fahrneheit -> (t * 9/5) + 32
    temp_diction = {t: (t * 9 / 5) + 32 for t in temps if t < 100}
    print(temp_diction)
    print(temp_diction[12])

    # Defining two teams
    time_a = {"John": 24, "Jessica": 18, "Gustavo": 58, "Barbara": 7}
    time_b = {"Leticia": 12, "Gabriel": 88, "Joseph": 4}
    teams = (time_a, time_b)

    # Combining two dictionaries with one comprehension
    new_time = {k: v for time in teams for k, v in time.items()}
    print(new_time)


if __name__ == "__main__":
    main()
