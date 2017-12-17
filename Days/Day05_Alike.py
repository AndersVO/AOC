from typing import List
def steps_to_ext(jumps: List[int]) -> int:

    jumps = jumps[:]
    current_index = 0
    num_steps = 0

    while current_index >= 0 and current_index < len(jumps):
        jumpSize = jumps[current_index]
        jumps[current_index] += 1
        current_index += jumpSize
        num_steps += 1

    return num_steps

def steps_to_ext2(jumps: List[int]) -> int:

    jumps = jumps[:]
    current_index = 0
    num_steps = 0

    while current_index >= 0 and current_index < len(jumps):
        jumpSize = jumps[current_index]
        if jumps[current_index] == 3:
            jumps[current_index] -= 1
        else:
            jumps[current_index] += 1
        current_index += jumpSize
        num_steps += 1

    return num_steps

TEST_OFFSETS = [0, 3, 0, 1, -3]
assert steps_to_ext(TEST_OFFSETS) == 5
assert steps_to_ext2(TEST_OFFSETS) == 10

if __name__ == "__main__":
    with open("day05_input.txt", "r") as f:
        jumps = [int(line) for line in f]
    print(steps_to_ext(jumps))
    print(steps_to_ext2(jumps))


