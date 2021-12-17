# Using OrderedDict objects
from collections import OrderedDict


def main():
    # List of teams with number of lost and won matches
    times_fut = [
        ("Cruise", (18, 12)),
        ("Vasco", (24, 6)),
        ("Avaí", (20, 10)),
        ("Flemish", (22, 8)),
        ("Palm trees", (15, 15)),
        ("Saints", (20, 10)),
        ("Botafogo", (16, 14)),
        ("Fluminense", (25, 5)),
    ]

    # Sorting teams by number of wins
    times_ord = sorted(times_fut, key=lambda t: t[1][0], reverse=True)

    # Create an ordered dictionary with teams
    times = OrderedDict(times_ord)
    print(times)

    # Use popitem to remove top item
    name, stat = times.popitem(False)
    print("Most winning team: ", name, stat)

    # Take an equality test
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    print("Equality test: ", a == b)


if __name__ == "__main__":
    main()
