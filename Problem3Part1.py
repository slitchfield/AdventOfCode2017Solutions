

import sys
import numpy as np


def main(argv):
    #location = 277678
    location = 13

    # Problem reduces to finding x/y coord of puzzle input, given that successive integers move in a spiral
    # Note that 1 lives at (0, 0), 2 lives at (1, 0), 3 lives at (1, 1), etc
    # Number of elements on each "shell" is the difference between successive odd squares
    # First element on that shell is (n-2)^2 + 1, located at ((n-1)/2, -(n-1)/2+1) <-- y coord has a special case where
    #   n == 1

    # Problem then becomes, what shell is the location on, and where does it lie in that shell?

    # Find the shell!
    # Equivalent to taking square root and rounding down to nearest odd integer

    shell = int(np.sqrt(location))
    if shell % 2 == 0:
        shell = shell - 1
    #shell = shell + 2
    my_shell = shell+2

    print shell
    print "Shell starts at ({0}, {1})".format((my_shell-1)/2, -(my_shell-1)/2+1)
    offset = location - (shell*shell + 1)
    print offset
    side = int(offset / shell) # 0 = right, 1 = top, 2 = left, 3 = bottom
    print side
    side_offset = (offset-1) % shell
    print side_offset

    # Need to find location of corners:
    starting_point = ((my_shell-1)/2, -(my_shell-1)/2+1)
    bottom_left = (-(my_shell-1)/2, -(my_shell-1)/2)
    bottom_right = ((my_shell - 1)/2, -(my_shell-1)/2)
    top_right = ((my_shell-1)/2, (my_shell-1)/2)
    top_left = (-(my_shell-1)/2, (my_shell-1)/2)

    corners = [starting_point, top_right, top_left, bottom_left]

    relevant_corner = corners[side]
    print relevant_corner

    if side == 0:
        coords = (relevant_corner[0], relevant_corner[1] + side_offset)
    elif side == 1:
        coords = (relevant_corner[0] - side_offset, relevant_corner[1])
    elif side == 2:
        coords = (relevant_corner[0], relevant_corner[1] - side_offset)
    elif side == 3:
        coords = (relevant_corner[0] + side_offset, relevant_corner[1])

    print coords
    print abs(coords[0]) + abs(coords[1])


if __name__ == "__main__":

    main(sys.argv[1:])