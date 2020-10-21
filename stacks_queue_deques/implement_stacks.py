# Implementing stacks using list in python
# implement method push/pop/isEmpty/size/peek

class stack():

    def __init__(self):
        self.items = []

    def isEmpty(self):

        return self.items == []

    def push(self, item):

        self.items.append(item)

    def pop(self):

        return self.items.pop()

    def size(self):

        return len(self.items)

    def peek(self):

        return self.items[len(self.items)-1]


test = stack()

#print(test.peek())

test.push('1')

print(test.isEmpty())
print(test.peek())