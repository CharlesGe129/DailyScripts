import random


class Hex:
    def __init__(self, name, tile_name):
        self.name = name
        self.adj = list()
        self.tile_name = tile_name
        self.full_name = f"{tile_name}_{name}"

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


class Tile:
    def __init__(self, name):
        self.name = name
        self.hexes = [Hex(i, name) for i in range(19)]
        self.adj = dict()
        self.cal_hex_adj()
        self.cal_hex_reverse_adj()

    def cal_hex_adj(self):
        self.hexes[0].adj = self.cal_hex_adj_by_type(0, 0)
        self.hexes[1].adj = self.cal_hex_adj_by_type(1, 1)
        self.hexes[2].adj = self.cal_hex_adj_by_type(2, 1)
        self.hexes[3].adj = self.cal_hex_adj_by_type(3, 2)
        self.hexes[4].adj = self.cal_hex_adj_by_type(4, 1)
        self.hexes[5].adj = self.cal_hex_adj_by_type(5, 3)
        self.hexes[6].adj = self.cal_hex_adj_by_type(6, 1)
        self.hexes[7].adj = self.cal_hex_adj_by_type(7, 1)
        self.hexes[8].adj = self.cal_hex_adj_by_type(8, 2)
        self.hexes[9].adj = self.cal_hex_adj_by_type(9, 1)
        self.hexes[10].adj = self.cal_hex_adj_by_type(10, 3)
        self.hexes[11].adj = self.cal_hex_adj_by_type(11, 1)
        self.hexes[12].adj = self.cal_hex_adj_by_type(12, 1)
        self.hexes[13].adj = [self.hexes[16]]
        self.hexes[14].adj = [self.hexes[16], self.hexes[17], self.hexes[18]]
        self.hexes[15].adj = [self.hexes[17]]
        self.hexes[16].adj = [self.hexes[18]]
        self.hexes[17].adj = [self.hexes[18]]

    # 5 types: 0=[1, 2], 1=[2, 3, 4], 2=[4, 5], 3=[4, 6], 5=[7]
    def cal_hex_adj_by_type(self, num, type_no):
        adj_lists = {0: [num+1, num+2],
                     1: [num+2, num+3, num+5],
                     2: [num+3, num+5],
                     3: [num+2, num+5]}[type_no]
        return [self.hexes[each] for each in adj_lists]

    def cal_hex_reverse_adj(self):
        for i in range(17, -1, -1):
            for each in self.hexes[i].adj:
                each.adj = [self.hexes[i]] + each.adj

    def print_hex(self):
        for i in range(19):
            print(f"{i}: {[each.full_name for each in self.hexes[i].adj]}")


class Board:
    def __init__(self):
        self.tiles = list()
        self.rs_distance = dict()
        self.flag_distance = list(list())

    def create_tile(self):
        self.tiles.append(Tile(0))
        self.tiles.append(Tile(1))
        self.link_tiles(self.tiles[0], self.tiles[1], 0)

    def link_tiles(self, t1, t2, type_no):
        links = self.get_link_by_direction(type_no)
        if type_no == 0:
            # Left-Right
            t1.adj[t2] = 'right'
            t2.adj[t1] = 'left'
            [[self.add_link(t1.hexes[h1_no], t2.hexes[h2_no]) for h2_no in h2_list]
             for h1_no, h2_list in links.items()]

    @staticmethod
    def add_link(h1, h2):
        h1.adj.append(h2)
        h2.adj.append(h1)

    @staticmethod
    def get_link_by_direction(type_no):
        return {0: {5: [3], 10: [3, 8], 15: [8, 13]}}[type_no]

    def path(self, t1, t2):
        self.rs_distance = dict()
        self.flag_distance = [False for i in range(len(self.tiles))]
        self.traverse(t1, t2, str(t1.name), 0)
        distance = sorted(self.rs_distance.keys())[0]
        # print(f"Distance between tile[{t1.name}] and hex[{t2.name}] is {distance}")
        # [print(each) for each in self.rs_distance[distance]]
        return self.rs_distance[distance]

    def traverse(self, start, end, path, count):
        # print(f"Start = {start.name}, end = {end.name}, path = {path}, count = {count}")
        if start == end:
            # print(f"Match: {path}")
            if count in self.rs_distance:
                self.rs_distance[count].append(path)
            else:
                self.rs_distance[count] = [path]
        elif not self.flag_distance[start.name]:
            self.flag_distance[start.name] = True
            [self.traverse(each, end, f"{path} -> {each.name}", count + 1) for each in start.adj]
            self.flag_distance[start.name] = False

    def cal_inside_path(self, t1, t2):
        if t1.adj[t2] == 'right':
            return [[5, 3], [10, 3], [10, 8], [15, 8], [15, 13]]


