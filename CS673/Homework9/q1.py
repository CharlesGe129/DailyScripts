def delta(text, pattern):
    # print(text)
    i = min(len(text), len(pattern)) + 1
    count = i
    while i > 1:
        i -= 1
        count -= 1
        # print(f"    text's surfix: {text[len(text)-i:]}")
        # print(f"    pattern's prefix: {pattern[:i]}")
        if text[len(text)-i:] == pattern[:i]:
            # print(f"    match: {count}")
            return count
    return 0


def DFA(pattern):
    char = set(pattern)
    rs = dict()
    for i in range(len(pattern)):
        rs[f'q{i}'] = dict()
        substr = pattern[:i]
        for out in char:
            if i < len(pattern) and out == pattern[i]:
                continue
            text = substr + out
            rs[f'q{i}'][out] = delta(text, pattern)
    return rs


pattern = "ababaab"
print(pattern)
rs = DFA(pattern)
[print(k, v) for (k, v) in rs.items()]