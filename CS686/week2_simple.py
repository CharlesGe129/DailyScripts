class AC:
    def __init__(self):
        self.map = dict()
        chars = 'pyfgcrlaoeuidhtnsqjkxbmwvz'
        for c in chars:
            for d in chars:
                for e in chars:
                    self.map[c + d + e] = list()
                self.map[c + d] = list()
            self.map[c] = list()

    def initial(self, filename):
        array = self.get_data(filename)
        for word in array:
            for i in range(3):
                key = word[0:i + 1]
                if key not in self.map:
                    break
                else:
                    self.map[key].append(word)

    def print(self):
        for each in self.map:
            if self.map[each]:
                print(each)
                print(self.map[each])

    def get_data(self, filename):
        a = list()
        with open(filename, 'r') as f:
            i = 0
            while True:
                temp = f.readline().strip('\n')
                if temp:
                    a.append(temp)
                    i += 1
                else:
                    break
        return a

    def autocomplete(self, key):
        if len(key) > 3:
            array = self.map[key[0:3]]
            for each in array:
                if each.startswith(key):
                    print(each)
        else:
            [print(each) for each in self.map[key]]


a = AC()
a.initial('data.txt')
a.autocomplete('bare')
