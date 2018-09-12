class Stack:
    def __init__(self):
        self.data = list()
        self.char_map = {'(': ')', '[': ']', '{': '}'}
        self.index = 0

    def push(self, char):
        if char in self.char_map:
            if self.index < len(self.data):
                self.data[self.index] = char
            else:
                self.data.append(char)
            self.index += 1
            return True
        else:
            # print(f"index={self.index}, char={char}, last={self.data[self.index-1]}")
            if self.index == 0 or char != self.char_map[self.data[self.index-1]]:
                return False
            else:
                self.index -= 1
                return True


def verify_closable(text):
    # print("*******************")
    stack = Stack()
    for char in text:
        # print(f"char={char}")
        if not stack.push(char):
            # print(False)
            return False
        # print(True)
    return stack.index == 0

print(verify_closable("[]{}"))
print(verify_closable("[({})]"))
print(verify_closable("[({})][]{()}"))
print(verify_closable("([)]"))
print(verify_closable("([)]"))
print(verify_closable("([)"))
print(verify_closable("[({})][(]{()}"))
print(verify_closable("("))
print(verify_closable("]"))
