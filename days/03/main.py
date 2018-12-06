from claims import claims_by_inch, inches


overlapped_inches = [
    inch, claims in claims_by_inch(inches).values()
    if len(claims) > 1
]
print("part 1: %d inches are within one or more claims" % len(overlapped_inches))



# ex #123 @ 4,5 : 2,2 => (4,5), (4,6) ... (6,7)


# def claim_contains(claim, x, y):
#     (ox, oy, width, height) = tuple(claim[1:])
#     return ox <= x and x < ox + width and oy <= y and y < oy + height



# claim_contents = [
#     contents(c) for c in claims
# ]

# counts = {}
# for claim_content in claim_contents:
#     for inch in claim_content:
#         (claim_id, x, y) = inch
#         counts[(x,y)] = [claim_id] + counts[(x,y)] if (x,y) in counts else [claim_id]
        # counts[(x,y)] = counts[(x,y)] + 1 if (x,y) in counts else 1

# non_overlapping = [
#     v[0]
#     for k, v in counts.items()
#     if len(v) == 1
# ]




# ex : 1,2,3 
# claim_ids = set([c[0] for c in claims])



# claim_ids.remove(2)



# for k, claims in counts.items():
#     if len(claims) > 1:
#         for claim in claims:
#             if claim in claim_ids:
#                 claim_ids.remove(claim)

# print(claim_ids)

# # print(len([len(xs) for xs in counts.values() if len(xs) == 1]))


# # print(len([k for k in counts if counts[k] > 1]))
