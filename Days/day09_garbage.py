def score_stream(s: str) -> int:
    # idea is to work from in to out
    score = 0
    depth = 1
    garbage_count = 0
    garbage = False
    negated = False



    for c in s:
        if negated:
            negated = False
            continue
        elif c == '!':
            negated = True
        elif garbage and c != '>':
            garbage_count += 1
        elif c == '<':
            garbage = True
        elif c == '>':
            garbage = False
        elif c == '{':
            score += depth
            depth += 1
        elif c == '}':
            depth -= 1

    return score, garbage_count

"""
assert score_stream("{{!}!}!<}<!>{>}}") == 3
assert score_stream("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
assert score_stream("{}") == 1
assert score_stream("{{{}}}") == 6
assert score_stream("{{},{}}") == 5
assert score_stream("{{{},{},{{}}}}") == 16
assert score_stream("{<a>,<a>,<a>,<a>}") == 1
assert score_stream("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
assert score_stream("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
assert score_stream("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3
"""

if __name__ == "__main__":
    with open("day09_input.txt") as f:
        stream = f.read().strip()
    print(score_stream(stream))

