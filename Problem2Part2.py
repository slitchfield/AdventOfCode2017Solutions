

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
        # Now, instead of mins/maxes, looking for evenly divisible numbers
        # We could be smart about this, but for every element, just check every other element
        for dividend_idx in range(len(line)):
            for divisor_idx in range(len(line)):
                if dividend_idx != divisor_idx:
                    if line[dividend_idx] % line[divisor_idx] == 0:
                        accum += (line[dividend_idx] / line[divisor_idx])

    print accum


if __name__ == "__main__":
    main(sys.argv[1:])