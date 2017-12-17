import csv

from itertools import permutations


def main(inputfile):
    sheetreader = csv.reader(inputfile, delimiter='\t')
    accumulator = 0
    for row in sheetreader:
        row_ints = map(int, row)
        pairs = permutations(row_ints, 2)
        for pair in pairs:
            # If the first number is evenly divisible by the second
            # add them to the accumulator
            if pair[0] % pair[1] == 0:
                accumulator += pair[0]/pair[1]
    return accumulator


if __name__ == '__main__':
    with open('2-input.txt') as inputfile:
        result = main(inputfile)
        print(result)
