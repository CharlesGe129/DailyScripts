import random


class CF:
    def __init__(self, row, col, num):
        self.row = row
        self.col = col
        self.num = num
        self.matrix = [['.' for j in range(col)] for i in range(row)]
        self.over = False
        self.color = True

    def run(self):
        while not self.over:
            print('=========================')
            self.step()
            self.print()

    def step(self):
        y = random.randint(0, self.col - 1)
        x = self.get_row(y)
        if y == -1:
            return
        self.matrix[x][y] = 'X' if self.color else 'O'
        self.color = not self.color
        self.check(x, y)

    def get_row(self, y):
        x = -1
        for i in range(self.row - 1, -1, -1):
            if self.matrix[i][y] == '.':
                x = i
                break
        return x

    def check(self, x, y):
        self.check_single(x, y, 0, 1)
        self.check_single(x, y, 1, 0)
        self.check_single(x, y, 1, 1)
        self.check_single(x, y, -1, 1)

    def check_single(self, x, y, dx, dy):
        color = self.matrix[x][y]
        score = -1
        i = x
        j = y
        while self.row > i >= 0 and self.col > j >= 0 and self.matrix[i][j] == color:
            score += 1
            i += dx
            j += dy
        i = x
        j = y
        dx = -dx
        dy = -dy
        while self.row > i >= 0 and self.col > j >= 0 and self.matrix[i][j] == color:
            score += 1
            i += dx
            j += dy
        if score >= self.num:
            self.over = True
            print(f'finish at row={x+1}, col={y+1}')

    def print(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.matrix[i][j], end='')
            print()


a = CF(7, 6, 4)
a.run()
