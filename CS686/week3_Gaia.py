import random


class Hex:
    def __init__(self, name):
        self.name = name
        self.adj = list()


class Tile:
    def __init__(self):
        self.hexes = [Hex(i) for i in range(19)]
        self.adj = list()
        self.cal_hex_adj()
        self.cal_hex_reverse_adj()

    def cal_hex_adj(self):
        self.hexes[0].adj = self.cal_hex_adj_by_type(0, 0)
        self.hexes[1].adj = self.cal_hex_adj_by_type(1, 1)
        self.hexes[2].adj = self.cal_hex_adj_by_type(2, 2)
        self.hexes[3].adj = self.cal_hex_adj_by_type(3, 3)
        self.hexes[4].adj = self.cal_hex_adj_by_type(4, 1)
        self.hexes[5].adj = self.cal_hex_adj_by_type(5, 4)
        self.hexes[6].adj = self.cal_hex_adj_by_type(6, 1)
        self.hexes[7].adj = self.cal_hex_adj_by_type(7, 2)
        self.hexes[8].adj = self.cal_hex_adj_by_type(8, 3)
        self.hexes[9].adj = self.cal_hex_adj_by_type(9, 1)
        self.hexes[10].adj = self.cal_hex_adj_by_type(10, 4)
        self.hexes[11].adj = self.cal_hex_adj_by_type(11, 1)
        self.hexes[12].adj = self.cal_hex_adj_by_type(12, 2)
        self.hexes[13].adj = self.cal_hex_adj_by_type(13, 3)
        self.hexes[14].adj = self.cal_hex_adj_by_type(14, 1)
        self.hexes[15].adj = self.cal_hex_adj_by_type(15, 4)
        self.hexes[16].adj = self.cal_hex_adj_by_type(16, 0)
        self.hexes[17].adj = [self.hexes[18]]

    # 5 types: 0=[1, 2], 1=[2, 3, 4], 2=[4, 5], 3=[4, 6], 5=[7]
    def cal_hex_adj_by_type(self, num, type_no):
        adj_lists = {0: [num+1, num+2],
                1: [num+1, num+2, num+3],
                2: [num+2, num+3],
                3: [num+1, num+3],
                4: [num+2]}[type_no]
        return [self.hexes[each] for each in adj_lists]

    def cal_hex_reverse_adj(self):
        for i in range(17, -1, -1):
            for each in self.hexes[i].adj:
                each.adj = [self.hexes[i]] + each.adj
        for i in range(19):
            print(f"{i}: {[each.name for each in self.hexes[i].adj]}")

    def print_hex(self):
        print("   00")
        print(" 01  02")
        print("03 04 05")
        print(" 06  07")
        print("08 09 10")
        print(" 11  12")
        print("13 14 15")
        print(" 16  17")
        print("   18")


class Board:
    def __init__(self, tiles):
        self.tiles = tiles


class Game:
    def __init__(self):
        self.board = Board(None)
        self.tile = None
        self.rs_distance = dict()
        self.flag_distance = list()

    def create_tile(self):
        self.tile = Tile()

    def distance(self, h1, h2):
        self.rs_distance = dict()
        self.flag_distance = [False for i in range(19)]
        self.traverse(h1, h2, str(h1.name), 0)
        distance = sorted(self.rs_distance.keys())[0]
        print(f"Distance between hex[{h1.name}] and hex[{h2.name}] is {distance}")
        [print(each) for each in self.rs_distance[distance]]

    def traverse(self, start, end, path, count):
        # print(f"Start = {start}, end = {end}, path = {path}, count = {count}")
        if start == end:
            # print(f"Match: {path}")
            if count in self.rs_distance:
                self.rs_distance[count].append(path)
            else:
                self.rs_distance[count] = [path]
        elif not self.flag_distance[start.name]:
            self.flag_distance[start.name] = True
            [self.traverse(each, end, f"{path}-{each.name}", count + 1) for each in start.adj]
            self.flag_distance[start.name] = False

a = Game()
a.create_tile()
a.tile.print_hex()
a.distance(a.tile.hexes[random.randint(0, 18)], a.tile.hexes[random.randint(0, 18)])
a.distance(a.tile.hexes[15], a.tile.hexes[8])
