import csv


def main(inputfile):
    sheetreader = csv.reader(inputfile, delimiter='\t')
    accumulator = 0
    for row in sheetreader:
        row_ints = map(int, row)
        max_digit = max(row_ints)
        min_digit = min(row_ints)
        accumulator += max_digit - min_digit
    return accumulator


if __name__ == '__main__':
    with open('2-input.txt') as inputfile:
        result = main(inputfile)
        print(result)
