def clean_o(line):
    length = len(line)
    line_cleaned = ''
    i = 0
    while i < length:
        letter = line[i]
        if letter == 'o':
            if i + 1 < length and line[i+1] == 'o':
                i += 1
            else:
                line_cleaned = line_cleaned[:-1]
        else:
            line_cleaned += letter
        i += 1
        # print(f"{i}, {letter}, {line_cleaned}")
    return line_cleaned


def reveal_keyboard_input():
    line_cleaned = clean_o(input())
    result = ''
    print(line_cleaned)
    for letter in line_cleaned:
        if letter == 'i':
            result = result[:-1]
        else:
            result += letter
    print(result)


reveal_keyboard_input()


def reveal_keyboard_input():
    line = input()
    rs = ''
    rs_last = ''
    for letter in line:
        if letter == 'i':
            rs_last = rs
            rs = rs[:-1]
        elif letter == 'o':
            temp = rs
            rs = rs_last
            rs_last = temp
        else:
            rs_last = rs
            rs += letter
    print(rs)

reveal_keyboard_input()
