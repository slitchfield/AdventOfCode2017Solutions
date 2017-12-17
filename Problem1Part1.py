

import sys


def main(argv):


    if len(argv) < 1:
        print "I need an input filename!"
        sys.exit(1)
    else:
        input_filename = argv[0]

    with open(input_filename, 'r') as input_file:
        input_string = input_file.readlines()[0].strip().rstrip()

    input_list = []
    for char in input_string:
        input_list.append(int(char))

    sum = 0
    for idx in range(len(input_list)):

        # First check if this is the last element
        if idx == len(input_list) - 1:
            # Need to check against first element of the list!
            if input_list[idx] == input_list[0]:
                sum = sum + input_list[idx]
        else:
            if input_list[idx] == input_list[idx + 1]:
                sum = sum + input_list[idx]

    print sum


if __name__ == "__main__":
    main(sys.argv[1:])