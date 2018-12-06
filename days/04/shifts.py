from records import sorted_records, action, BEGINS_SHIFT

def shift_bounds(records):
    idxs = [
        i
        for i, r in enumerate(sorted_records)
        if action(r) == BEGINS_SHIFT
    ]
    idxs.append(len(records) + 1)

    return list(zip(
        idxs[:-1],
        idxs[1:]
    ))


shifts = [
    sorted_records[lo:hi]
    for (lo, hi) in shift_bounds(sorted_records)
]
