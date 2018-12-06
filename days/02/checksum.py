from functools import reduce

# ex: aab => {a: 2, b: 1}
def letter_frequencies(word):
    frequencies = {}
    for letter in list(word):
        frequencies[letter] = frequencies[letter] + 1 if letter in frequencies else 1
    return frequencies

# words containing exactly `count` of any letter
def containing(words, count):
    return list(filter(
        lambda x: count in letter_frequencies(x).values(),
        words))

# ex: "aabccc" = "cccbaa" => 2*1*3 = 6
def word_checksum(word):
    frequencies = [v for k,v in letter_frequencies(word).items()]
    product = reduce(lambda x, y: x * y, frequencies, 1)
    return product



def checksum(word):
    return len(containing(word, 2)) * len(containing(word, 3))
