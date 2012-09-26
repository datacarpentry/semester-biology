Making Choices
==============

    number = -2
    if number < 0:
        abs_value = -1 * number
    elif number > 0:
        abs_value = number
    return abs_value


    def abs(number):
        if number < 0:
            abs_value = -1 * number
        elif number > 0:
            abs_value = number
        return abs_value

Demonstrate the function.

    abs(-5)
    abs(10)

And we can then combine this with loops to do the same thing repeatedly.

    numbers = [1, 7, -2, -8, 23, 17, -42]

    results = []
    for item in numbers:
        results.append([abs(item)])

    print results