from checksum import checksum

boxIds = open("box_ids.txt", "r").read().split()

print("the checksum is %d" % checksum(boxIds))
