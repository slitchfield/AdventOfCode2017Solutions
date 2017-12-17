

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
    stride = len(input_list) / 2
    for idx in range(len(input_list)):
        cur_val = input_list[idx]
        target_val = input_list[(idx + stride) % len(input_list)]
        if cur_val == target_val:
            sum += cur_val

    print sum


if __name__ == "__main__":
    main(sys.argv[1:])