from checksum import word_checksum, checksum


# ex: ["foo", "foo", "bar"] => "foo": 2, "bar": 1
def count_words_frequencies(words):
    d = {}
    for w in words:
        d[w] = d[w] + 1 if w in d else 1
    return d


# ex: bar, 1 => br
def drop_letter(word, i):
    w = list(word)
    del w[i]
    return ''.join(w)


# 
def commonLetters(box_ids, drop_index):
    box_id_count = count_words_frequencies([
        drop_letter(box_id, drop_index)
        for box_id in box_ids
    ])

    repeating_box_ids = [
        box_id
        for box_id, count in box_id_count.items()
        if count > 1
    ]

    if len(repeating_box_ids) > 0:
        print("the common letters are %s" % repeating_box_ids[0])
    elif drop_index > 0:
        return commonLetters(box_ids, drop_index - 1)
    else:
        return None


box_ids = open("box_ids.txt", "r").read().split()

commonLetters(box_ids, min([
    len(box_id) for box_id in box_ids
]) - 1)
