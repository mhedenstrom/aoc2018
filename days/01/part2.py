from changes import changes
from itertools import accumulate, cycle

seen = set()
print(next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f)))

# test1 = [1, -1]
# test2 = [3, 3, 4, -2, -4]
# test3 = [-6, 3, 8, 5, -6]
# test4 = [7, 7, -2, -7, -4]
# test5 = [1, -2, 3, 1]


# +1, -1 first reaches 0 twice.
# +3, +3, +4, -2, -4 first reaches 10 twice.
# -6, +3, +8, +5, -6 first reaches 5 twice.
# +7, +7, -2, -7, -4 first reaches 14 twice.

# changes = test4

# from itertools import cycle

# f = 0
# seen = []
# pool = cycle(changes)
# while f not in seen:
#     if len(seen) % 1000 == 0:
#         print(len(seen))
#     seen.append(0)
#     n = next(pool)
#     f += n
# print(f)

# netChange = sum(changes)

# print("%d frequency changes" % len(changes))

# print("net change %d" % netChange)
# print("---")


# frequencies = changes[:]

# xs = [
#     frequencies[max(0,i-1):i+1] # % netChange
#     for i in range(0, len(changes))
# ]


# (i, l)  <= index of sublist, length of sublist (sum = 0)
# sublists = [
#     (i, l)
#     for l in range(1,len(changes)+1)
#     for i in range(len(changes))
#     # if sum((changes[i:] + changes[:i])[:l]) == 0
# ]

# total = sum(changes)

# sublists = [
#     (i,j, sum(changes[i:] + changes[:j]))
#     for i in range(len(changes))
#     for j in range(len(changes))
#     if sum(changes[i:] + changes[:j]) % netChange == 0 and sum(changes[i:] + changes[:j]) <= 0
# ]

# print(sublists)

# sublists = sorted(sublists, key = lambda t: -t[2])



# (i,j,s) = sublists[0]
# loops =  int(abs(s) / netChange)
# if i > j:
#     loops += 1

# res = netChange * loops + sum(changes[:2])

# print("first frequency seen twice is %d" % res)

# cyclic list
#   sublist
#     sum = 0 ?

"""
3,3,4,-2,-4


l=5:
3,3,4,-2,-4  => 4
  3,4,-2,-4,3 => 4
    4,-2,-4,3,3 => 4
      -2,-4,3,3,4 => 4
         -4,3,3,4,-2 => 4

l=4:
3,3,4,-2 => 8, i=0
  3,4,-2,-4 => 1, i=1
    4,-2,-4,3 => 1, i=2
      -2,-4,3,3 => 0, i=3
         -4,3,3,4 => 6, i=4

l=3:
3,3,4 => 10
  3,4,-2 => 5
    4,-2,-4 => -2
      -2,-4,3 => -3
         -4,3,3 => 2

l=2:
3,3 => 6
  3,4 => 7
    4,-2 => 2
      -2,-4 => -6 
         -4,3 => -1

l=1:
3, => 3
  3, => 3
    4, => 4
      -2, => -2
         -4 => -4






3,3,4,-2,-4 => [-2, -4, 3, 3] sum = 0
# 3, 3, 4, -2, -4
1:  3 6 10 8 4
2: 
                   14
 
                     12

     10     |   10
            |
        8   |           8
            | 7
   6        |
            |
          4 |
 3          |
 """


# 76496 too low