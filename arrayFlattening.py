def array_flatten(content, rs):
    [traverse(each, rs) for each in content]


def traverse(content, rs):
    if isinstance(content, str):
        rs.append(content)
    elif isinstance(content, list):
        array_flatten(content, rs)


test = ["aa", "bb", ["cc", "dd", ["ee", "ff"]]]
rs = list()
array_flatten(test, rs)
print(rs)