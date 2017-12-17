def main(numstring):
    accumulator = 0
    string_length = len(numstring)
    half_string = string_length / 2

    for idx, digit in enumerate(numstring):
        if digit == numstring[(idx + half_string) % string_length]:
            accumulator += int(digit)

    return accumulator


if __name__ == '__main__':
    with open('1-input.txt') as inputfile:
        result = main(inputfile.read().rstrip())
        print(result)
