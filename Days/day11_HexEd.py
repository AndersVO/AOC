"""
--- Day 11: Hex Ed ---
Crossing the bridge, you've barely reached the other side of the stream when a program comes up to you, clearly in distress. "It's my child process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes can be found to the north, northeast, southeast, south, southwest, and northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \
You have the path the child process took. Starting where he started, you need to determine the fewest number of steps required to reach him. (A "step" means to move from the hex you are in to any adjacent hex.)

For example:

ne,ne,ne is 3 steps away.
ne,ne,sw,sw is 0 steps away (back where you started).
ne,ne,s,s is 2 steps away (se,se).
se,sw,se,sw,sw is 3 steps away (s,s,sw).
"""
from typing import Dict
from collections import defaultdict, Counter
from copy import copy



def eliminate_opp(counts: Dict[str, int]) -> bool:
    # subtract the ones that are opposite
    # first find lowest number in opposites
    n_s = min(counts['n'], counts['s'])
    nw_se = min(counts['nw'], counts['se'])
    ne_sw = min(counts['ne'], counts['sw'])
    if n_s > 0 or nw_se > 0 or ne_sw > 0:
        # subtract
        counts['n'] -= n_s
        counts['s'] -= n_s
        counts['nw'] -= nw_se
        counts['se'] -= nw_se
        counts['ne'] -= ne_sw
        counts['sw'] -= ne_sw
        return True
    else:
        return False

def condense(counts: Dict[str,int]) -> bool:
    # idea here is that a combination of 2 steps can be simplified to one step
    #    [nw ne] -> n
    #    [n se] -> ne
    #    [ne s] -> se
    #    [se nw] -> s
    #    [s nw] -> sw
    #    [sw n] -> nw
    answer = False
    for m1, m2, p in [
        ('n', 'se', 'ne'),
        ('ne', 's', 'se'),
        ('se', 'sw', 's'),
        ('s', 'nw', 'sw'),
        ('sw', 'n', 'nw'),
        ('nw', 'ne', 'n')]:

        transform = min(counts[m1], counts[m2])

        if transform > 0:
            answer = True
            counts[m1] -= transform
            counts[m2] -= transform
            counts[p] += transform

    return answer


def distance(counts: Dict[str, int]) -> int:
    counts = copy(counts)

    while True:
        if not eliminate_opp(counts) and not condense(counts):
            break

    return sum(counts.values())

if __name__ == "__main__":
    with open("day11_input.txt") as f:
        path = f.read().strip().split(",")

    counts: Dict[str, int] = defaultdict(int)

    max_dist = float('-inf')

    for move in path:
        counts[move] += 1
        dist = distance(counts)
        if dist > max_dist:
            max_dist = dist

        print(move, dist, max_dist)
