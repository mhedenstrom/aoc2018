from math import ceil
from string import ascii_lowercase


polymer = open("polymer.txt", "r").read()


"""
True iff a != b, but same letter (equal lowercase versions)
"""
def are_opposite_units(a, b):
    return a.lower() == b.lower() and a != b


"""
react a/A unit pairs, recursively by dividing list into chunks (divide and conquer).
base case:
- single unit (does not react) => return unchanged
- two-unit string (might react) => return empty string if reacts, otherwise unchanged
- longer strings... =>
    1. split into two (almost) equal parts and recurse
    2. re-join results
    3. joining ends may react, in which case leave them out, otherwise return joined string
"""
def react_binary(xs):
    # some base cases for very short strings
    if len(xs) < 2:
        return xs
    elif len(xs) == 2:
        [a, b] = xs
        if are_opposite_units(a, b):
            return ""
        else:
            return xs
    
    # split longer strings into 2 parts and call recursively
    k = int(len(xs)/2)
    res1 = react_binary(xs[:k])
    res2 = react_binary(xs[k:])

    if (len(res1) == 0 or len(res2) == 0):
        # either result is empty; no reaction
        return res1 + res2

    if are_opposite_units(res1[-1], res2[0]):
        # joining end units react; leave them out
        return res1[:-1] + res2[1:]
    
    # nothing reacts, just return
    return res1 + res2


"""
Multi-pass react-calling function.
Will make polymer react until it doesn't get any shorter.
"""
def react_all(xs):
    length = len(xs)

    while True:
        xs = react_binary(xs)
        if len(xs) == length:
            # did not get any shorter
            return xs
        
        length = len(xs)


"""
PART 1:
Make the polymer react fully and see how short it gets.
"""
fully_reacted_polymer = react_all(polymer)
print("The resulting polymer %s contains %d units" % (fully_reacted_polymer, len(fully_reacted_polymer)))


"""
PART2:
For every removed letter, see how short the modified polymer gets.
"""
letters = list(ascii_lowercase)[:]
lengths = []
for letter in letters:
    shortPolymer = polymer.replace(letter, "").replace(letter.upper(), "")
    lengths.append(len(react_all(shortPolymer)))
print("The shortest polymer we can get by removing a single base is of length %d" % min(lengths))

# 10658 too high dammit
# c...