import random


def push(stack1, element):
    stack1.append(element)


def pop(stack1, stack2):
    if not stack2:
        while stack1:
            stack2.append(stack1.pop())
    return stack2.pop()


def check(n):
    data = [i for i in range(n)]
    stack1 = list()
    stack2 = list()
    output = list()
    i = 0
    while i < n or stack1 or stack2:
        if random.randint(0, 1) == 0 and i < n:
            push(stack1, data[i])
            i += 1
        else:
            if stack1 or stack2:
                output.append(pop(stack1, stack2))
    return data == output

for i in range(100):
    if not check(i):
        break
