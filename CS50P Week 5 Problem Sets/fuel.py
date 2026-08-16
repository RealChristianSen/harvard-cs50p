def main():

    fraction = input("Fraction: ")

    print(convert(fraction))


def convert(fraction):

    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError

    if y < x or x < 0 or y < 0:
        raise ValueError

    try:
        return round((x / y) * 100)

    except ValueError:
        raise ValueError


def gauge(percentage):

    if percentage >= 99:
        return "F"

    if percentage <= 1:
        return "E"

    return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
