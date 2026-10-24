#!/usr/bin/python3
"""
FizzBuzz implementation
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function
    """
    if n < 1:
        return

    tmp_list = []
    for i in range(1, n + 1):
        # Check for numbers divisible by both 3 and 5 first
        if i % 3 == 0 and i % 5 == 0:
            tmp_list.append("FizzBuzz")
        # Check for numbers divisible by 3 only
        elif i % 3 == 0:
            tmp_list.append("Fizz")
        # Check for numbers divisible by 5 only
        elif i % 5 == 0:
            tmp_list.append("Buzz")
        # Otherwise, append the number itself
        else:
            tmp_list.append(str(i))

    print(" ".join(tmp_list))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(1)

    fizzbuzz(int(sys.argv[1]))
