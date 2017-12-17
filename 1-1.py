def main(numstring):
    accumulator = 0
    for idx, digit in enumerate(numstring):
        # Do nothing for the first digit
        if idx == 0:
            continue

        # Do something special for the last digit
        if idx == len(numstring) - 1 and digit == numstring[0]:
            accumulator += int(digit)
            continue

        # For the standard case
        if digit == numstring[idx - 1]:
            accumulator += int(digit)

    return accumulator


if __name__ == '__main__':
    with open('1-input.txt') as inputfile:
        result = main(inputfile.read().rstrip())
        print(result)
