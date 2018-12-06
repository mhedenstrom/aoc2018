# from math import abs

test_input = [
    "1, 1",
    "1, 6",
    "8, 3",
    "3, 4",
    "5, 5",
    "8, 9"
]

# all coordinates in the grid
coords = [
    tuple([int(x.strip()) for x in c.split(",")])
    for c in open("grid.txt", "r").read().split('\n')
    # for c in test_input
]

xs = [x for (x,y) in coords]
ys = [y for (x,y) in coords]
x_min, x_max = min(xs), max(xs)
y_min, y_max = min(ys), max(ys)


grid = [
    (x,y)
    for y in range(y_min, y_max)
    for x in range(x_min, x_max)
]


inner_points = [
    (x,y)
    for (x,y) in coords
    if x > x_min and x < x_max and y > y_min and y < y_max
]


def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


"""
List of one or more points equally close to (x,y).
"""
def closest_points(x, y):
    distances = [
        ((x2, y2), manhattan_distance(x, y, x2, y2))
        for (x2, y2) in coords
    ]

    min_distance = min([d[1] for d in distances])

    return [
        point
        for (point, distance) in distances
        if distance == min_distance
    ]


"""
A single closest point, or None if there is a tie.
"""
def closest_point(x, y):
    ps = closest_points(x, y)
    return ps[0] if len(ps) == 1 else None


"""
Mapping from location to nearest point.
"""
def closest_region_area(ps):
    closest = [
        closest_point(x, y)
        for (x, y) in grid
    ]

    count = {}
    for p in [c for c in closest if c is not None]:
        count[p] = count[p] + 1 if p in count else 1

    return max(count.values())


def region_any_point_within_distance(d):
    return len([
        (x, y)
        for x, y in grid
        if sum([manhattan_distance(x, y, x2, y2) for (x2,y2) in coords]) < d
    ])


# Part 1
print("The size of the largest area is %d" %  closest_region_area(grid))

# Part 2
max_distance = 10000
print(
    "Size of region with total distance to all points < %d is %d" %
    (max_distance, region_any_point_within_distance(max_distance)))
