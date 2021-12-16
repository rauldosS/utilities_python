# Customizing the string representation of a class


class MyColors:
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # Use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgb":
            return (self.red, self.green, self.blue)
        else:
            raise AttributeError

    # Use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgb":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # Use dir to list available properties
    def __dir__(self):
        return ("red", "green", "blue", "rgb")


def main():
    # Creating an instance of MyColors
    colors = MyColors()

    # Set the value of an attribute
    print(colors.rgb)

    # Set the value of an attribute
    colors.rgb = (125, 200, 86)
    # rgb(75, 139, 190) # blue
    # rgb(255, 232, 115) # yellow
    print(colors.rgb)

    # Access a specific attribute
    print(colors.red)

    # List available attributes
    print(dir(colors))


if __name__ == "__main__":
    main()
