# Simple program to convert from Celsius to Fahrenheit and vice versa.

import time
import multiprocessing


def main():
    user_input = int(input("Enter number: "))

    f = user_input
    c = user_input

    f_to_c = 5/9 * (f-32)
    c_to_f = (c * 9 / 5) + 32

    print("\nFahrenheit to celsius: {}".format(f_to_c))
    print("Celsius to fahrenheit: {}".format(c_to_f))


if __name__ == "__main__":
    main()


# formula found at: https://www.thoughtco.com/fahrenheit-to-celsius-formula-609230
