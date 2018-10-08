import json


class Graph:
    def __init__(self):
        self.vertices = dict()
        self.paths = dict()

    def mount_graph(self, raw_route):
        for entry in raw_route:
            start = entry['from']
            end = entry['to']
            if start in self.vertices:
                self.vertices[start][end] = int(entry['duration'])
            else:
                self.vertices[start] = {end: int(entry['duration'])}

    def shortest_path(self, start, end):
        start_adj = self.vertices[start]
        result = {v: {'cost': start_adj[v] if v in start_adj else -1,
                      'path': start + " -> " + v if v in start_adj else start}
                  for v in self.vertices if v != start}
        for i in range(len(self.vertices)-2):
            last_result = result.copy()
            # print(f"{i+2}: ")
            # [print(f"{k}: {v['cost']}") for k, v in last_result.items()]
            for v in self.vertices:
                if v == start or last_result[v]['cost'] == -1:
                    continue
                cur_cost = last_result[v]['cost']
                cur_path = last_result[v]['path']
                # print(f"start checking {v}, curcost={cur_cost}, curpath={cur_path}")
                for next_v, next_cost in self.vertices[v].items():
                    if next_v == start:
                        continue
                    # print(f"next_v={next_v}, last_cost={last_result[next_v]['cost']}, new_cost={cur_cost+next_cost}")
                    if result[next_v]['cost'] == -1 or result[next_v]['cost'] > cur_cost + next_cost:
                        result[next_v] = {'cost': cur_cost + next_cost, 'path': cur_path + ' -> ' + next_v}
                        # print("match")
        print(result[end])

    def all_path(self, start, end):
        self.traverse_all_path(start, end, start, 0)
        for cost in sorted(self.paths.keys()):
            [print(f"cost={cost}, path={path}") for path in self.paths[cost]]

    def traverse_all_path(self, cur, end, path, sum_cost):
        # print(f"cur={cur}, path={path}, cost={sum_cost}")
        if cur == end:
            # print("match!")
            if sum_cost not in self.paths:
                self.paths[sum_cost] = list()
            self.paths[sum_cost].append(path)
            return
        for v, next_cost in self.vertices[cur].items():
            if v in path.split(' -> '):
                continue
            self.traverse_all_path(v, end, f"{path} -> {v}", sum_cost + next_cost)

    def print_graph(self):
        for k, v in self.vertices.items():
            print(k)
            print(v)


raw_route = json.loads('[{"route_id":"A_C","from":"A","to":"C","duration":8},{"route_id":"A_E","from":"A","to":"E","duration":4},{"route_id":"A_F","from":"A","to":"F","duration":8},{"route_id":"A_H","from":"A","to":"H","duration":7},{"route_id":"B_A","from":"B","to":"A","duration":10},{"route_id":"B_C","from":"B","to":"C","duration":3},{"route_id":"B_D","from":"B","to":"D","duration":7},{"route_id":"B_G","from":"B","to":"G","duration":8},{"route_id":"B_H","from":"B","to":"H","duration":1},{"route_id":"C_B","from":"C","to":"B","duration":6},{"route_id":"C_F","from":"C","to":"F","duration":7},{"route_id":"C_G","from":"C","to":"G","duration":10},{"route_id":"C_H","from":"C","to":"H","duration":2},{"route_id":"D_B","from":"D","to":"B","duration":3},{"route_id":"D_C","from":"D","to":"C","duration":1},{"route_id":"D_E","from":"D","to":"E","duration":9},{"route_id":"D_F","from":"D","to":"F","duration":8},{"route_id":"D_G","from":"D","to":"G","duration":10},{"route_id":"E_A","from":"E","to":"A","duration":8},{"route_id":"E_C","from":"E","to":"C","duration":1},{"route_id":"E_F","from":"E","to":"F","duration":3},{"route_id":"E_G","from":"E","to":"G","duration":4},{"route_id":"F_A","from":"F","to":"A","duration":2},{"route_id":"F_B","from":"F","to":"B","duration":9},{ "route_id":"F_C","from":"F","to":"C","duration":2},{"route_id":"F_D","from":"F","to":"D","duration":9},{"route_id":"F_G","from":"F","to":"G","duration":4},{"route_id":"G_A","from":"G","to":"A","duration":9},{"route_id":"G_D","from":"G","to":"D","duration":8},{"route_id":"G_E","from":"G","to":"E","duration":11},{"route_id":"G_F","from":"G","to":"F","duration":7},{"route_id":"G_H","from":"G","to":"H","duration":10},{"route_id":"H_A","from":"H","to":"A","duration":1},{"route_id":"H_B","from":"H","to":"B","duration":8},{"route_id":"H_C","from":"H","to":"C","duration":7},{"route_id":"H_D","from":"H","to":"D","duration":8},{"route_id":"H_F","from":"H","to":"F","duration":6}]')
graph = Graph()
graph.mount_graph(raw_route)
# graph.shortest_path("G", "B")
graph.all_path("G", "B")
# graph.print_graph()
