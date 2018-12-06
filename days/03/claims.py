import re

def to_inches(cid, x, y, width, height):
    return [
        (cid, x + dx, y + dy)
        for dx in range(width)
        for dy in range(height)
    ]


def parse_claim(line):
    return map(int, [
        i 
        for i in re.compile("[^\\d]+").split(line) 
        if len(i) > 0
    ])


def claims_by_inch(inches):
    count = {}
    for (cid, x, y) in inches:
        count[(x,y)] = [cid] + count[(x,y)] if (x,y) in count else [cid]
    return count


# flat list of (cid, x, y)
inches = [
    inch
    for inch in to_inches(cid, x, y, width, height)
    for (cid, x, y, width, height) in parse_claim(line)
    for line in open("claims.txt", "r").read().split('\n')
]
