# format: [ header [subtree] metadata ]
data = open("data.txt", "r").read()
# data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
data = [
    int(s)
    for s in data.split(' ')
]


def parse(data):

    # header
    (child_count, metadata_count) = data[:2]
    data = data[2:]

    # recursively get children
    children = []
    for c in range(child_count):
        (child, data) = parse(data)
        children.append(child)

    # return this node and remaining data
    (metadata, data) = data[:metadata_count], data[metadata_count:]
    return (
        (metadata, children), # node
        data
    )


def get_metadata_sum(node):
    (metadata, children) = node

    return sum(metadata) + sum([
        get_metadata_sum(child)
        for child in children
    ])


def get_node_value(node):
    (meta, children) = node

    if (len(children) == 0):
        return sum(meta)

    child_indexes = [
        i - 1
        for i in meta
        if i > 0 and i - 1 < len(children)
    ]

    cache = {}
    for k in list(set(child_indexes)):
        cache[k] = get_node_value(children[k])

    return sum([
        cache[k]
        for k in child_indexes
    ])


# Parse input data
(root_node, remainder) = parse(data)

# Part 1:
print("The sum of all metadata entries is %d" % get_metadata_sum(root_node))

# Part 2:
print("The value of the root node is %d" % get_node_value(root_node))
