def create_pie(pattern):
    pie = [0 for each in pattern]
    k = 0
    for q in range(2, len(pattern)):
        while k > 0 and pattern[k+1] != pattern[q]:
            k = pie[k]
        if pattern[k+1] == pattern[q]:
            k += 1
        pie[q] = k
    return pie


def kmp(text, pattern):
    text = '#' + text
    pattern = '#' + pattern
    m = len(pattern)
    pie = create_pie(pattern)
    print(f"Pattern: {pattern}")
    print(f"Pie: {pie}")
    q = 0
    for i in range(1, len(text)):
        while q > 0 and pattern[q+1] != text[i]:
            q = pie[q]
        if pattern[q+1] == text[i]:
            q += 1
        if q == m - 1:
            print(f"Match found at {i-q+1}: {text[i-q+1:i+1]}")
            q = pie[q]


kmp("abababbabbabababb", "ababb")
