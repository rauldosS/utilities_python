import math

PI = math.pi

def convert_number(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            # return default None
            pass

def multiplication(n1, n2):
    return n1 * n2

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(multiplication(4, 3))
    print(PI)