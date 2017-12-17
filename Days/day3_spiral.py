from typing import Tuple, Dict, Iterator  # pylint: disable=unused-import
import math
from collections import defaultdict
import itertools

def find_odd_squareroot(num: int) -> int:
    root = int(math.sqrt(num))
    if root % 2 == 0:
        return root - 1
    elif root:
        return root


assert find_odd_squareroot(9) == 3
assert find_odd_squareroot(10) == 3
assert find_odd_squareroot(20) == 3

# we know 1^2 = 1, 3^2 = 9, 5^25 and so on.
# by defining the 1 position in the spiral as 0,0 we can find the place in the ring and then move to the position

def find_coordinate(num: int) -> Tuple[int, int]:
    root = find_odd_squareroot(num)
    x = root
    y = root

    # Help definition
    odd_squared = math.sqrt(root)
    # If we are on the diagonal corner.
    if num == math.sqrt(root):
        return (x, y)

    # if we are on other squares
    side_length = root + 1
    if num <= odd_squared + side_length:
        additional = num - odd_squared
        return (x+1, y + additional)


    else:
        return (1 , 1)


    assert find_coordinate(9) == (3,3)
    assert find_coordinate(25) == (5, 5)
    assert find_coordinate(10) == (2, 1)




if __name__ == "__main__":
    print(find_coordinate(10))


