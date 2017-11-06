name = ['a', 'b', 'c', 'd']
name_to_index = {}
Adj = []
rs = {}
end = 0


def prepare_map():
    for i in range(len(name)):
        name_to_index[name[i]] = i
        rs[i] = [0]


def prepare_adj():
    for i in range(len(name)):
        Adj.append([])
    Adj[0] = ['b', 'c']
    Adj[1] = ['c']
    Adj[2] = ['d']
    Adj[3] = []
    for i in range(len(Adj)):
        a = list()
        for node in Adj[i]:
            a.append(name_to_index[node])
        Adj[i] = a
    print(Adj)


def show_matrix():
    num = len(Adj)
    m = []
    for i in range(num):
        a = []
        for j in range(num):
            a.append(0)
        m.append(a)
    for i in range(num):
        for each in Adj[i]:
            m[i][each] = 1
    print("  ", end='')
    [print(each + ' ', end='') for each in name]
    print()
    for i in range(len(m)):
        row = m[i]
        print(name[i] + " ", end='')
        [print(f"{each} ", end='') for each in row]
        print()


def search(node):
    global rs
    nodes = []
    print(f"Current node: {node}")
    for path in rs[node]:
        print(f"    Path: {path}")
        for v in Adj[node]:
            print(f"        Adj: {v}")
            rs[v].append(path + [v])
            print(f"        rs[{v}].append({path+[v]})")
            nodes.append(v)
    if node != end:
        rs[node] = []
    print(f"Ready to recursion: node={nodes}")
    for each in nodes:
        search(each)


def search_num(node):
    global rs
    nodes = []
    print(f"Current node: {node}")
    for v in Adj[node]:
        print(f"        Adj: {v}")
        print(f"        rs[{v}] += {rs[node]}")
        print(rs)
        rs[v][0] += rs[node][0]
        nodes.append(v)
    if node != end:
        rs[node][0] = 0
    print(f"Ready to recursion: node={nodes}")
    for each in nodes:
        search_num(each)


def process_name(rs):
    result = []
    print(rs)
    for key in rs:
        node = rs[key]
        new_node = []
        print(node)
        for path in node:
            a = []
            for each in path:
                a.append(name[each])
            new_node.append(a)
        result.append(new_node)
    return result


def do():
    global end
    global rs
    prepare_map()
    prepare_adj()
    show_matrix()
    end = name_to_index['d']

    rs[name_to_index['a']] = [1]
    search_num(name_to_index['a'])

    #rs = process_name(rs)
    [print(f"{i}: {rs[i]}") for i in range(len(name))]


do()