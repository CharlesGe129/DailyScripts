name = ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
name_to_index = {}
Adj = []
rs = {}
number = {}
end = 0


def prepare_map():
    for i in range(len(name)):
        name_to_index[name[i]] = i
        rs[i] = 0


def reverse_adj(adj):
    rs = [[] for i in range(len(adj))]
    for i in range(len(adj)):
        for each in adj[i]:
            rs[each].append(i)
    return rs


def prepare_adj():
    global Adj
    for i in range(len(name)):
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
    Adj = reverse_adj(Adj)
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
    global number
    num = 0
    print(f"Current node: {node}")
    for v in Adj[node]:
        print(f"    Adj node of {node}: {v}")
        if f"{v}{node}" in number:
            number[f"{v}{node}"] += 1
        else:
            number[f"{v}{node}"] = 1
        if rs[v] == 0:
            print(f"        Node {v} is empty")
            search(v)
        print(f"        Node {v} = {rs[v]}")
        num += rs[v]
    print(f"Finish node {node}, num = {num}")
    rs[node] = num


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
    global number
    prepare_map()
    prepare_adj()
    show_matrix()
    end = name_to_index['v']

    rs[name_to_index['p']] = 1
    search(name_to_index['v'])

    #rs = process_name(rs)
    [print(f"{i}: {rs[i]}") for i in range(len(name))]
    print(number)


do()