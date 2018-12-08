
# format: [ header [subtree] metadata ]
data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
data = open("data.txt", "r").read()
tree = [
    int(s)
    for s in data.split(' ')
]


# traverse the tree and collect all metadata
def get_metadata(node):
    (metadata, children) = node

    for child in children:
        metadata.extend(get_metadata(child))

    return metadata


# parse data into a tree: (node, children)
def get_node(nodes):

    # header
    (child_count, meta_count) = nodes[:2]
    nodes = nodes[2:]

    # recursively get children
    children = []
    for c in range(child_count):
        (one_child, nodes) = get_node(nodes)
        children.append(one_child)

    # return this node and remaining data
    (metadata, remainder) = nodes[:meta_count], nodes[meta_count:]
    return (
        (metadata, children), # node
        remainder
    )

# parse tree
(root_node, remainder) = get_node(tree)
if len(remainder) > 0:
    # should not remain anything from the original data
    print("error")

# print(root_node)
print(sum(get_metadata(root_node)))