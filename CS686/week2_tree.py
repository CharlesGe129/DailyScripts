count = 0

class Node:
    def __init__(self, char):
        self.isWord = False
        self.char = char
        self.children = dict()


class AC:
    def __init__(self):
        self.root = Node('')

    def compile(self, filename):
        [self.insert(word) for word in AC.get_data(filename)]

    @staticmethod
    def get_data(filename):
        words = list()
        with open(filename, 'r') as f:
            i = 0
            while True:
                temp = f.readline().strip('\n')
                if temp:
                    words.append(temp)
                    i += 1
                else:
                    break
        return words

    def insert(self, word):
        node = self.root
        i = 0
        # go to the deepest existing node
        for i in range(len(word)):
            letter = word[i]
            if letter in node.children:
                node = node.children[letter]
            else:
                break
        for letter in word[i:]:
            node.children[letter] = Node(letter)
            node = node.children[letter]
        node.isWord = True

    @staticmethod
    def show(node, prefix):
        global count
        prefix += node.char
        if node.isWord or not node.children:
            count += 1
            print(f"{count}: {prefix}")
        if node.children:
            [AC.show(child, prefix) for child in node.children.values()]

    def autocomplete(self, ac):
        prefix = ''
        node = self.root
        i = 0
        # go to the deepest
        for i in range(len(ac)):
            letter = ac[i]
            if letter in node.children:
                node = node.children[letter]
                prefix += letter
                i += 1
            else:
                break
        if i == len(ac):  # has more auto-complete
            AC.show(node, prefix[:len(prefix)-1])


a = AC()
a.compile('data.txt')
# a.show(a.root, '')
a.autocomplete('bare')