class Game:
    def __init__(self):
        self.board = Board()
        self.rs_distance = dict()
        self.flag_distance = list()

    def create_board(self):
        self.board.create_tile()

    def print_board(self):
        Hex(1, 1).print_hex()
        for tile in self.board.tiles:
            print(f"==========This is tile {tile.name}==========")
            tile.print_hex()

    def distance(self, h1, h2):
        tile_path = self.board.path(self.board.tiles[h1.tile_name], self.board.tiles[h2.tile_name])
        tile_path = [path.split(' -> ') for path in tile_path]
        rs_distances = dict()
        for path in tile_path:
            for i in range(len(path)-1):
                # each two adj tiles
                t1 = self.board.tiles[int(path[0])]
                t2 = self.board.tiles[int(path[1])]
                hex_edge_lists = self.board.cal_inside_path(t1, t2)
                for edge_pair in hex_edge_lists:
                    hex_edge_t1 = t1.hexes[edge_pair[0]]
                    hex_edge_t2 = t2.hexes[edge_pair[1]]
                    print(f"find inside path from {h1.full_name} to {h2.full_name} by {hex_edge_t1.full_name}, {hex_edge_t2.full_name}")
                    path_in_t1 = self.path_inside(h1, hex_edge_t1)
                    path_in_t2 = self.path_inside(hex_edge_t2, h2)
                    paths = self.link_two_path(path_in_t1, path_in_t2)
                    for each_path in paths:
                        count = each_path.count('->')
                        print(f"Found a path from {h1.full_name} to {h2.full_name}, count = {count}: {each_path}")
                        if count in rs_distances:
                            rs_distances[count].append(each_path)
                        else:
                            rs_distances[count] = [each_path]
        print("========== Result ==========")
        [print(each)for each in rs_distances[sorted(rs_distances.keys())[0]]]
        return

    @staticmethod
    def link_two_path(path1, path2):
        path = list()
        for p1 in path1:
            for p2 in path2:
                path.append(f"{p1} -> {p2}")
        return path

    def path_inside(self, h1, h2):
        self.rs_distance = dict()
        self.flag_distance = [False for i in range(19)]
        self.traverse(h1, h2, f"{h1.full_name}", 0)
        distance = sorted(self.rs_distance.keys())[0]
        # print(f"Distance between hex[{h1.full_name}] and hex[{h2.full_name}] is {distance}")
        # [print(each) for each in self.rs_distance[distance]]
        return self.rs_distance[distance]

    def traverse(self, start, end, path, count):
        if not start.tile_name == end.tile_name:
            return
        # print(f"Start = {start.full_name}, end = {end.full_name}, h1={start}, h2={end}, path = {path}, count = {count}")
        if start == end:
            # print(f"Match: {path}")
            if count in self.rs_distance:
                self.rs_distance[count].append(path)
            else:
                self.rs_distance[count] = [path]
        elif not self.flag_distance[start.name]:
            self.flag_distance[start.name] = True
            [self.traverse(each, end, f"{path} -> {each.full_name}", count + 1) for each in start.adj]
            self.flag_distance[start.name] = False

a = Game()
a.create_board()
a.print_board()
# a.distance(a.board.tiles[0].hexes[11], a.board.tiles[1].hexes[7])
a.distance(a.board.tiles[0].hexes[random.randint(0, 18)], a.board.tiles[1].hexes[random.randint(0, 18)])
