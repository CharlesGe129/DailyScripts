name = ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
name_to_index = {}
Adj = []
rs = {}
end = 0


def prepare_map():
    for i in range(len(name)):
        name_to_index[name[i]] = i
        rs[i] = 0


def prepare_adj():
    for i in range(14):
        Adj.append([])
    Adj[0] = ['q', 'r', 'x']
    Adj[1] = ['o', 'q', 'u']
    Adj[2] = ['r', 's', 'v']
    Adj[3] = ['o', 's', 'z']
    Adj[4] = ['t']
    Adj[5] = ['u', 'y']
    Adj[6] = ['r']
    Adj[7] = []
    Adj[8] = ['t']
    Adj[9] = ['w', 'x']
    Adj[10] = ['z']
    Adj[11] = []
    Adj[12] = ['v']
    Adj[13] = []
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


def search_path(node):
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


def search(node):
    global rs
    nodes = []
    print(f"Current node: {node}")
    for v in Adj[node]:
        print(f"        Adj: {v}")
        print(f"        rs[{v}] += {rs[node]}")
        print(rs)
        rs[v] += rs[node]
        nodes.append(v)
    if node != end:
        rs[node] = 0
    print(f"Ready to recursion: node={nodes}")
    for each in nodes:
        search(each)


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

    rs[name_to_index['p']] = 1
    end = name_to_index['v']
    search(name_to_index['p'])

    #rs = process_name(rs)
    [print(f"{name[i]}: {rs[i]}") for i in range(len(name))]


do()