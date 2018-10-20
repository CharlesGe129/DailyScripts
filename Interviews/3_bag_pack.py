'''
100
3
10 50
20 150
30 100
40 120
'''


class Bag:
    def __init__(self):
        self.table = dict()
        self.max_money = 100
        self.max_num_items = 3
        self.items = [{'cost': 10, 'value': 50}, {'cost': 20, 'value': 150},
                      {'cost': 30, 'value': 100}, {'cost': 40, 'value': 120}]

    def init_table(self):
        for i in range(self.max_num_items):
            self.table[i+1] = dict()
            for j in range(self.max_money+1):
                self.table[i+1][j] = dict()
                for k in range(len(self.items)):
                    self.table[i+1][j][k+1] = 0

    def start(self):
        # With at most i items, j money, and among first k items
        self.init_table()
        for num_items in range(1, self.max_num_items+1):
            for total_money in range(1, self.max_money+1):
                for first_k_item in range(1, len(self.items)+1):
                    print(f"Fulfill num={num_items}, money={total_money}, first={first_k_item}")
                    item = self.items[first_k_item-1]
                    if total_money < item['cost']:
                        if first_k_item == 1:
                            best_value = 0
                        else:
                            best_value = self.table[num_items][total_money][first_k_item - 1]
                    # If I can choose only 1 item
                    elif num_items == 1:
                        # If only first item
                        if first_k_item == 1:
                            best_value = item['value']
                        else:
                            best_value = max(self.table[1][total_money][first_k_item-1], item['value'])
                    # If only first item
                    elif first_k_item == 1:
                        best_value = item['value']
                    else:
                        print(f"choose among table[{num_items}][{total_money}][{first_k_item-1}]={self.table[num_items][total_money][first_k_item-1]} and table[{num_items-1}][{total_money-item['cost']}][{first_k_item-1}]={self.table[num_items-1][total_money-item['cost']][first_k_item-1]}+{item['value']}")
                        best_value = max(self.table[num_items][total_money][first_k_item-1],
                                         self.table[num_items-1][total_money-item['cost']][first_k_item-1]+item['value'])
                    print(f"best={best_value}")
                    self.table[num_items][total_money][first_k_item] = best_value
        print(self.table[self.max_num_items][self.max_money][len(self.items)])

Bag().start()
