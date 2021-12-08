import numpy as np
file = open("input.txt")
# file = open("test.txt")
# file = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]

def decode(num):
    one_candidate = [x for x in num if len(x) == 2]
    assert len(one_candidate) == 1
    one = one_candidate[0]
    seven_candidate = [x for x in num if len(x) == 3]
    assert len(seven_candidate) == 1
    seven = seven_candidate[0]
    four_candidate = [x for x in num if len(x) == 4]
    assert len(four_candidate) == 1
    four= four_candidate[0]
    eight_candidate = [x for x in num if len(x) == 7]
    assert len(eight_candidate) == 1
    eight = eight_candidate[0]

    fivetwothree = [x for x in num if len(list(x)) == 5]
    ninesixzero = [x for x in num if len(list(x)) == 6]
    
    three_candidate = [j for j in fivetwothree if set(list(one)).issubset(list(j))]
    assert len(three_candidate) == 1
    three = three_candidate[0]
    fivetwothree.remove(three_candidate[0])

    six_candidate = [j for j in ninesixzero if not set(list(one)).issubset(list(j))]
    assert len(six_candidate) == 1
    six = six_candidate[0]
    ninesixzero.remove(six_candidate[0])
    
    botright = set(list(one)).intersection(set(list(six)))

    five_candidate = [k for k in fivetwothree if botright.issubset(k)]
    assert len(five_candidate) == 1
    five = five_candidate[0]
    fivetwothree.remove(five)

    assert len(fivetwothree) == 1
    two = fivetwothree[0]

    nine_candidate = [o for o in ninesixzero if set(list(five)).issubset(o)]
    assert len(nine_candidate) == 1
    nine = nine_candidate[0]
    ninesixzero.remove(nine)

    assert len(ninesixzero) == 1
    zero = ninesixzero[0]

    # print(f"Zero: {zero}")
    # print(f"One: {one}")
    # print(f"Two: {two}")
    # print(f"Three: {three}")
    # print(f"Four: {four}")
    # print(f"Five: {five}")
    # print(f"Six: {six}")
    # print(f"Seven: {seven}")
    # print(f"Eight: {eight}")
    # print(f"Nine: {nine}")

    return [zero, one, two, three, four, five, six, seven, eight, nine]

total = 0

for line in file:
    digits = line.split("|")[0][:-1].split(" ")
    codes = line.split("|")[1][1:].rstrip().split(" ")
    decoded = decode(digits)
    value = []
    for code in codes:
        value += [str(idx) for idx, h in enumerate(decoded) if "".join(sorted(h)) == "".join(sorted(code))]
    
    total += int("".join(value))
print(total)
file.close()