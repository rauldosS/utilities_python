# Using namedtuple objects
import collections


def main():
    # Create a namedtuple to store coordinates
    coordinates = collections.namedtuple("Coordinates", "x y")

    p1 = coordinates(10, 20)
    p2 = coordinates(30, 40)

    print(p1, p2)
    print(p1.x, p1.y)

    # Use _replace() to create a new instance
    p1 = p1._replace(x=100)
    print(p1)


if __name__ == "__main__":
    main()
