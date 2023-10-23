def find_max(numbers):
    maximum = numbers[0] # shift+F6 is the shortcut for refactoring
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum