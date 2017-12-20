"""
http://adventofcode.com/2017/day/10
"""
from typing import List



def rotate(num: List[int],skips: List[int] ) -> List[int]:
    skips = encode(skips)
    current_pos = 0
    skip_size = 0
    seq_length = len(num)
    for range(64):
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

def xor(xs: List[int]) -> int:
    assert len(xs) == 16

    result = xs[0]
    for x in xs[1:]:
        result = result ^ x

    return result



if __name__ == "__main__":
    Lengths = "225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110"
    list_of_numbers = list(range(256))
    hashed_knot = rotate(list_of_numbers, Lengths)
    print(hashed_knot)
    print("Multiplied 1st and 2nd", hashed_knot[0]* hashed_knot[1])
