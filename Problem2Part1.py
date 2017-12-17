

import sys


def main(argv):

    if len(argv) < 0:
        print "I need a filename!"
        sys.exit(1)
    else:
        filename = argv[0]

    with open(filename, 'r') as file_ptr:
        line_arr = file_ptr.readlines()

    well_formed_arr = []
    for line in line_arr:
        well_formed_arr.append([int(x) for x in line.strip().rstrip().split('\t')])

    accum = 0
    for line in well_formed_arr:
        min = 1e7
        max = 0
        for elem in line:
            if elem < min:
                min = elem
            if elem > max:
                max = elem
        accum += (max - min)

    print accum


if __name__ == "__main__":
    main(sys.argv[1:])