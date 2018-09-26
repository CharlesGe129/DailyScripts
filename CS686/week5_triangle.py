class Node:
    def __init__(self, name, summation, left, right, next_node):
        self.name = name
        self.summation = summation
        self.left = left
        self.right = right
        self.next_node = next_node


class Solution:
    def __init__(self):
        self.cur_level = list()

    @staticmethod
    def get_data():
        with open('week5_data.txt', 'r') as f:
            return f.read()

    def cal_triangle_expensive_path(self):
        data = self.get_data().split('\n')
        [self.scan_next_level(data[i].strip().split(" ")) for i in range(len(data)-1, -1, -1)]
        self.print_result()

    def scan_next_level(self, next_level):
        cur_weigh = self.cur_level
        next_level = [int(each) for each in next_level]
        if not cur_weigh:
            next_weigh = [Node(number, number, None, None, None) for number in next_level]
        else:
            next_weigh = [Node(next_level[i],
                               next_level[i] + max(cur_weigh[i].summation, cur_weigh[i+1].summation),
                               cur_weigh[i],
                               cur_weigh[i+1],
                               cur_weigh[i] if cur_weigh[i].summation > cur_weigh[i+1].summation else cur_weigh[i+1])
                          for i in range(len(next_level))]
        # print("====")
        # [print(f"cur={each.name}, sum={each.summation}; ", end='') for each in cur_weigh]
        # print()
        # [print(f"cur={each.name}, sum={each.summation}; ", end='') for each in next_weigh]
        # print()
        self.cur_level = next_weigh

    def print_result(self):
        node = self.cur_level[0]
        print(node.name, end='')
        while node.next_node:
            node = node.next_node
            print(f"-{node.name}", end='')
        print()


Solution().cal_triangle_expensive_path()
# print(sum([int(each) for each in path.split('-')]))