rs = []
v = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 6, 6, 6, 6, 6, 5, 4]
rs.append(v)
v = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 0, 5, 5, 5, 5, 4, 3]
rs.append(v)
v = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 0, 0, 4, 4, 4, 4, 3, 3]
rs.append(v)
v = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 3]
rs.append(v)
v = [1, 1, 1, 1, 1, 1, 2, 2, 2, 0, 3, 0, 0, 0, 2, 2, 2, 3, 3, 3]
rs.append(v)
v = [1, 1, 1, 1, 1, 1, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2]
rs.append(v)
v = [1, 1, 1, 1, 1, 1, 0, 2, 2, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2]
rs.append(v)
v = [1, 1, 1, 1, 1, 1, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2]
rs.append(v)
v = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
rs.append(v)
for i in range(20):
    if i < 9:
        print(f'v{i+1}:   ', end='')
    else:
        print(f'v{i+1}:  ', end='')
    for j in range(len(rs)):
        print(str(rs[j][i]) + "  ", end='')
    print()
    print()
