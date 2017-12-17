def is_valid(passphrase: str) -> bool:
    sections = passphrase.split()
    amount = len(sections)
    amount_unique = len(set(sections))
    if amount == amount_unique:
        return True
    else:
        return False

assert is_valid("aa bb cc dd ee")
assert not is_valid("aa bb cc dd aa")
assert is_valid("aa bb cc dd aaa")

def is_valid2(passphrase: str) -> bool:
    sections = passphrase.split()
    amount_word = len(sections)
    non_anagrams = {tuple(sorted(word)) for word in sections}
    amount_non_anagrams = len(non_anagrams)
    return amount_word == amount_non_anagrams




if __name__ == "__main__":
    with open("day04_input.txt", "r") as f:
        row = [line.strip() for line in f]
    valid_pass = [pp for pp in row if is_valid(pp)]
    print(len(valid_pass))


    valid_pass2 = [pp for pp in row if is_valid2(pp)]
    print(len(valid_pass2))
