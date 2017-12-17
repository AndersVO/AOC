from typing import List
import itertools

def redistribute(memorybanks: List[int]) -> int:
    number_of_banks = len(memorybanks)

    # find the block with most data
    max_value = max(memorybanks)
    max_block_idx = min(i for i, value in enumerate(memorybanks) if value == max_value)
    #print(max_block_idx)
    #Take the memory out
    memory_to_distribute = max_value
    memorybanks[max_block_idx] = 0

    #set idx to next block
    idx = (max_block_idx + 1) % number_of_banks
    #distribute memory


    for i in range(memory_to_distribute):
        memorybanks[idx] += 1
        idx = (idx + 1) % number_of_banks
        #print(idx)


def loop_size(memorybanks: List[int]) -> int:

    memorybanks = memorybanks[:]
    first_seen = { tuple(memorybanks): 0}

    for cycle in itertools.count(1):
        redistribute(memorybanks)
        as_tuple = tuple(memorybanks)

        if as_tuple in first_seen:
            return cycle - first_seen[as_tuple]
        else:
            first_seen[as_tuple] = cycle


def how_many_cycles(memorybanks: List[int]) -> int:


    memorybanks = memorybanks[:]

    seen = {tuple(memorybanks)}

    for cycle in itertools.count(1):
        redistribute(memorybanks)
        as_tuple = tuple(memorybanks)
        if as_tuple in seen:
            return cycle
        else:
            seen.add(as_tuple)


if __name__ == "__main__":
    INPUT = """5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6"""
    memorybanks = [int(x) for x in INPUT.split()]
    print(how_many_cycles(memorybanks))
    print(loop_size(memorybanks))
