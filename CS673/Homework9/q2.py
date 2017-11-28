def charles_algorithm(text, pattern):
    start = 0
    for p in sub_str(pattern):
        flag = False
        while start + len(p) <= len(text):
            t = text[start:start+len(p)]
            if compare(t, p):
                flag = True
                break
            else:
                start += 1
        if not flag:
            return False
    return True


def sub_str(pattern):
    result = []
    start = 0
    while start < len(pattern):
        end = start + 1
        while end < len(pattern) and pattern[end] != '%':
            end += 1
        result.append(pattern[start:end])
        start = end + 1
    return result


def compare(origin, new):
    if len(origin) != len(new):
        return False
    for i in range(len(origin)):
        if origin[i] != new[i]:
            return False
    return True


print(charles_algorithm("abarogdracodeabaoeaoecaoe", "ab%ba%eaoe%caoe"))
