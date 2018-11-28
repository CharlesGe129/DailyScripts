import queue


class KnightOnPhonePanel:
    def __init__(self):
        self.panel = dict()
        self.queue = queue.Queue()
        self.mount_panel()

    def mount_panel(self):
        self.panel[0] = [4, 6]
        self.panel[1] = [6, 8]
        self.panel[2] = [7, 9]
        self.panel[3] = [4, 8]
        self.panel[4] = [3, 9, 0]
        self.panel[5] = []
        self.panel[6] = [1, 7, 0]
        self.panel[7] = [2, 6]
        self.panel[8] = [1, 3]
        self.panel[9] = [2, 4]

    def biggest_distinct_numbers(self, start, hop):
        self.queue.put({'node': start, 'path': str(start)})
        self.bfs(hop)

    def bfs(self, hop):
        last_hop_nodes = []
        while not self.queue.empty():
            last_hop_nodes.append(self.queue.get())
        for each in last_hop_nodes:
            node = each['node']
            path = each['path']
            [self.queue.put({'node': next_node, 'path': f"{path}->{next_node}"}) for next_node in self.panel[node]]
        if hop == 1:
            self.print_result()
        else:
            self.bfs(hop-1)

    def print_result(self):
        biggest_distinct = -1
        while not self.queue.empty():
            path = self.queue.get()['path']
            biggest_distinct = max(len(set(path.split('->'))), biggest_distinct)
            print(path)
        print(f"biggest distinct number: {biggest_distinct}")

    def test(self, num, step):
        moves = self.panel[num]
        if step == 1:
            return len(moves)
        count = 0
        for move in moves:
            count = count + self.test(move, step-1)
        return count

KnightOnPhonePanel().biggest_distinct_numbers(1, 5)
print(KnightOnPhonePanel().test(1, 5))
