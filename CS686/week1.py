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
            print(f"{i}, {y}")
            if self.matrix[i][y] == '.':
                x = i
                break
        return x

    def check(self, x, y):
        self.check_ho(x, y)
        self.check_ve(x, y)
        self.check_le(x, y)
        self.check_ri(x, y)

    def check_ho(self, x, y):
        color = self.matrix[x][y]
        score = 0
        j = y
        while j >= 0:
            if self.matrix[x][j] == color:
                score += 1
            else:
                break
            j -= 1
        if score == self.num:
            self.over = True
            print(f'horizontal [{x}, {y}] to the left')
            return
        score = 0
        j = y
        while j < self.col:
            if self.matrix[x][j] == color:
                score += 1
            else:
                break
            j += 1
        if score == self.num:
            self.over = True
            print(f'horizontal [{x}, {y}] to the right')
            # print(f'color = {self.matrix[x][y]}, less[{x}, {y+1}] = {self.matrix[x][y+1]}, r = {self.matrix[x][y] == self.matrix[x][y+1]}')
            return

    def check_ve(self, x, y):
        color = self.matrix[x][y]
        score = 0
        i = x
        while i >= 0:
            if self.matrix[i][y] == color:
                score += 1
            else:
                break
            i -= 1
        if score == self.num:
            self.over = True
            print(f'vertical [{x}, {y}] to the top')
            return
        score = 0
        i = x
        while i < self.row:
            if self.matrix[i][y] == color:
                score += 1
            else:
                break
            i += 1
        if score == self.num:
            self.over = True
            print(f'vertical [{x}, {y}] to the bottom')
            # print(f'color = {self.matrix[x][y]}, less[{x+1}, {y}] = {self.matrix[x+1][y]}, r = {self.matrix[x][y] == self.matrix[x+1][y]}')
            return

    def check_le(self, x, y):
        color = self.matrix[x][y]
        score = 0
        i = x
        j = y
        while i >= 0 and j >= 0:
            if self.matrix[i][j] == color:
                score += 1
            else:
                break
            i -= 1
            j -= 1
        if score == self.num:
            self.over = True
            print(f'left top [{x}, {y}] to the left top')
            return
        score = 0
        i = x
        j = y
        while i < self.row and j < self.col:
            if self.matrix[i][j] == color:
                score += 1
            else:
                break
            i += 1
            j += 1
        if score == self.num:
            self.over = True
            print(f'right top [{x}, {y}] to the left bottom')
            return

    def check_ri(self, x, y):
        color = self.matrix[x][y]
        score = 0
        i = x
        j = y
        while i >= 0 and j < self.col:
            if self.matrix[i][j] == color:
                score += 1
            else:
                break
            i -= 1
            j += 1
        if score == self.num:
            self.over = True
            print(f'right top [{x}, {y}] to the left bottom')
            return
        score = 0
        i = x
        j = y
        while i < self.row and j >= 0:
            if self.matrix[i][j] == color:
                score += 1
            else:
                break
            i += 1
            j -= 1
        if score == self.num:
            self.over = True
            print(f'right top [{x}, {y}] to the right top')
            return

    def print(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.matrix[i][j], end='')
            print()


a = CF(7, 6, 4)
a.run()