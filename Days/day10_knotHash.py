"""
http://adventofcode.com/2017/day/10
"""
from typing import List



def rotate(num: List[int],skips: List[int] ) -> List[int]:
    skips = encode(skips)
    current_pos = 0
    skip_size = 0
    seq_length = len(num)
    for rounds in range(64):
        for skip in skips:
            start = current_pos % len(num)
            end = (current_pos + skip) % len(num)
            if start < end:
                print("start", start)
                print("end", end)
                num_in_focus = num[start:end]
                print("num in focus", num_in_focus)
                focus_reversed = reversed(num_in_focus)
                num[start:end] = focus_reversed
                print(num)

            elif end < start:
                # visual example
                # 1    2    3   4   5   6   7
                #     end         start
                # 6    5    3   4   2   1   7
                print("OVERFLOW BEFORE")
                print(num)
                num_in_focus = num[start:] + num[:end]
                print("num in focus", num_in_focus)
                focus_reversed = list(reversed(num_in_focus))
                print(focus_reversed)
                num[start:] = focus_reversed[:(seq_length-start)]
                num[:end] = focus_reversed[(seq_length-start):]
                print("OVERFLOW AFTER")
                print(num)

            current_pos = (start + skip_size + skip)
            skip_size +=1
    return num

def encode(s: str) -> List[int]:
    return [ord(c) for c in s] + [17, 31, 73, 47, 23]

assert encode("1,2,3") == [49,44,50,44,51,17,31,73,47,23]

def xor16(xs: List[int]) -> int:
    """
    xor all 16 numbers together
    """
    assert len(xs) == 16

    result = xs[0]
    for x in xs[1:]:
        result = result ^ x

    return result

assert xor16([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]) == 64


def sparse_to_dense(xs: List[int]) -> List[int]:
    assert len(xs) == 256

    return [xor16(xs[start:(start+16)])
            for start in range(0, 256, 16)]

assert sparse_to_dense([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22] * 16) == [64] * 16

def hexit(x: int) -> str:
    # hex returns something like '0x1' or '0xff'
    # we need to throw away the first two chars
    # and maybe add a leading 0
    h = hex(x)[2:]

    assert 1 <= len(h) <= 2

    return h if len(h) == 2 else '0' + h


if __name__ == "__main__":
    Lengths = "225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110"
    xor_sparsed_hash = []
    list_of_numbers = list(range(256))
    hashed_knot = rotate(list_of_numbers, Lengths)
    print(hashed_knot)

    xor_dense_hash = sparse_to_dense(hashed_knot)
    hex_dense_hash = ''.join([hexit(x) for x in xor_dense_hash])
    print("Multiplied 1st and 2nd", hex_dense_hash)